# Time complexity O(n^2) and space complexity O(1)


# IN C++

# string longestPalindrome(string str) {
#     int n = str.size();
#     if (n < 2)
#         return str; 
#     int maxLength = 1,start=0;
#     int low, high;
#     for (int i = 0; i < n; i++) {
#         low = i - 1;
#         high = i + 1;
#         while ( high < n && str[high] == str[i])                                 
#             high++;      
#         while ( low >= 0 && str[low] == str[i])                    
#             low--;      
#         while (low >= 0 && high < n && str[low] == str[high]){ 
#             low--;
#             high++;
#         }
#         int length = high - low - 1;
#         if (maxLength < length) {
#             maxLength = length;
#                 start=low+1;
#         }
#     }
#     return str.substr(start,maxLength);
# }

#Method 2 DP: Time complexity O(n^2) and space complexity O(n^2)
def longestPalindrome(S):
    n=len(S)
    dp=[[0 for i in range(n)] for j in range(n)]
    dp[0][0]=1
    res=S[0]
    res_len=1
    for i in range(n):
        dp[i][i]=1
    for i in range(n-1):
        if S[i]==S[i+1]:
            dp[i][i+1]=1
            if res_len<2:
                res_len=2
                res=S[i]+S[i+1]
    start=0
    for k in range(3,n+1):
        for j in range(n-k+1):
            if dp[j+1][j+k-2]==1 and S[j]==S[j+k-1]:
                dp[j][j+k-1]=1
                if k>res_len:
                    res_len=k
                    start=j
    if res_len>2:
        return S[start:start+res_len]
    else:
        return res



#Method 3: Naive 
def longestPalin(self, S):
    res=""
    res_len=0
    for i in range(len(S)):
        temp=S[i:]
        while temp!=temp[::-1]:
            temp=temp[:-1]
        if len(temp)>res_len:
            res_len=len(temp)
            res=temp
    return res


#https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1#
#https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
        

