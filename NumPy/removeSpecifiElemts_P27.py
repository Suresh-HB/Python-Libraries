'''

@Author: Suresh
@Date: 2024-07-
@Last Modified by: Suresh
@Last Modified: 2024-07-
@Title : Python program to remove the specific elements from the given array.

'''


import os
import numpy as np
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)


def remove_element(arr):
    
    """
    Description: Function to remove the specific elements from the given array
    Parameters:
        arr: Function to taking array as a parameter for remvoing elements
    Returns:
        None:
    """
    
    logger.info(" Inside 'remove_element' method ")
    list_indices = [1,4,5]
    arr_delEle = np.delete(arr,list_indices)
    logger.debug(f"Array after deleted \n {arr_delEle}")


def main():

    logger.info(" Inside main method ")
    
    arr = np.array([ 10,20,30,40,50,60,70,80,90,100])
    logger.debug(f" {arr}")
    logger.info(" calling 'remove_element' method ")
    remove_element(arr)


if __name__ == '__main__':
    main()