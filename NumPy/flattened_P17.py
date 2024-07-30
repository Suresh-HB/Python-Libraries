'''

@Author: Suresh
@Date: 2024-07-
@Last Modified by: Suresh
@Last Modified: 2024-07-
@Title : Python program to converting the given array into flattened array .

'''

import numpy as np
import os
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)


def flattened_array(a):
    
    """
    Description: Function to converting the given array into flattened array
    Parameters:
        a: Function taking array as parameter for converting to flattend array
    Returns:
        None:
    """
    
    logger.info(" Inside '' method ")

    flat_array = a.flatten()
    print(flat_array)

    
def main():

    logger.info(" Inside main method ")
    a= np.array([[10,20,30],[40,50,60]])
    logger.debug(f" given array \n {a} ")
    logger.info(" calling 'flattened_array' method ")
    flattened_array(a)


if __name__ == '__main__':
    main()