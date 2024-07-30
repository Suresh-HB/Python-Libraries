'''

@Author: Suresh
@Date: 2024-07-26
@Last Modified by: Suresh
@Last Modified: 2024-07-26
@Title : Python program to find the set exclusive-or of two arrays.

'''

import numpy as np
import os
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)


def set_exclusive(array1,array2):
    
    """
    Description: Function to find the set exclusive-or of two arrays.Set exclusive-or 
    will return the sorted, unique values that are in only one (not both) of the input arrays.

    Parameters: 
        array1: Function taking array1 as a parameter 
        array2: Function taking array2 as a parameter 
    Returns:
        None:
    """

    logger.info(" : Inside 'set_exclusive' method ")

    exclusive = np.setxor1d(array1,array2)
    logger.debug(f" : Exclusive values from array {exclusive}")


def main():

    logger.info(" : Inside main method ")
    array1 = np.array([0,10,20,40,60,80])
    array2 = np.array([10, 30, 40, 50, 70])
    logger.debug(f" given arrays {array1} and {array2}")

    logger.info(" calling 'set_exclusive' method ")
    set_exclusive(array1,array2)


if __name__ == '__main__':
    main()