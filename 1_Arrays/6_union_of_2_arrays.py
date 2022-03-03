def doUnion(a,n,b,m):
    s1=set(a)
    s2=set(b)
    return len(s1 | s2)

#alternate
def union(a,n,b,m):
    s=set()
    s.update(a)
    s.update(b)
    return len(s)

#https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/