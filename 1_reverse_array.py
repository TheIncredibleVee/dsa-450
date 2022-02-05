from sys import stdin

t=int(stdin.readline())
while t>0:
    t-=1
    n=int(stdin.readline())
    arr=list(map(int, stdin.readline().split()))
    for i in arr[::-1]:
        print(i, end=" ")
    print()

#ALternate
def rev(arr,l,r):
    low=l
    high=n-1
    while low<=high:
        arr[low],arr[high]=arr[high],arr[low]
    return arr

#alternate
def rev(arr,l,r):
    arr.reverse()
    return arr


#https://www.geeksforgeeks.org/reverse-array-without-using-subtract-sign-anywhere-code/
#https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
