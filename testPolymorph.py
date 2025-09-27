#!/usr/bin/env python3

# File Name: testPolymorph.py

class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid File Type")
        
        self.filename = filename
        
class MP3File(AudioFile):
    ext = "mp3"
    
    def play(self):
        print("Playing {0} as mp3".format(self.filename))
        
class OGGFile(AudioFile):
    ext = "ogg"
    
    def play(self):
        print("Playing {0} as ogg".format(self.filename))
        
 