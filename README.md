# CountDown-Timer
GUI countdown timer created using Python! Enjoy
PROJECT TITLE: TIMER + ALARM APP
Video Demo: https://youtu.be/ivRIr-tgw4w
Compiled by: Mohammad Ahnaf
City, Country: Ajman, UAE
Date: 6th May 2024
Discord: chikanlegbees#9759
Reddit: mo_ahnaf11
edX: mo_ahnaf11
github: moahnaf11

Steps to set it up from source:
Open your IDE and make sure you have set up a virtual environment. Run the command `pip install python-dateutil` in your terminal to load this 3rd party package and then run the command `pip install pyttsx3` in your terminal to load the next 3rd party package, then run the command `pip install pillow` in your terminal to load the next and final 3rd party package to use the app! Copy - Paste the source code timerapp.py to ur IDE and run! The app should be displayed

Project Description:
I created a timer app using Python! previously it was a CLI(Command-Line-Interface) program, over time I turned into a GUI(Graphical-User-Interface) application . My project is basically made for students in school or university. Its basically a countdown app which allows people to keep track of time and help with time management. My Project's functionality is that it allows the user to input a date and then time after which it will countdown to that specific date and time. When the timer hits 0 it will output in voice saying "FINISH" and then it will start a beeping sound hence the alarm aspect to my project! There's a snooze button which allows the user to temporarily pause the the beeping sound for 45 seconds, a snooze timer of 45 seconds commences once the snooze button is clicked. If the user however would like to exit from the application once the timer completes they can simply click the close button or the X on the top right of the application bar. The user can snooze however many times he/she wishes.

My app was mainly designed for students in school/university but its free to use by anyone! People could use this app for time management purposes. It can be used to check the delta between the current date and time to a user specific date and time while also counting down to it!. My project was inspired by the fact that most browser timer sites dont really allow the user to input the date and time together and then output a continuous countdown to it! Most sites would just output the delta between the current date and time and output the delta as days left for example without displaying it in a timer format with seconds decrementing by 1 and so on. Or they'd just allow the user to input the date and then display the delta to that date assuming the users want to see the delta to 00:00 midnight on that specific date he/she has specified. Or in other cases the display is in a few units only for example days or hours etc whereas my app would display the delta in years, months, days, hours, minutes and seconds respectively. My timer app provides the user with some more flexibilty and functionality in terms of user inputs(date and time) and timer displays!

Instructions For Use:
Run the script. The app window will be displayed as well as a black window in the background which is simply the command prompt, minimise the command prompt but do not close it as this will kill the program! You can enlarge the timerapp window but its best to use it as it is in terms of the window size that is displayed!

Date Formats Supported:
This app is designed for users worldwide. There are a few conventions on how Dates are represented in various parts of the world. To accommodate for the differences in practices by different countries worldwide the user is given an option to input the date in a format which suits them best! The 3 formats allowed are DD/MM/YYYY , MM/DD/YYYY and YYYY/MM/DD respectively. The app is designed to allow users to input the date in any of the 3 formats, Simply click YES or NO as the 3 date formats are prompted to you, if you have accidentally clicked NO on the date format you prefer simply click NO on the others as it will display the prompts in a loop so you can click YES the next time around!

Date Input Format:
Simply enter the date in the format you have chosen for example if the date you would like to input is the 6th of May, and you have chosen the DD/MM/YYYY format simply input either 6/5/2024 or 06/05/2024, the leading zeros are not necessary but you can type them if you wish, the same applies for the other date formats! If your input is invalid the enter button will simply clear the entry box for you to re-type the date in the specified format

Time Input Format:
Simply enter the time in the 24 hour format, 12 hour formats are not supported so if the time you'd like to countdown to is 9 AM on that specific date, enter 09:00, leading zeros are very important here otherwise the input will be invalid. Similarly like the date entry, if the time input is invalid or not in the specified format clicking enter wll clear the entry box allowing for re_entry. If however the date and times are in the correct format and clicking enter after time displays the date entry again, this means the date and time you have entered is in the past. The app only supports countdown to a future date and time. For example today is May 6 2024, 09:00, if you type date in the correct format but enter time 08:59 the app will take u back to the date entry as May 6 2024 08:59 has passed and it can't display a negative countdown!

Snooze:
After date and times have been inputted correctly the timer will be displayed! After timer is completed the beep will commence after which you have the option to snooze using the snooze button or end the program with the close button. You can also click close while the timer is displayed to end the program.


This was my Project! I hope you may find this beneficial to you! A sweet alternative to using browser timer applications.
Thank You for reading! 

Feel free to reach out to some of my socials I have listed at the top of this document!










