#O(nlogn) time and O(1) space
def find_median(v):
    v.sort()
    n=len(v)
    return v[n//2] if n %2 else (v[n//2]+v[n//2-1])//2
#https://practice.geeksforgeeks.org/problems/find-the-median0527/1#