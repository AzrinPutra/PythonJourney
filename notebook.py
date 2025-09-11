#!/usr/bin/env python3

# File Name: notebook.py

import datetime

class Notebook:
    """ Represent a collection of notes that can be tagged,
    modified and searched..
    """
    
    def __init__(self):
        """ Initialize a notebook with an empty list """
        self.notes = []
        
    def new_note(self, memo, tags=""):
        """ Create a new note and append it to the list """
        self.notes.append(Note(memo, tags=""))
    
    def _find_note(self, note_id):
        """ Locate note with the given id """
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
        
    def modify_memo(self, note_id, memo):
        """ Find the note with the given id and change its 
        memo to the given value.
        """
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        else:
            return False
                
    def modify_tags(self, note_id, tags):
        """ Find the note with the given id and change its tags 
        to the given value
        """
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        else:
            return False
                
    def search(self, filter):
        """ Find all notes that match the given filter """
        for note in self.notes:
            if note.match(filter):
                return note
        
    

# Store the next available id for all the new notes
last_id = 0

class Note:
    """ Represent a note in the notebook. Match against a string
    in searches and store tags for each notes
    """
    
    def __init__(self, memo, tags=""):
        """ Initialize a note with memo and optional space-separated
        tags. Automatically set the note's creation date and a unique
        id.
        """
        
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
        
    def match(self, filter):
        """ Determine if this note matches the filter text. Return
        True if it matches. Return False if otherwise. Search is 
        case-sensitive and matches both text and tags via interation of strings
        """
        
        return filter in self.memo or filter in self.tags