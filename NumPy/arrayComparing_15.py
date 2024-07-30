'''

@Author: Suresh
@Date: 2024-07-26
@Last Modified by: Suresh
@Last Modified: 2024-07-26
@Title : Python program to compare two arrays using numpy

'''

import numpy as np
import os
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)


def compare_array(array1,array2):
    
    """
    Description: Function to compare two arrays using numpy
    Parameters:
        array1,array2: Function to taking arrays as a paramter for comparision between both the arrays
    Returns:
        None:
    """
    
    logger.info(" Inside 'compare_array' method ")
    greater = array1>array2
    logger.debug(F" a > b : {greater} ")

    lesser = array1<array2
    logger.debug(F" a < b : {lesser} ")

    greater_equl = array1>array2
    logger.debug(F" a >= b : {greater_equl} ")

    lesser_equl = array1>array2
    logger.debug(F" a >= b : {greater_equl} ")

def main():

    logger.info(" Inside main method ")
    array1 = np.array([2,4])
    array2 = np.array([6,3])
    logger.debug(f" : comparision arrays {array1} and {array2} ")

    logger.info(" calling 'compare_array' method ")
    compare_array(array1,array2)



if __name__ == '__main__':
    main()