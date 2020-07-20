'''
Input: a List of integers
Returns: a List of integers
'''
from itertools import compress, repeat, chain

def moving_zeroes(arr):
    # Your code here
    a = [0 for i in range(arr.count(0))]
    x = [ i for i in arr if i != 0]
    x.extend(a)
    return(x)

#Test code

#print(moving_zeroes([0,2,3,4,6,7,10]))
#print(moving_zeroes([10,0,11,12,0,14,17]))

#arr = [0,2,3,4,6,7,10]   


#print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")