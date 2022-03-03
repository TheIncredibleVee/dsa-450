#O(n)
def rotate( arr, n):
    arr[:]=arr[-1:]+arr[:-1]

#alternate O(n) 
def rot(arr, n):
    x=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=x

#https://www.geeksforgeeks.org/c-program-cyclically-rotate-array-one/