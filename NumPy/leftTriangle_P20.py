'''

@Author: Suresh
@Date: 2024-07-26
@Last Modified by: Suresh
@Last Modified: 2024-07-26
@Title : Python program to create an array which looks like below array.

'''

import numpy as np
import os
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)


def create_method(arry):
    
    """
    Description: Function to create array like which as given
    Parameters:
        :
    Returns:
        None:
    """
    
    logger.info(" Inside 'create_method' method ")
    for i in range(1,5):
        arry[i:,:i]=1
    logger.debug(f" Array is created as per requirement \n {arry}")


def main():

    logger.info(" Inside main method ")

    arry = np.full((4,3),0)
    logger.info("Array created and filled with zeros")
    logger.debug(arry)
    logger.info(" calling 'create_method' method ")
    create_method(arry)


if __name__ == '__main__':
    main()