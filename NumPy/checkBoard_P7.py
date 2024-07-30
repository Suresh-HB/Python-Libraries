'''

@Author: Suresh
@Date: 2024-07-25
@Last Modified by: Suresh
@Last Modified: 2024-07-25
@Title :  Python program to create a 8x8 matrix and fill it with a checkerboard pattern.

'''

import numpy as np
import os
import myloggingfile

fname = os.path.basename(__file__)
logger = myloggingfile.logger_init(fname)

def  check_board(checkerboard):

    logger.info(f" : Inside 'check_board' method ")
    checkerboard[::2, 1::2] = 1   #col 0 axis
    checkerboard[1::2, ::2] = 1   #col 1 axi
    logger.debug(f" : checkerboard pattern \n {checkerboard}")

def main():
    
    logger.info(f" : Inside main method ")
    checkerboard = np.zeros((8, 8), dtype=int)
    logger.info(f" : calling 'check_board' method")
    check_board(checkerboard)


if __name__ == '__main__':
    main()