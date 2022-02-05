#using extra array for maxend. Can also be done in O(1) space. Check 8_largest_sum_in_subarray.py

def maxSubArraySum(self,arr,N):
    maxend=arr[0]
    res=arr[0]
    for i in range(1,N):
        maxend=max(maxend+arr[i],arr[i])
        res=max(res,maxend)
    return res

#https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/