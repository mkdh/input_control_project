# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 09:12:44 2018

@author: User
"""

from pynput import keyboard
import cls_thread

#import pyautogui
#import threading
import sys

class Status:
    my_exit = False
    my_active = True
    my_current_loop = 0

#names = [str(i) for i in range(0, 10, 1)]

#width, height = pyautogui.size()

def mainThread():
    listenerThread = keyboard.Listener(on_press = onKeyPress)
    listenerThread.start()

    while(not Status.my_exit):
        if (not Status.my_active):
            continue

        myMainEvent()

    keyboard.Listener.stop(listenerThread)
    print("Stopped listerning")
    sys.exit(0)

def onKeyPress(key):
    print("Still listerning")

    try:
        k = key.char
    except Exception:
        k = key.name

    if (k == "z"):
        Status.my_active = not Status.my_active

    elif (k == "x"):
        Status.my_exit = not Status.my_exit


    #---------------- Even Code Write Here -----------------------
def myMainEvent():    
    from pynput.keyboard import Controller, Key
    import time
    keyboard = Controller()
    
    if Status.my_current_loop == 0:        
        with keyboard .pressed(Key.alt):
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)

    time.sleep(0.2)   # Delays for 5 seconds. You can also use a float value.
    
    '''
    This is infinite loop. The index of loop will start from 0.
    It means the Status.my_current_loop == 0 as above code.
    '''
    if Status.my_current_loop < 16:   
        keyboard.type(",\"")
        keyboard.press(Key.end)
        keyboard.release(Key.end)
        keyboard.type("\"")
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.home)
        keyboard.release(Key.home)
    
    
    
    '''
    with keyboard .pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')        
    '''
    Status.my_current_loop = Status.my_current_loop + 1
    #Status.my_exit = not Status.my_exit

    #---------------------------------------

'''
from pynput.mouse import Button, Controller, Key
mouse = Controller()
mouse.position = (0, 0)
mouse.move(0, 10)
mouse.click(Button.right, 1)

mouse.press(Key.cmd.value)
mouse.press('x')
mouse.release('v')
# keyboard.release(Key.ctrl.value) #this would be for your key combination
mouse.release(Key.cmd.value)
'''


#controlThread = threading.Thread(target = mainThread)
#controlThread.start()

mainThread()
cls_thread.Thread().mainThread()

