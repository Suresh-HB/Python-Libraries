'''

@Author: Suresh
@Date: 2024-07-26
@Last Modified by: Suresh
@Last Modified: 2024-07-26
@Title : Python program to convert a NumPy array into Python list structure. 

'''

import numpy as np
import os
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)


def  array_to_list_conversion(my_array):
    
    """
    Description: Function to convert the given array into list.
    Parameters:
        my_array : Function to taking array as a parameter for converting to list
    Returns:
        None:
    """
    
    logger.info(" Inside 'array_to_list_conversion' method ")

    listed_arrayv = my_array.tolist()
    logger.debug(f" Array after converted into list \n {listed_arrayv}  ")


def main():

    logger.info(" Inside main method ")
    my_array = np.array([[0, 1], [2, 3], [4, 5]])
    logger.debug(f" \n {my_array}")
    logger.info(" calling 'array_to_list_conversion' method ")
    array_to_list_conversion(my_array)


if __name__ == '__main__':
    main()