#https://www.geeksforgeeks.org/a-product-array-puzzle/

# Create two array prefix and suffix of length n, i.e length of the original array, initilize prefix[0] = 1 and suffix[n-1] = 1 and also another array to store the product.
# Traverse the array from second index to end.
# For every index i update prefix[i] as prefix[i] = prefix[i-1] * array[i-1], i.e store the product upto i-1 index from the start of array.
# Traverse the array from second last index to start.
# For every index i update suffix[i] as suffix[i] = suffix[i+1] * array[i+1], i.e store the product upto i+1 index from the end of array
# Traverse the array from start to end.
# For every index i the output will be prefix[i] * suffix[i], the product of the array element except that element.
# C++CJavaPython3C#PHP


# Function to print product array for a given array  
# arr[] of size n  
  
  
def productArray(arr, n):  
  
    # Base case 
    if(n == 1): 
        print(0) 
        return
          
    # Allocate memory for temporary arrays left[] and right[]  
    left = [0]*n  
    right = [0]*n  
  
    # Allocate memory for the product array  
    prod = [0]*n  
  
    # Left most element of left array is always 1  
    left[0] = 1
  
    # Rightmost most element of right array is always 1  
    right[n - 1] = 1
  
    # Construct the left array  
    for i in range(1, n):  
        left[i] = arr[i - 1] * left[i - 1]  

    print("\nThe left array is:") 
    for i in range(n):  
        print(left[i], end =' ')

    # Construct the right array  
    for j in range(n-2, -1, -1):  
        right[j] = arr[j + 1] * right[j + 1]  

    print("\nThe right array is:") 
    for i in range(n):  
        print(right[i], end =' ')
  
    # Construct the product array using  
    # left[] and right[]  
    for i in range(n):  
        prod[i] = left[i] * right[i]  
  
    # print the constructed prod array  
    print("\nThe product array is:")  
    for i in range(n):  
        print(prod[i], end =' ')  
  
  
# Driver code  
arr = [10, 3, 5, 6, 2]  
n = len(arr)  

productArray(arr, n)  
  
# This code is contributed by ankush_953