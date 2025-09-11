#!/usr/bin/env Python3

# File Name: SuperInitTest_V2.py

class Baseclass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1
        
class LeftSubClass(Baseclass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Left Subclass")
        self.num_left_calls += 1
    
class RightSubClass(Baseclass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Right Subclass")
        self.num_right_calls += 0
        
class Subclass(LeftSubClass, RightSubClass):
    num_sub_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on subclass")
        self.num_sub_calls += 1

