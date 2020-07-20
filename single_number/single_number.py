'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):

    
    # Your code here
   
   
    """
    :type nums: List[int]
    :rtype: int
    """
    
   
    for i in range(1,len(arr)):
        arr[0] ^= arr[i]
    return arr[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]  # output = 9
    

    print(f"The odd-number-out is {single_number(arr)}")