import mido

from library.converter import Converter


class MidiFile():
    def __init__(self, file):
        self.file = file
        self.converter = Converter("midi")
             
    def process(self):
        midi = mido.MidiFile(self.file, clip=True)
        result = []
        
        for i, message in enumerate(midi):
            if message.type == "note_on":
                note, velocity, time = message.note, message.velocity, message.time
                
                if velocity > 0:
                    if time > 0:
                        r = [[self.converter.convert(note)], time]
                        
                    elif time == 0:
                        if len(result) > 0 and result[-1][0] != ["none"]:
                            lr = result.pop(-1)
                            lr[0].append(self.converter.convert(note))
                            
                            r = [lr[0], time]
                        
                        else:
                            r = [[self.converter.convert(note)], time]
                        
                    result.append(r)
                
                elif velocity == 0:
                    if time > 0:
                        r = [["none"], time]
                    
                        result.append(r)
                        
            elif type == "control_change":
                time = message.time
                
                if time > 0:
                    r = [["none"], time]
                    
                    result.append(r)
                    
        for i in range(len(result)):
            if (i + 1) == len(result):
                result[i][1] = 0
                
            else:
                result[i][1] = result[i + 1][1]
            
            if len(result[i][0]) > 1 and "none" in result[i][0]:
                result[i][0].remove("none")
                
            result[i] = tuple(result[i])
                
        return result
   
"""
midi = MidiFile("assets/midi/lemon.mid")
sheet = midi.process()

with open("processed_lemon_mid.txt", "w") as file:
    for message in sheet:
        file.write(str(message) + "\n")
""" 