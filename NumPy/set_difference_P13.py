'''

@Author: Suresh
@Date: 2024-07-26
@Last Modified by: Suresh
@Last Modified: 2024-07-26
@Title : Python program to find the set difference of two arrays.

'''

import numpy as np
import myloggingfile
import os

fname = os.path.basename(__file__)
logger =myloggingfile.logger_init(fname)

def set_differece(array1,array2):

    """
    Description: Function to finding the set difference between the two given arrays
    Parameters:
        array1: Function taking the given array1 as parameters 
        array2: Function taking the given array2 as parameters 
    Returns:
        None:
    """

    logger.info("Inside set_difference method")
    difference = np.setdiff1d(array1,array2)
    logger.debug(f" : diffrence is {difference} ")

def main():
    
    logger.info("Inside main method ")
    array1 = np.array([0,10,20,40,60,80])
    array2 = np.array([10,30,40,50,70,90])
    logger.debug(f" given arrays {array1} and {array2}")
    set_differece(array1,array2)


if __name__ == '__main__':
    main()