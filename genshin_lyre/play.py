import time

import keyboard
import pyautogui


pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False
pyautogui.DARWIN_CATCH_UP_TIME = 0


sleep_scale = 1
is_pause = False


class Key_listener():
    def __init__(self):
        pass
    
    def speed_up(self):
        global sleep_scale
        
        if sleep_scale >= 0.2:
            sleep_scale -= 0.2
            time.sleep(1)
        
    def speed_down(self):
        global sleep_scale
        
        if sleep_scale <= 2.0:
            sleep_scale += 0.2
            time.sleep(1)
            
    def pause(self):
        global is_pause
        
        is_pause = not is_pause
        time.sleep(1)
            
    def set_hotkey(self):
        keyboard.add_hotkey(hotkey="Right", callback=self.speed_up)    
        keyboard.add_hotkey(hotkey="Left", callback=self.speed_down)
        keyboard.add_hotkey(hotkey="Space", callback=self.pause)

    
def play(sheet):
    global sleep_scale, is_pause
    sleep_scale = 1
    
    key_listener = Key_listener()
    key_listener.set_hotkey()
    
    sheet.pop(0) # duration
    
    for element in sheet:
        while is_pause:
            time.sleep(0.1)
        
        press_keys, wait = element[0], element[1] * sleep_scale
        
        print(press_keys, wait)
        
        if len(press_keys) == 1:
            if press_keys[0] != "none":
                pyautogui.press(press_keys[0])
        
        else:
            pyautogui.press(press_keys)
        
        time.sleep(wait)