#Time complexity O(n) and space complexity O(1)

def maxSubStr(str, n):
    res=-1
    sum=0
    for i in str:
        if i=='0':
            sum-=1
        else:
            sum+=1
        if sum==0:
            res+=1
    if sum==0:
        return res
    else:
        return -1



#https://www.geeksforgeeks.org/split-the-binary-string-into-substrings-with-equal-number-of-0s-and-1s/