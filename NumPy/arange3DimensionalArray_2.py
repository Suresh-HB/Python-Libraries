'''

@Author: Suresh
@Date: 2024-07-24
@Last Modified by: Suresh
@Last Modified: 2024-07-24 
@Title : Create a 3x3 matrix with values ranging from 2 to 10.

'''

import numpy as np

import myloggingfile
import os
import appendValuesatLast_9

current_scriptname=os.path.basename(__file__)
logger=myloggingfile.logger_init(current_scriptname)



def main():
    
    logger.info("Inside main method")

    range_from=2
    range_upto=10

    x=np.arange(range_from,range_upto+1).reshape(3,3)
    logger.debug(f"{x}")
    logger.info(f"3*3 matrix is created")
    
   

if __name__ == '__main__':
    main()