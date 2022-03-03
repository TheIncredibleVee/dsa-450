#O(nlogn)
def getMinDiff(arr, n, k):
    arr.sort()
    mini=arr[0]
    maxi=arr[n-1]
    res=maxi-mini
    for i in range(1,n):
        if arr[i]>=k:
            m=min(mini+k,arr[i]-k)
            mx=max(maxi-k,arr[i-1]+k)
            res=min(res,mx-m)
    return res

#https://www.youtube.com/watch?v=o9WG7t6EKZo