from tkinter import*            ## to import TKinter library 
import tkinter.font             ## Font associated with TKinter 
from gpiozero import LED                    
import RPi.GPIO                 ## To import GPIO library 
RPi.GPIO.setmode(RPi.GPIO.BCM)  
import time                     ## to get the current time

## hardware
Led = LED (14)                  ## Defining pin for my LED 

## GUI DEFINITIONS ##
win = Tk()                      ## It creates an interface to the GUI toolkit
win.title("GUI - Morse Code")   ## Defining the title of the window
myFont = tkinter.font. Font(family = 'Helvetica', size = 12, weight = "bold") ## Title font selection


## Defining morse code pattern for every letter
translate_dict = { 'A':'.-', 
                   'B':'-...',
                    'C':'-.-.', 
                    'D':'-..', 
                    'E':'.',
                    'F':'..-.', 
                    'G':'--.', 
                    'H':'....',
                    'I':'..', 
                    'J':'.---',
                     'K':'-.-',
                    'L':'.-..',
                     'M':'--', 
                     'N':'-.',
                    'O':'---',
                     'P':'.--.', 
                     'Q':'--.-',
                    'R':'.-.',
                     'S':'...', 
                     'T':'-',
                    'U':'..-', 
                    'V':'...-',
                     'W':'.--',
                    'X':'-..-', 
                    'Y':'-.--', 
                    'Z':'--..',
                    '1':'.----', 
                    '2':'..---', 
                    '3':'...--',
                    '4':'....-', 
                    '5':'.....', 
                    '6':'-....',
                    '7':'--...', 
                    '8':'---..', 
                    '9':'----.',
                    '0':'-----', 
                    ', ':'--..--', 
                    '.':'.-.-.-',
                    '?':'..--..', 
                    '/':'-..-.', 
                    '-':'-....-',
                    '(':'-.--.',
                     ')':'-.--.-'}
ledinput = str()

## Initialsing the blink for dash 
def dash():
    Led.on()
    time.sleep(1.0)
    Led.off()
    time.sleep(0.3)

## Initialising the blink for a dot 
def dot():
    Led.on()
    time.sleep(0.5)
    Led.off()
    time.sleep(0.1)

## Analysing the input in the box and responding respectively 
def Analysing_input(ledinput):
    ledinput = code.get()           ## getting the input

    ledinput = " ".join(translate_dict[char] for char in ledinput.upper())
    print(ledinput)     ## Printing the input

    for char in ledinput:       ## defining variable named "char"
        if char == ".":         ## If the morse code pattern of the written character is dot
            dot()               ## blink dot

        elif char == "-":       ## If the morse code pattern of the written character is dash
            dash()              ## blink dash

        elif char == "/" or char == " ":   ## if invalid or no input is given, then no change is made
            time.sleep(0.5)

        else:
            print("Enter a valid Character")            ## If an invalid character is entered, New entry will be asked. 

def close():                    ## closing the window
    RPi.GPIO.cleanup()
    win.destroy()


###### 
ledButton = Button (win, text = 'Blink Name', font = myFont, command = lambda: Analysing_input(ledinput), bg = 'orange', height = 1)     
ledButton.grid (row=1, column=1)                        

code = Entry(win, font=myFont, width=10)                
code.grid(row=0, column=1)                              

exitButton = Button (win, text = 'Exit', font = myFont, command = close, bg = 'aqua', height = 1, width = 6)        
exitButton.grid (row=2, column=1)                       

win.protocol("WM_DELETE_WINDOW", close)         # exit cleanly 
win.mainloop()                                  # Loop forever
