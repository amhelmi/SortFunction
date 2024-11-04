#!/usr/bin/env python3
import numpy as np
import string

def sort(width, height, length, mass):
    '''
    Sorts packages based on criteria for bulky and heavy packages as defined below.
    - A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
    - A package is **heavy** when its mass is greater or equal to 20 kg.

    Keyword arguments:
    width: width of package in cm (float)
    height: height of package in cm (float)
    length: length of package in cm (float)
    mass: mass of package in kg (float)

    Returns: String with the name of the stack for the package
    '''
    bulky = False
    heavy = False
    valsArray = np.array([width, height, length])
    volume = width * height * length
    # check for elements with 0 dimension, return as error
    if (valsArray == 0).any() or mass == 0:
        print("Error: At least one dimension is 0 and therefore invalid.")
        return "Error".upper()
    # check for bulky
    if volume >= 1000000 or (valsArray >= 150).any():
        bulky = True
    # check for heavy
    if mass >= 20:
        heavy = True

    if bulky and heavy:
        return "Rejected".upper()
    elif bulky or heavy:
        return "Special".upper()
    else:
        return "Standard".upper()
    
    return "Error".upper()

if __name__ == "__main__":
    # test cases
    correct = ["SPECIAL","SPECIAL","REJECTED","STANDARD","ERROR"]

    testBulky = sort(160,100,10,10)
    testHeavy = sort(50,100,100,25)
    testRejected = sort(150,150,150,20)
    testStandard = sort(15,15,25,5)
    testError = sort(10,25,0,35)
    tests = [testBulky,testHeavy,testRejected,testStandard,testError]

    if correct == tests:
        print("All tests pass")
    else:
        print("One test failed: ", tests)
