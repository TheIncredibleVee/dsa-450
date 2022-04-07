#Time complexity O(nm) and space complexity O(nm)

def editDistance(self, s, t):
    n=len(s)
    m=len(t)
    dp=[]
    for i in range(n+1):
        dp.append([0]*(m+1))
    for i in range(n+1):
        dp[i][0]=i
    for i in range(m+1):
        dp[0][i]=i
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    return dp[n][m]




#https://practice.geeksforgeeks.org/problems/edit-distance3702/1
#https://www.geeksforgeeks.org/edit-distance-dp-5/