#O(min(logn,logm)) time complexity and O(1) space complexity
def median(arr1,n,arr2,m):
    if n>m:
        arr1, arr2=arr2,arr1
        n,m=m,n
    low=0
    high=n-1
    while high>=low:
        mid=(high+low)//2
        leftA = arr1[mid-1] if mid>0 else float('-inf')
        leftB = arr2[(n+m+1)//2-mid] if (n+m+1)//2-mid>0 else float('-inf')
        rightA=arr1[mid] if mid<n else float('inf')
        rightB=arr2[(n+m+1)//2-mid] if (n+m+1)//2-mid < m else float('inf')

        if leftA<=rightB and leftB<=rightA:
            if (n+m+1)//2:
                return max(leftA,leftB)
            else:  
                return (max(leftA,leftB)+min(rightA,rightB))/2
        elif leftA>rightB:
            high=mid-1
        else:
            low=mid+1
    
    return -1

#O(n+m) Time Complexity and O(1) Space Complexity
# def getMedian(ar1, ar2, n, m) :
 
#     i = 0 # Current index of input array ar1[]
#     j = 0 # Current index of input array ar2[]
#     m1, m2 = -1, -1
#     if((m + n) % 2 == 1) :   
#         for count in range(((n + m) // 2) + 1) :       
#             if(i != n and j != m) :           
#                 if ar1[i] > ar2[j] :
#                     m1 = ar2[j]
#                     j += 1
#                 else :
#                     m1 = ar1[i]
#                     i += 1           
#             elif(i < n) :           
#                 m1 = ar1[i]
#                 i += 1
          
#             # for case when j<m,
#             else :           
#                 m1 = ar2[j]
#                 j += 1       
#         return m1
#     else :
#         for count in range(((n + m) // 2) + 1) :        
#             m2 = m1
#             if(i != n and j != m) :       
#                 if ar1[i] > ar2[j] :
#                     m1 = ar2[j]
#                     j += 1
#                 else :
#                     m1 = ar1[i]
#                     i += 1           
#             elif(i < n) :           
#                 m1 = ar1[i]
#                 i += 1
             
#             else :           
#                 m1 = ar2[j]
#                 j += 1       
#         return (m1 + m2)//2



#https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/