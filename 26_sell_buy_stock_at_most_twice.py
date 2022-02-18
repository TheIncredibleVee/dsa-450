#O(n) time and O(1) space
def maxProfit(prices):
    n=len(prices)
    # 
    # Method 1: 1-D DP O(n) time and O(n) space 
    # dp=[0]*n
    # max_so_far=prices[n-1]
    # for i in range(n-2,-1,-1):
    #     if prices[i]>=max_so_far:
    #         max_so_far=prices[i]
    #         dp[i]=dp[i-1]
    #     else:
    #         dp[i]=max(dp[i+1], max_so_far-prices[i])
    # res=max(dp)
    # res_one=0
    # min_so_far=prices[0]
    # for i in range(len(prices)-1):
    #     min_so_far=min(min_so_far, prices[i])
    #     res_one=max(prices[i]-min_so_far,res_one)
    #     res=max(res,res_one+dp[i+1])
    # res=max(res, prices[len(prices)-1]-min_so_far)
    # return res

    #Methods 2: 2-Sate Machine Algo O(n) time and O(1) space
    buy1=-100000000000000
    sell1=0
    buy2=-100000000000000
    sell2=0
    for i in prices:
        buy1=max(buy1, -i)
        sell1=max(sell1,buy1+i)
        buy2=max(buy2, sell1-i)
        sell2=max(sell2, buy2+i)
    return max(sell2,sell1,0)


#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/submissions/
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/149383/Easy-DP-solution-using-state-machine-O(n)-time-complexity-O(1)-space-complexity
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39611/Is-it-Best-Solution-with-O(n)-O(1).
#https://www.youtube.com/watch?v=4wNXkhAky3s