#O(n) time and O(1) space 
def merge(arr):
    i=0
    j=len(arr)-1
    res=0
    while j>=i:
        if arr[i]==arr[j]:
            j-=1
            i+=1
        elif arr[i]>arr[j]:
            res+=1
            arr[j-1]+=arr[j]
            j-=1
        else:
            res+=1
            arr[i+1]+=arr[i]
            i+=1
    return res;

#https://app.glider.ai/practice/problem/basic-programming/make-array-palindrome/problem
#https://www.geeksforgeeks.org/find-minimum-number-of-merge-operations-to-make-an-array-palindrome/
