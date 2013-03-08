#!/usr/bin/python
from Tkinter import *
import GPIO           # importing GPIO library 
led = 4               # assigning the gpio_4 to variable led   
GPIO.export(led)      # exporting the gpio_4  
GPIO.setup(led,1)     # make the gpio_4 as output pin by the value 1
def ledon():          # function for turning on an led
    print "turn on"
    GPIO.write(led,1)
def ledoff():         #function for turning off an led
    print "turn off"
    GPIO.write(led,0)
root =Tk()
 
button1 = Button(root,text="ON",command=ledon)   #assigning the function ledon to the button "ON" 
button2 = Button(root,text="OFF",command=ledoff) #assigning the function ledoff to the button "OFF"
button1.pack(side = LEFT )                       #alignment for the button "ON"
button2.pack(side = RIGHT)                       #alignment for the button "OFF"
root.mainloop()
