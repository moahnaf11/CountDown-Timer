""" 
Created by: Mohammad Ahnaf
City, Country: Ajman, UAE
Date: 6th May 2024
Discord: chikanlegbees#9759
Reddit: mo_ahnaf11
edX: mo_ahnaf11
github: moahnaf11

"""


from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import re
import pyttsx3
import tkinter as tk
from PIL import ImageTk, Image
import winsound

"""instantiates the timer app window store the variables prompts which are used for date entries
   stores index and fonts for texts/ buttons
   Creates the window assigns timericon
   Fixes app label
   Places the timer image as label
   Beep set to true for snooze
   
"""
class App(tk.Tk):
    prompts = ["Would you like to write the date in this format DD/MM/YYYY ?",
            "Would you like to write the date in this format MM/DD/YYYY ?",
            "Would you like to write the date in this format YYYY/MM/DD ?"
        ]
    index = 0
    font = ("Times", 14, "bold")
    font_button = ("Times", 13, "bold")
    font_entry = ("Times", 13, "bold")
    font_date = ("Arial", 12, "bold")
    beep = True

    def __init__(self):
        super().__init__()
        self.timericon = tk.PhotoImage(file="pngegg.png")
        self.app_label = tk.Label(self, text="CountDown Timer", font=self.font_date, fg="black", borderwidth=4, relief=tk.RIDGE)
        self.timerimage = Image.open("timer.png")
        self.timerimage.thumbnail((90,90))
        self.timer_image = ImageTk.PhotoImage(self.timerimage)
        self.image_label = tk.Label(self, image=self.timer_image)


        self.geometry("775x320")
        self.resizable(True, True)
        self.title("Timer App")
        self.app_label.pack(ipadx=60)
        self.image_label.pack(pady=10)
        self.iconphoto(False, self.timericon)

"""
Instantiates all my label widgets!
"""
class Mylabel(tk.Label):
    def __init__(self):
        super().__init__()
        self.date_format_label = tk.Label(app, text=app.prompts[app.index], font=app.font_date, fg="black")
        self.date_label = tk.Label(app, text="", font=app.font, fg="black")
        self.time_label = tk.Label(app, text="Enter time in the 24hr format -> 00:00 ", font=app.font)
        self.display = tk.Label(app, text="", font=("Courier New", 12, "bold"), borderwidth=4, relief=tk.SOLID)
        self.finish_label = tk.Label(app, text="FINISH", font=("Arial", 12, "underline", "bold"))

"""
Frame instantiated and packed for storing YES and NO Buttons 
"""      
class Myframe(tk.Frame):
    def __init__(self):
        super().__init__()
        self.frame = tk.Frame(app, borderwidth=5, border= 5, relief=tk.RAISED)
        self.frame.pack(pady=10)

"""
All Buttons Instantiated 
"""
class Mybutton(tk.Button):
    def __init__(self):
        super().__init__()
        self.yes_button = tk.Button(frames.frame, text="YES", font=app.font_date, bg="green", borderwidth=4, relief=tk.SUNKEN, width=5, command=yes)
        self.no_button = tk.Button(frames.frame, text="NO", font=app.font_date, bg="red", borderwidth=4, relief=tk.SUNKEN, width=5, command=no)
        self.enter_button = tk.Button(app, text="ENTER", bg="green", font=app.font_button, relief=tk.RAISED, command=enter )
        self.entertime_button = tk.Button(app, text="ENTER", bg="green", font=app.font_button, relief=tk.RAISED, command=entertime)
        self.close_button = tk.Button(app, text="Close", font=app.font_button, relief=tk.RAISED, borderwidth=5, command=app.destroy, bg="red")
        self.snooze_button = tk.Button(app, text="SNOOZE", font=("Times", 10, "bold"), relief=tk.RAISED, borderwidth=5, command=snooze, bg="yellow")

"""
Entry Widgets Instantiated
"""  
class Myentry(tk.Entry):
    def __init__(self):
        super().__init__()
        self.date_entry = tk.Entry(app, text="", font= app.font_entry, justify=tk.CENTER, width=20, borderwidth=5)
        self.time_entry = tk.Entry(app, text="", font=app.font_entry, justify=tk.CENTER, borderwidth=5, width=20)

"""
Functionality for the YES Button!
"""
def yes():
    global prompt
    if app.index == 0:
        prompt = "Enter Date in the format -> DD/MM/YYYY "
    elif app.index == 1:
        prompt = "Enter Date in the format -> MM/DD/YYYY "
    else:
        prompt = "Enter Date in the format -> YYYY/MM/DD "
    label.date_format_label.destroy()
    frames.frame.destroy()
    getdate()
    
