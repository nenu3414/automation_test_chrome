# import necessory modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
import time

# search btn
def search_result():
    # initialize Chrome webdriver
    bot=webdriver.Chrome(r"Enter device address where chrome webdriver is present")
    # to get data from url
    bot.get('https://www.google.com/')
    # this will delay the execution by 10 second as some of the systems will perform slow due to network issue
    time.sleep(10)
    # closes the screen
    window.quit()
    # this will give value of name in line HTML of chrome web browser
    result=bot.find_element_by_name('q')
    # if anything is already written,clears it
    result.clear()
    # send keys to the search box of chrome web browser
    result.send_keys(entry1.get())
    result.send_keys(Keys.RETURN)

# facebook btn (shortcut key)
def facebook():
    bot1 = webdriver.Chrome(r"Enter device address where chrome webdriver is present")
    bot1.get('https://www.facebook.com/')

# twitter btn (shortcut key)
def twitter():
    bot2 = webdriver.Chrome(r"Enter device address where chrome webdriver is present")
    bot2.get('https://www.twitter.com/')

# github btn (shortcut key)
def github():
    bot3 = webdriver.Chrome(r"Enter device address where chrome webdriver is present")
    bot3.get('https://www.github.com/')

# coursera btn (shortcut key)
def coursera():
    bot4 = webdriver.Chrome(r"Enter device address where chrome webdriver is present")
    bot4.get('https://www.coursera.com/')

window=Tk()
# title given to screen
window.title("Browser")
# geometry given to screen
window.geometry("450x200")
# txt label
search=Label(window,text="What's on your mind? Enter Here.",font='arial 12',fg='red')
search.place(x=10,y=8)
# entry widget
entry1=Entry(window)
# placing as per x and y axis co-ordinates
entry1.place(x=250,y=10)

# search btn with func assigned,width and background color
b1=Button(window,text="Search",command=search_result,width=12,bg='light green')
b1.place(x=170,y=50)

# facebook btn with func assigned,width, background color and font color
b2=Button(window,text="Facebook",command=facebook,width=12,bg='dark blue',fg='white')
b2.place(x=100,y=100)

# twitter btn with func assigned,width, background color and font color
b3=Button(window,text="Twitter",command=twitter,width=12,bg='red',fg='yellow')
b3.place(x=100,y=150)

# github btn with func assigned,width, background color and font color
b4=Button(window,text="Github",command=github,width=12,bg='red',fg='yellow')
b4.place(x=240,y=100)

# coursera btn with func assigned,width, background color and font color
b5=Button(window,text="Coursera",command=coursera,width=12,bg='dark blue',fg='white')
b5.place(x=240,y=150)

# infinite loop to run the application as long as window is not closed
window.mainloop()