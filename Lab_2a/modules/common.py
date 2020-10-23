import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform



def func(x):
    for i in range(101):
        if(x == True and i % 2 == 0):
            print(i)
        elif(x == False and i % 2 != 0):
            print(i)
func(True)