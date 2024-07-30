'''

@Author: Suresh
@Date: 2024-07-24
@Last Modified by: Suresh
@Last Modified: 2024-07-24 
@Title : Python program to reverse an array (first element becomes last).

'''

import numpy as np
import os
import myloggingfile

current_scriptname = os.path.basename(__file__)
logger = myloggingfile.logger_init(current_scriptname)


def reverseFristAndLastElement(a):
    
    """
    Description: Function to reverse the frist and last elment of given array.
    Parameters:
        a: Function taking array as a parameter 
    Returns:
        None: 
    """

    logger.info("Inside 'reverseFristAndLastElement' method")
    logger.debug(f"Original array: {a}")
    a[0],a[-1]=a[-1],a[0]
    logger.debug(f"Array after reversing frist and last element: {a}")
    

def main():

    logger.info("Inside main method")
    a=np.array([50,20,30,40,10])
    logger.info("calling 'reverseFristAndLastElement' method")
    reverseFristAndLastElement(a)
    
    
if __name__ == '__main__':
    main()