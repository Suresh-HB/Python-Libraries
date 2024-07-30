'''

@Author: Suresh
@Date: 2024-07-25
@Last Modified by: Suresh
@Last Modified: 2024-07-25
@Title : Python program to create a 2d array with 1 on the border and 0 inside.

'''

import numpy as np
import os
import myloggingfile 


filename = os.path.basename(__file__)
logger = myloggingfile.logger_init(filename)

def create_border_array(original_array):

    """
    Description: Function to put the 1 on the border and 0 inside in the array
    Parameters:
        a: Function taking the given array as parameter
    Returns:
        None:
    """

    logger.info(": Inside 'create_border_array' method")

    original_array[1:-1, 1:-1] = 0
    logger.debug(f"\n {original_array}")
    logger.info(": 1 on the border and 0 inside in the array:")


def main():

    logger.info(": Inside main method")
    n = 5
    original_array = np.ones((n, n))
    
    logger.debug(f": Original array \n {original_array}")
    logger.info(f": Create an {n} x {n} array filled with ones")
    
    create_border_array(original_array)


if __name__ == '__main__':
    main()