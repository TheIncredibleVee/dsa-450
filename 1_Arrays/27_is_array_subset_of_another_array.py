#O(n) time and O(n) space
def isSubset(a1, a2, n, m):
    s=set(a1)
    for i in a2:
        if i not in s:
            return "No"
    return "Yes"


#https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1#
    
