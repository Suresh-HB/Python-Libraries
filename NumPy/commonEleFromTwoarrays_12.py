'''

@Author: Suresh
@Date: 2024-07-25
@Last Modified by: Suresh
@Last Modified: 2024-07-25
@Title : Python program to find common values between two arrays.

'''

import numpy as np
import os
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)


def find_common_elements(array1,array2):
   
    """
    Description: Function to finding the common array elements from the two given 1D arrays
    Parameters:
        array1: Function taking the given 1D array as parameters 
        array2: Function taking the given 1D array as parameters 
    Returns:
        None:
    """ 

    logger.info(" : Inside 'find_common_element' method")

    com_elements = np.intersect1d(array1,array2)
    logger.debug(f" : {com_elements} these are the common elements from both the arrays")

def main():

    logger.info("Insdie main method")
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([3, 4, 5, 5, 6, 7])

    logger.info(" : Given two original arrays")
    logger.debug(f" : Original Array-1 {array1}")
    logger.debug(f" : Original Array-2 {array2}")

    logger.info(" : Calling 'find_common_element' method")
    find_common_elements(array1,array2)


if __name__ == '__main__':
    main()