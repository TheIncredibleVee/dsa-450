
#O(N)
def nextPermutation( arr):
    n = len(arr)
    x = n-1
    while (x > 0 and arr[x] <= arr[x-1]):
        x -= 1
        
    if (x > 0):
        for i in range(n-1, x-1, -1):
            if (arr[x-1] < arr[i]):
                arr[x-1], arr[i] = arr[i], arr[x-1]
                break
                
    rotate(arr, x, n-1)

    
def rotate( arr, low, high):
    if (low == high):
        return 
    
    while (low < high):
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1

#https://leetcode.com/problems/next-permutation/submissions/