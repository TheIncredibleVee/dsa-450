def findMinDiff(A,N,M):
    if M ==1:
        return 0
    A.sort()
    low=0
    high=M-1
    res=A[high]-A[low]
    for i in range(N-M+1):
        res=min(res,A[high+i]-A[low+i])
    return res

#https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1#
#https://www.geeksforgeeks.org/chocolate-distribution-problem/