def find3Numbers(self,A, n, X):
    # 
    # Method 1: Brute Force O(n^2) time and O(n) space
    # 
    # s= set(A)
    # for i in range(n):
    #     res= X-A[i]
    #     if A[i]>X:
    #         continue
    #     for j in range(n):
    #         if A[i]==A[j]:
    #             continue
    #         if res-A[j] in s and res-A[j]!=A[j] and res-A[j]!=A[i]:
    #             return True
    # return False
    
    #Method 2:  Sorting and then taking 1 elem and then seraching in between i+1 and n-1
    #           O(n^2) time and O(1) space

    A.sort()
    for i in range(n):
        if A[i]>=X:
            break
        rest=X-A[i]
        low=i+1
        high=n-1
        while low<high:
            if rest== A[low]+A[high]:
                return 1
            if rest>A[low]+A[high]:
                low+=1
            else:
                high-=1
    return 0

#https://practice.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1#