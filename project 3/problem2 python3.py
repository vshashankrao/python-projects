"""
Author: your name
Module for Homework 3, Problem 2
Object Oriented Programming (50:198:113), Spring 2019

Insert your Time class implementation below,
along with proper documentation. 
"""

class Time:
    def __init__(self, init_hr = 12, init_min = 0, init_ampm = "AM"):
        if init_hr < 1 or init_hr > 12:
            raise Exception("Error: Invalid hour for Time object")
        if init_min < 0 or init_min > 59:
            raise Exception("Error: Invalid minute for Time object")
        init_ampm = init_ampm.upper()
        if init_ampm != "AM" and init_ampm != "PM":
            raise Exception("Error: Invalid am/pm flag for Time object")

        self.hr = init_hr
        self.min = init_min
        self.ampm = init_ampm


    # IMPLEMENT THE REMAINING METHODS OF THE Time CLASS BELOW!!


