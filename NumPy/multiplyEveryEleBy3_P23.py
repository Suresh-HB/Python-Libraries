'''

@Author: Suresh
@Date: 2024-07-
@Last Modified by: Suresh
@Last Modified: 2024-07-
@Title : a Python program to create an array of (3, 4) shape, multiply every element
value by 3 and display the new array.

'''

import numpy as np
import os
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)


def create_and_multiply_array(original_array):
    
    """
    Description: Function to multiply every element in the array with 3
    Parameters:
       original_array : Function to taking array as aparameter
    Returns:
        None:
    """
    
    logger.info(" Inside 'create_and_multiply_array' method ")
    new_array = original_array * 3
    logger.info("New array elements:")
    logger.debug(f"\n{new_array}")


def main():

    logger.info(" Inside main method ")

    original_array = np.arange(12).reshape(3, 4)
    logger.debug(f" Original array \n{original_array} ")
    logger.info(" calling 'create_and_multiply_array' method ")
    create_and_multiply_array(original_array)


if __name__ == '__main__':
    main()
