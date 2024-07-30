'''

@Author: Suresh
@Date: 2024-07-24
@Last Modified by: Suresh
@Last Modified: 2024-07-24 
@Title : Write a Python program to create a null vector of size 10 and update sixth value to 11.

'''

import numpy as np
import myloggingfile
import os

current_scriptname=os.path.basename(__file__)
logger=myloggingfile.logger_init(current_scriptname)


def createNullVector(size,index,update_value):
    
    """
    Description: Function to create null vector with given size and updating the specified index value with specified value.
    Parameters:
        size: Function taking size for null vector creation.
        index: Function taking index for update the exsisting value in given index.
        update_value: Function taking value which is replaced by given value at specified index.
    Returns:
        None: 
    """
    
    logger.info("Inside null vector method")

    null_vector = np.zeros(size)
    logger.debug(f"original vector: {null_vector}")

    null_vector[index]=update_value
    logger.debug(f"Updated null vector: {null_vector}")
    
    logger.info(f"Null vector index {index} is updated to {update_value}")

def main():

    logger.info("Inside main method")
    size = 10
    index = 6
    update_value = 11

    logger.info(" calling createNullVector method")
    createNullVector(size,index,update_value)


if __name__ == '__main__':
    main()