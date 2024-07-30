'''

@Author: Suresh
@Date: 2024-07-25
@Last Modified by: Suresh
@Last Modified: 2024-07-25
@Title : Python program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements

'''


import numpy as np
import os 
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)



def main():

    logger.info(" : Inside main method")

    array = np.array([1, 2, 3], dtype=np.int64)
    size_of_array = array.size
    logger.debug(f" : size of the array is : {size_of_array}")

    size_of_one_element = array.itemsize
    logger.debug(f" : size of the each array element is : {size_of_one_element}")

    total_bytes_consumed = size_of_array * size_of_one_element
    logger.debug(f" : Total size of the array is : {total_bytes_consumed}")
    

if __name__ == '__main__':
    main()