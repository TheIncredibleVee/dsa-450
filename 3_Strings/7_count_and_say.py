#Time complexity O(n*len(res(n-1))) and space complexity O(n)

def countAndSay(n):
    dp=[]
    dp.append("1")
    dp.append("11")
    for val in range(2,n):
        temp=dp[-1]
        cnt=0
        curr=0
        res=""
        for i in temp:
            if curr==0:
                curr=i
                cnt=1
                continue
            if curr==i:
                cnt+=1
            else:
                res+=str(cnt)+str(curr)
                curr=i
                cnt=1
        res+=str(cnt)+str(curr)
        dp.append(res)
    return dp[n-1]


#https://leetcode.com/problems/count-and-say/submissions/