#O(n)
def minJumps( arr, n):
    if n<=1:
        return 0
    if arr[0]==0:
        return -1
    jumps=1
    maxrange=arr[0]
    steps=arr[0]
    for i in range(1,n-1):
        maxrange=max(maxrange, i+arr[i])
        steps-=1
        if steps==0:
            if i>=maxrange:
                return -1
            jumps+=1
            steps = maxrange - i
    return jumps

#https://www.geeksforgeeks.org/minimum-number-jumps-reach-endset-2on-solution/