'''

@Author: Suresh
@Date: 2024-07-24
@Last Modified by: Suresh
@Last Modified: 2024-07-24 
@Title : Python program to convert a list of numeric value into a one-dimensional
NumPy array.

'''

import numpy as np

import myloggingfile
import os

current_scriptname=os.path.basename(__file__)
logger=myloggingfile.logger_init(current_scriptname)


def one_dimensionalarray(list1):
    
    """
    Description: Function to convert the given list into numpy array using numpy library.
    Parameters:
        list1 : Function taking the list1 as parameter.
    Returns:
        None: 
    """

 
    logger.info("Inside one_dimensionalarray method with argument")
    logger.debug("method taking the parameter as {list1}")

    a=np.array(list1)
    
    logger.debug(f"{a}  it is the numpy array after converting from given list")
    logger.info("one_dimensionalarray completes its task")


def main():

    logger.info("Inside main method")
    list1=[12.23, 13.32, 100, 36.32]

    logger.debug(f"list1 {list1}  is the given list to convert numpy array")
    one_dimensionalarray(list1)
   

if __name__ == '__main__':
    main()