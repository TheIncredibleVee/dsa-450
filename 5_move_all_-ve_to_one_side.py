#O(n) 2-3 passes
def segregateElements(arr, n):
        # Your code goes here
        lst=[]
        for i in range(n):
            if arr[i]>=0:
                lst.append(arr[i])
        for i in range(n):
            if arr[i]<0:
                lst.append(arr[i])
        arr[:]=lst


#ALternate: O(n) 1 pass
#Right side postives and left side negatives
def segregateElements(arr, n):
    low=0
    high=n-1
    while low<=high:
        if arr[low]<0:
            low+=1
        elif arr[high]>=0:
            high-=1
        else:
            arr[low],arr[high]=arr[high],arr[low]
            low+=1
            high-=1


#https://www.geeksforgeeks.org/move-ve-elements-end-order-extra-space-allowed/
#https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers/
#https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers-publish/