"""
Functionality for the No Button!
"""   
def no():
    app.index += 1
    label.date_format_label.config(text=app.prompts[app.index])
    if app.index == 2:
        app.index = -1

"""
Packs label widget/ entry widget and enter button for the users date entry!
"""
def getdate():
    label.date_label.pack()
    label.date_label.config(text=prompt)
    entry.date_entry.delete(0, tk.END)
    entry.date_entry.pack(pady=10)
    button.enter_button.pack(ipadx=30)

"""
Enter Button functionality for users date entry
"""
def enter():
    usersdate = entry.date_entry.get().strip()
    label.date_label.pack_forget()
    entry.date_entry.pack_forget()
    button.enter_button.pack_forget()
    checkdate(usersdate)

"""
Users date validation and reprompt if needed!
"""
def checkdate(usersdate):
    global year, month, day
    if app.index == 0:
        try:
            day, month, year = map(int, usersdate.split("/"))
            datetime(year, month, day)
            gettime()
        except ValueError:
            getdate()
    elif app.index == 1:
        try:
            month, day, year = map(int, usersdate.split("/"))
            datetime(year, month, day)
            gettime()
        except ValueError:
            getdate()
    else:
        try:
            year, month, day = map(int, usersdate.split("/"))
            datetime(year, month, day)
            gettime()
            
        except ValueError:
            getdate()

"""
Time entry prompt label widgets/ entry widgets / enter button for time entry packing!
"""
def gettime():
    label.time_label.pack()
    entry.time_entry.delete(0, tk.END)
    entry.time_entry.pack(pady=10)
    button.entertime_button.pack(ipadx=30)

"""
Enter Button functionality for users time entry
"""
def entertime():
    global usersdatettime
    pattern = r"((0\d|1\d|2[0-3]):[0-5]\d$)"
    userstime = entry.time_entry.get()
    if match := re.search(pattern, userstime):
        hour, minute = map(int, userstime.split(":"))
        usersdatettime = datetime(year, month, day, hour, minute)
        if usersdatettime > datetime.now():
            destroy()
            displaywindow()
        else:
            destroy()
            getdate()
    else:
        destroy()
        gettime()

"""
Destruction of all widgets after time entered 
"""
def destroy():
    label.time_label.pack_forget()
    entry.time_entry.pack_forget()
    button.entertime_button.pack_forget()

"""
Display functionality for app window
"""
def displaywindow():
    label.display.pack(pady=10, padx=(10,10))
    button.close_button.pack(ipadx=30, side=tk.BOTTOM, pady=10)
    displaytimer()

"""
Timer widget displayed with countdown checks for components when they are Zero
Voice output of Finish 
Snooze button 
"""
def displaytimer():
    delta = relativedelta(usersdatettime, datetime.now())
    time_components = [delta.years, delta.months, delta.days, delta.hours, delta.minutes, delta.seconds]
    text_var = f"{delta.years} year(s) : {delta.months} month(s) : {delta.days} day(s) : {delta.hours} hour(s) : {delta.minutes} minute(s) : {delta.seconds} second(s)"
    label.display.config(text=text_var)
    
    if all(element == 0 for element in time_components):
        label.finish_label.pack()
        engine = pyttsx3.init()
        engine.say("Finish")
        button.snooze_button.pack(pady=5, ipadx=40)
        engine.runAndWait()
        beep()
    else:
        app.after(1000, displaytimer)
    
"""
BEEP sound when timer hits Zero
"""
def beep():
    if app.beep == True:
        winsound.Beep(500, 500)
        app.after(1000, beep)

"""
Snooze button functionality
"""
def snooze():
    seconds = 45
    app.beep = False
    snoozetimer(seconds)
    
"""
Display SNOOZE countdown of 45 seconds 
"""
def snoozetimer(seconds):
    label.display.config(text=f"{seconds} second(s)", width=20)
    if seconds == 0:
        app.beep = True
        beep()
    else:
        app.after(1000, snoozetimer, seconds-1)

"""
Instantiating objects of each class
"""
def main():
    global app, label, frames, button, entry
    app = App() 
    label = Mylabel()
    label.date_format_label.pack(pady=10) 
    frames = Myframe() 
    button = Mybutton()  
    button.yes_button.pack(side=tk.LEFT)  
    button.no_button.pack(side=tk.LEFT)   
    entry = Myentry()
    app.mainloop()

if __name__=="__main__":
    main()
   

