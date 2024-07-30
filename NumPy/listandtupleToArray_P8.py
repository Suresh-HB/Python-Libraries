'''

@Author: Suresh
@Date: 2024-07-25
@Last Modified by: Suresh
@Last Modified: 2024-07-25
@Title : Python program to convert a list and tuple into arrays.

'''

import numpy as np
import os
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)

def conversion_to_array(lst,tup):

    logger.info(" : Inside 'conversion_to_array' method ")

    arr1=np.array(lst)
    arr2=np.array(tup)
    logger.debug(f" : array after converting from list \n {arr1}")
    logger.debug(f" : array after converting from tuple \n {arr2}")

def main():

    logger.info(" : Inside main method ")
    lst=[1,2,3,4,5,6,7,8]
    tup=([8,4,6],[1,2,3])
    logger.debug(f" : given vlaues in the form of list and tuple \n {lst} \n {tup}")

    logger.info(" : calling 'conversion_to_array method'")
    conversion_to_array(lst,tup)


if __name__ == '__main__':
    main()