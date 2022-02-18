def majorityElement( nums):

    #Method 1: HASHING O(n) space O(n) time

    # dic={}
    # n=len(nums)
    # if n==1:
    #     return nums
    # for i in nums:
    #     if i not in dic:
    #         dic[i]=1
    #     else:
    #         dic[i]+=1
    # res=[]
    # for i in dic.keys():
    #     if dic[i]>(n//3):
    #         res.append(i)
    # return res
    
    #METHOD 2: SORTING O(1) space O(nlogn) time
    #MOORE'S LAW O(1) space O(n) time
    res=[]
    n=len(nums)
    if n==1:
        return nums
    elem1=elem2=0
    cnt1=cnt2=0
    for idx, val in enumerate(nums):
        if elem1==val:
            cnt1+=1
        elif elem2==val:
            cnt2+=1
        elif cnt1==0:
            elem1=val
            cnt1+=1
        elif cnt2==0:
            elem2=val
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1
    cnt1=cnt2=0
    for i in nums:
        if i==elem1:
            cnt1+=1
        elif i==elem2:
            cnt2+=1
    if cnt1>(n//3):
        res.append(elem1)
    if cnt2>(n//3):
        res.append(elem2)
    return res


#https://leetcode.com/problems/majority-element-ii/
#https://leetcode.com/problems/majority-element-ii/discuss/1744145/Moore-Law
#https://leetcode.com/problems/majority-element-ii/discuss/1742851/C%2B%2B-Time-O(n)-Space-O(1)
