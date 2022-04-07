#Time complexity O(n) and space complexity O(n)

def validShuffle(target, s1,s2):
    if len(s1)+len(s2)!=len(target):
        return False
    d1={}
    d2={}
    for i in s1:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    for i in s2:
        if i in d1:
            d1[1]+=1
        else:
            d1[i]=1
    for i in target:
        if i in d2:
            d2[i]+=1
        else:
            d2[i]=1
    return d1==d2


#METHOD 2:Sorting  O(nlogn) time and O(1) space

def validShuffle(target,s1,s2):
    if len(s1)+len(s2)!=len(target):
        return False
    temp=sorted(s1+s1)
    target=sorted(target)
    return target==temp

#https://www.programiz.com/java-programming/examples/check-valid-shuffle-of-strings