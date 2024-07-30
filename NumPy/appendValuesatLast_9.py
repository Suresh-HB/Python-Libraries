'''

@Author: Suresh
@Date: 2024-07-25
@Last Modified by: Suresh
@Last Modified: 2024-07-25
@Title : Python program to append values to the end of an array

'''

import numpy as np
import os
import myloggingfile


fname = os.path.basename(__file__)
logger= myloggingfile.logger_init(fname)


def add_values(array1,list):

    """
    Description: Function to add given values at last to the 1D array
    Parameters:
        array1: Function taking the given array as parameter
        list: Function taking the given values as parameter for adding last to the array
    Returns:
        None:
    """
    
    logger.info(" : Inside 'add_values'ethod")    
    a=np.append(array1,list)
    logger.debug(f" : 1D array after adding values at last {a}")


def main():

    logger.info(" : Inside main method")
    array1= np.array([10,20,30])
    list=[40,50,60]
    logger.debug(f" : {list} given values for append with given 1D array {array1}")
    add_values(array1,list)
 

if __name__ == '__main__':
    main()