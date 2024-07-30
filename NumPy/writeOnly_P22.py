'''

@Author: Suresh
@Date: 2024-07-26
@Last Modified by: Suresh
@Last Modified: 2024-07-26
@Title : Python program to make an array immutable (read-only).

'''

import numpy as np
import os
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)

import numpy as np
import logging


def make_array_immutable(a):
   
    """
    Description: Function to make a numpy array immutable (read-only).
    Parameters:
        a : The numpy array to make immutable.
    Returns:
        a : The read-only numpy array.
    """

    a.setflags(write=False)
    return a


def main():

    x = np.array([1, 2, 3, 4])
    x = make_array_immutable(x)
    logger.info("Test the array is read-only or not:")
    
    try:
        logger.info("Try to change the value of the first element:")
        x[0] = 99
    except ValueError as e:
        logger.error("Traceback (most recent call last):")
        logger.error("  File \"<stdin>\", line 19, in <module>")
        logger.error("ValueError: assignment destination is read-only")


if __name__ == "__main__":

    main()
    
