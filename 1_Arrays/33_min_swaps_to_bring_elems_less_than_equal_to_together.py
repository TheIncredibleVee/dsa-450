#O(n)time and O(1) space

def minSwap (arr, n, k) : 
    res=0
    cnt=0
    for i in arr:
        if i<=k:
            cnt+=1
    for i in range(cnt):
        if arr[i]>k:
            res+=1
    temp=res
    for i in range(cnt,n):
        if arr[i-cnt]>k:
            temp-=1
        if arr[i]>k:
            temp+=1
        res=min(res,temp)
    return res

#https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1#
#https://www.geeksforgeeks.org/minimum-swaps-required-bring-elements-less-equal-k-together/
