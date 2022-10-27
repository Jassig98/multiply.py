#Author: Jasmine Singh
#Github Username: Jassig98
#Date: October 26, 2022
#Description: Recrusive function that finds product of two positive integers using them as parameters


def multiply(a,b):
    """This function multiplies given numbers"""
    if (a==0):
        return 0
    else:
        return b+multiply(a-1,b)
