import os
import time

import pyuac
import Levenshtein
import win32gui, win32con, win32api

from play import play
from library.process_json_sheet import JsonSheet
from library.process_midi import MidiFile


def search_file(directory, query, similarity=0.7):
    result = []
    
    for file in os.listdir(directory):
        filename = file.split(".")[0].lower()
        
        if any([Levenshtein.ratio(name, query.lower()) >= similarity for name in filename.split("_")]): 
            result.append(file)
            
    return result

def main():
    type = input("請輸入樂譜類型 (json / midi) ")
    
    while type not in ["json", "midi"]:
        type = input('類型錯誤，請選擇 "json" 或 "midi" ')
        
    name = input("請輸入樂譜名稱，或輸入 list 顯示所有樂譜 ")
    if name == "list":
        files = search_file(f"./assets/sheet/{type}", name, similarity=0)
    
    else:    
        files = search_file(f"./assets/sheet/{type}", name)
    
    while files == []:
        name = input("未找到符合的樂譜，請輸入樂譜名稱，或輸入 list 顯示所有樂譜 ")
        if name == "list":
            files = search_file(f"./assets/sheet/{type}", name, similarity=0)
            
        else:
            files = search_file(f"./assets/sheet/{type}", name)
        
    for count, file in enumerate(files):
        print(f"{count:3}. {file}")
    
    number = int(input("請從上方選擇樂譜編號 "))
    
    while number >= len(files):
        number = int(input("編號錯誤，請從上方選擇樂譜編號 "))
    
    sheet = files[number]
    
    if type == "json":
        processed_sheet = JsonSheet(sheet).process()

    elif type == "midi":
        processed_sheet = MidiFile(sheet).process()
        
    #print(processed_sheet)
    
    try:
        print("請打開風物之詩琴")
        
        #genshin = win32gui.FindWindow(None, "原神")
        #win32gui.SetForegroundWindow(genshin)
        
        time.sleep(5)
        
        play(processed_sheet)
        
    except Exception as e:
        print("未找到原神，請打開應用程式。")
        print(e)


if __name__ == "__main__":
    #if not pyuac.isUserAdmin():
    #    pyuac.runAsAdmin()
        
    #else:
        while True:
            main()