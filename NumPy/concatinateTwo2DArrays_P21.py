'''

@Author: Suresh
@Date: 2024-07-26
@Last Modified by: Suresh
@Last Modified: 2024-07-26
@Title : Python program to concatenate two 2-dimensional arrays.

'''

import numpy as np
import os
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)


def concatinate_arrays(array1,array2):
    
    """
    Description: Function to concatenates the two given 2D arrays in to one 2D array
    Parameters:
        array1,array2: these two arrays are taking as a parameters to peforming concatination opreation.
    Returns:
        None:
    """
    
    logger.info(" Inside 'concatinate_arrays' method ")

    array_concate = np.concatenate((array1,array2),axis=0)
    logger.debug(f" Array aftr concatinate \n {array_concate}")

def main():

    logger.info(" Inside main method ")
    array1 = np.array([[0, 1, 3], [5, 7, 9]])
    array2 = np.array([[0, 2, 4], [6, 8, 10]])
    logger.debug(f" {array1}")
    logger.debug(f" {array2}")
    logger.info(" calling 'concatinate_arrays' method ")
    concatinate_arrays(array1,array2)


if __name__ == '__main__':
    main()