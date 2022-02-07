def maxProfit( prices):
    res=0
    mi=float('inf')
    for idx, val in enumerate(prices):
        mi=min(prices[idx],mi)
        res= max(res,prices[idx]-mi)
    return res

#alternate
def maxProfit( prices):
    n=len(prices)
    leaders=[0]*n
    i=n-2
    leaders[n-1]=prices[n-1]
    while i>=0:
        if prices[i]>leaders[i+1]:
            leaders[i]=prices[i]
        else:
            leaders[i]=leaders[i+1]
        i-=1
    res=0
    for idx, val in enumerate(prices):
        if val<leaders[idx]:
            res=max(res, leaders[idx]-val)
    return res


#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/