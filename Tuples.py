"""Inmutable sequence of arbitrary objects
    Declaration: a = (2,3,'Mere')"""
#Tuple unpacking tutorial: https://www.geeksforgeeks.org/unpacking-a-tuple-in-python/


def tuple_constructor(String):
    """tuple(something) creates a tuple from an interable object"""
    return tuple(String)


def reverse_name(LastName,FirstName):
    """Reverse the content of the function definition using Tupel unpacking"""
    LastName, FirstName = FirstName, LastName
    return LastName, FirstName


def checkIfExistInTuple(element,tuple):
    return element in tuple


def minMax(items):
    """Shows how unpacking works"""
    return min(items), max(items)


'''
Empty tuple: a = ('Mere',)
Nested tuple: a = ((220, 284), (1184, 1210), (2620, 2924))
              Try to see what a[2][1] returns
Concetenation: a = ('Mere',2,"Ana")
               b = (1,2)
               c = a + b
'''