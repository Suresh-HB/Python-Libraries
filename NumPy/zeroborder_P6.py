'''

@Author: Suresh
@Date: 2024-07-26
@Last Modified by: Suresh
@Last Modified: 2024-07-26
@Title : Python program to put zero border for array.

'''


import numpy as np

def add_border(arr):

    original_shape = arr.shape
    expanded_shape = (original_shape[0] + 2, original_shape[1] + 2)
    bordered_arr = np.zeros(expanded_shape)
    bordered_arr[1:-1, 1:-1] = arr
    
    return bordered_arr

def main():

    original_array = np.array([[1., 1., 1.],
                               [1., 1., 1.],
                               [1., 1., 1.]])
    
    print("Original array:")
    print(original_array)
    
    bordered_array = add_border(original_array)
    
    print("1 on the border and 0 inside in the array:")
    print(bordered_array)

    
if __name__ == "__main__":
    main()

