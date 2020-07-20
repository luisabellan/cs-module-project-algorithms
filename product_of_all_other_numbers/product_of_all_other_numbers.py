'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here

        int a[n] # This is the input
    int products_below[n];
    p=1;
    for(int i = 0 ;i < n ; ++i) {
    products_below[i]=p;
    p*=a[i];
    }

    int products_above[n];
    p=1;
    for(int i=N-1;i>=0;--i) {
    products_above[i]=p;
    p*=a[i];
    }

    int products[n]; // This is the result
    for(int i=0;i<N;++i) {
    products[i]=products_below[i]*products_above[i];
    }
    If you need to be O(1) in space too you can do this (which is less clear IMHO)

    int a[n] // This is the input
    int products[n];

    // Get the products below the current index
    p=1;
    for(int i=0;i<n;++i) {
    products[i]=p;
    p*=a[i];
    }

    // Get the products above the curent index
    p=1;
    for(int i=n-1;i>=0;--i) {
    products[i]*=p;
    p*=a[i];
    }


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
