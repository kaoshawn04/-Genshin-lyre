import time
import json
import glob
import pyautogui
import win32gui, win32con, win32api

from library.process_json_sheet import JsonSheet
from library.process_midi import MidiFile


pyautogui.PAUSE = 0
pyautogui.DARWIN_CATCH_UP_TIME = 0

    
def play_sheet(sheet):
    for element in sheet:
        press_keys, pause = element[0], element[1]
        
        if len(press_keys) == 1:
            if press_keys[0] != "none":
                pyautogui.press(press_keys[0])
        
        else:
            pyautogui.press(press_keys)
            
        time.sleep(pause)
        

if __name__ == "__main__":
    type = int(input("樂譜類型( 0:json / 1:midi):"))
    name = input("name:")
    
    if type == 0:
        songs = json.load(open("assets/songs.json"))
        song = next(song for song in songs if song["name"] == name)
        sheet = JsonSheet(song, "main").process()
        
    else:
        sheet = MidiFile(f"assets/midi/{name}.mid").process()
    
    genshin = win32gui.FindWindow(None, "原神")
    win32gui.SetForegroundWindow(genshin)
    
    time.sleep(3)
    
    play_sheet(sheet)