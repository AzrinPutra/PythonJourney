#!/usr/env/bin python3
# To test this code in terminal, go to the folder that has this py file
# Run python3
# from collections.abc import Container
# In Python3, collections is deprecated and moved to ollections.abc
# from abstractclass import OddContainer
# This extracts the class OddContainer

class OddContainer:
    def __contains__(self, x):
        if not isinstance(x , int) or not x % 2:
            return False
        return True