#O(n) time and O(n) space
def findLongestConseqSubseq(arr, N):
    mini=min(arr)
    maxi=max(arr)
    s=set(arr)
    i=mini
    res=1
    for val in arr:
        if val-1 not in s:
            temp=val+1
            while temp in s:
                temp+=1
            res=max(res, temp-val)
    return res



#Naive using sorting 
def findLongestConseqSubseq(arr, n):
    
    ans = 0
    count = 0

    arr.sort()

    v = []

    v.append(arr[0])
    for i in range(1, n):
        if (arr[i] != arr[i - 1]):
            v.append(arr[i])

    for i in range(len(v)):

        if (i > 0 and v[i] == v[i - 1] + 1):
            count += 1
        else:
            count = 1
        ans = max(ans, count)
        
    return ans



#https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1