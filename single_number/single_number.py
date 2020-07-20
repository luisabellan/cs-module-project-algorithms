'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr = [-1]):
    # Your code here
    odd_one_out = 0
   
    sorted_arr = sorted(arr)
    print(str(sorted_arr))

    for i in range(sorted_arr):
        if not sorted_arr[i] == sorted_arr[i+1]:
            odd_one_out = sorted_arr[i]

            return  odd_one_out
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]  # output = 9
    

    print(f"The odd-number-out is {single_number(arr)}")