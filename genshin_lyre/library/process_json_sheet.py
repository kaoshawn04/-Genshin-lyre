from library.converter import Converter
from library.config_parser import get_config


notes_list = get_config("notes_list")[0].split("\n")


class JsonSheet():
    def __init__(self, song, song_part):
        self.song = song
        self.song_part = song_part
        self.converter = Converter("json_sheet")
    
    def change_key(self, notes, key):
        change = lambda note: notes_list[(notes_list.index(note) + key)]
        result = [change(note) if note != "none" else "none" for note in notes]

        return result
    
    def process(self):
        song_bpm = self.song["bpm"]
        song_key = self.song["key"]
        song_time_signature = self.song["time_signature"].split("/")
        
        result = []

        for element in self.song[self.song_part]:
            element = element.split()

            if element[0] == "change":
                match element[1]:
                    case "bpm": song_bpm = int(element[2])
                    case "time_signature": song_time_signature = element[2]

            else:
                notes, pause = element[0].split(","), (float(element[1]) / int(song_time_signature[1])) * (60 / int(song_bpm))

                if song_key != 0:
                    notes = self.change_key(notes, song_key)

                press_key = [self.converter.convert(note) for note in notes]

            result.append((press_key, round(pause, 5)))
        
        return result