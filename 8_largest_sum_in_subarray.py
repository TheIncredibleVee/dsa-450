#O(n)

def maxSubArraySum(arr,N):
    maxend=arr[0]
    res=arr[0]
    for i in range(1,N):
        maxend=max(maxend+arr[i],arr[i])
        res=max(res,maxend)
    return res

#https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
