# Point Blank Macro Script By Afrizal F.A - ICWR Development Team

import os, pyautogui
from pynput.mouse import Listener as l
from pynput import keyboard

class auto_on:

    def on_press(self, key):

        if key == keyboard.Key.f1:

            self.stop = True

    def on_click(self, x, y, button, pressed):

        if pressed == True:

            pyautogui.click(button='left')
            pyautogui.press(3)
            pyautogui.press(1)

        else:

            pass

    def __init__(self):

        self.stop = False
        listener =  keyboard.Listener(on_press=self.on_press)
        listener.start()
        l(on_click=self.on_click).start()
        
        while(True):

            if self.stop == True:

                exit()

            else:

                break

auto_on()
