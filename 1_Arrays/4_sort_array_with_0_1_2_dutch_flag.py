#O(n)
def sortt(arr,n):
    low=0
    mid=0
    high=n-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
        
#alternate O(n) 6 pass

def sort012(arr,n):
    # code here
    zero=0
    one=0
    two=0
    for i in arr:
        if i==0:
            zero+=1
        elif i==1:
            one+=1
        else:
            two+=1
    i=0
    while zero>0:
        arr[i]=0
        i+=1
        zero-=1
    while one>0:
        arr[i]=1
        one-=1
        i+=1
    while two>0:
        arr[i]=2
        two-=1
        i+=1
#https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/