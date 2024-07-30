'''

@Author: Suresh
@Date: 2024-07-26
@Last Modified by: Suresh
@Last Modified: 2024-07-26
@Title : Write a Python program to save a NumPy array to a text file.

'''

import numpy as np
import os
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)


def save_my_array(my_array):
    
    """
    Description: Function to save the array in txt file and run it in cmd.
    Parameters:
        my_array: Function taking array as parameter to save it in txt file.
    Returns:
        None:
    """
    
    logger.info(" Inside 'save_my_array' method ")
    saved_array = np.savetxt("suresh.txt",my_array)
    print_saved_array = np.loadtxt("suresh.txt")
    logger.debug(f"\n{print_saved_array}")


def main():

    logger.info(" Inside main method ")
    my_array = np.array([[20,10],[56,89]])
    logger.debug(f" Array saving into txt file  {my_array} ")
    logger.info(" calling 'save_my_array' method ")
    save_my_array(my_array)


if __name__ == '__main__':
    main()