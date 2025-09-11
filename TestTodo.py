#!/usr/bin/env python3

# File Name: TestTodo.py

import datetime

class Todo:
    def __init__(self):
        self.notes = []
        
    def add_note(self, memo):
        return self.notes.append(Note(memo, tags=""))
    
    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        else:
            return None
        
    def modify_note(self, note_id, memo):
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        else:
            return False
        
    def modify_tags(self, note_id, tags):
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        else:
            return False
        
    def search(self, filter):
        for note in self.notes:
            if note.match(filter):
                return note

last_id = 0
   
class Note:
    def __init__(self, memo, tags=""):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        last_id += 1
        self.id = last_id
    
    def match(self, filter):
        return filter in self.notes or filter in self.tags