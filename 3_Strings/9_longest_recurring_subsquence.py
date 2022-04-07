#Time complexity O(n^2) and space complexity O(n)

def LongestRepeatingSubsequence( str):
    n=len(str)
    curr=[0]*(n+1)
    prev=[0]*(n+1)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i!=j and str[i-1]==str[j-1]:
                curr[j]=1+prev[j-1]
            else:
                curr[j]=max(curr[j-1],prev[j])
        prev,curr=curr,prev
    return prev[n]


#https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1
#https://www.geeksforgeeks.org/longest-repeating-subsequence/
#https://www.cdn.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/