'''

@Author: Suresh
@Date: 2024-07-27
@Last Modified by: Suresh
@Last Modified: 2024-07-27
@Title : Python program to how to add an extra column to an numpy array.

'''

import numpy as np
import os
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)


def add_coloum(array):
    
    """
    Description: Function to add extra coloum to the given array 
    Parameters:
        array : Function taking array as a paramter to add extra column to that given array
    Returns:
        None:
    """
    
    logger.info(" Inside 'add_coloum' method ")
    col = np.arange(100,300,100).reshape(2,1)
    print(col)
    ad_col = np.concatenate((array,col),axis=1)
    logger.debug(f" Array after adding column \n {ad_col}  ")


def main():

    logger.info(" Inside main method ")
    array = np.arange(10,70,10).reshape(2,3)
    logger.debug(f" Array Before adding column \n {array}")
    logger.info(" calling 'add_coloum' method ")
    add_coloum(array)


if __name__ == '__main__':
    main()