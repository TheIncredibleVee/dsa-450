#O(n) time and O(n) space
def getPairsCount(arr, n, k):
    dic={}
    res=0
    for i in arr:
        if k-i in dic:
            res+=dic[k-i]
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return res




#Alternate
def getPairsCount(arr, n, k):
    dic={}
    for i in arr:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    res=0
    for i in arr:
        if k>=i and k-i in dic:
            res+=dic[k-i]
            if k-i==i:
                res-=1
    return res//2

#https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1#