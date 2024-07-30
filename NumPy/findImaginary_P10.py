'''

@Author: Suresh
@Date: 2024-07-25
@Last Modified by: Suresh
@Last Modified: 2024-07-25
@Title : Python program to find the real and imaginary parts of an array of complex numbers

'''

import numpy as np
import myloggingfile 
import os

fname = os.path.basename(__file__)
logger = myloggingfile. logger_init(fname)


def main():

    logger.info("Inside main method")
    
    arr_complex = np.array([ 1.00000000+0.j, 0.70710678+0.70710678j])
    logger.debug(f"Original array:{arr_complex}")

    real_part = np.real(arr_complex)
    logger.debug(f"real_part={real_part}")

    imaginary_part = np.imag(arr_complex)
    logger.debug(f"imaginary_part ={imaginary_part}")


if __name__ =='__main__':
    main()



