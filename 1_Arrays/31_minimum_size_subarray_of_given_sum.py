#o(n ) time and O(1) space 
def minSubArrayLen(target, nums):
    n=len(nums)
    curr_sum=0
    cnt=0
    if sum(nums)<target:
        return 0
    res=1000000000000
    start=0
    for i in range(n):
        curr_sum+=nums[i]
        while curr_sum>=target:
            curr_sum-=nums[start]
            res=min(res,i-start+1)
            start+=1
    return res if res!=1000000000000 else 0



    # while cnt<n and curr_sum<target:
    #     curr_sum+=nums[cnt]
    #     cnt+=1
    # res=cnt
    # start=0
    # end=cnt-1
    # print(start, end, res)
    # for i in range(end+1,n):
    #     curr_sum+=nums[i]
    #     print(start, i, res, curr_sum)
    #     while curr_sum>=target:
    #         curr_sum-=nums[start]
    #         res=min(res,i-start+1)
    #         start+=1
    #         print(start, i, res, curr_sum)
    # while curr_sum>=target:
    #     curr_sum-=nums[start]
    #     res=min(res,n-start)
    #     start+=1
    #





    #Making presum array and then searching target+presum[i] for all i and return the min of the res and dif. in indexes of i and found lowerbound will be ans
    #O(nlogn) time as nos are +ve and binary search is used and O(n) space

    #C++ code:
    #  int minSubArrayLen(int target, vector<int>& nums)
    # {
    #     int n = nums.size();
    #     if (n == 0)
    #         return 0;
    #     int ans = INT_MAX;
    #     vector<int> sums(n + 1, 0);
    #     for (int i = 1; i <= n; i++)
    #         sums[i] = sums[i - 1] + nums[i - 1];
    #     for (int i = 1; i <= n; i++) {
    #         int to_find = target + sums[i - 1];
    #         auto bound = lower_bound(sums.begin(), sums.end(), to_find);
    #         if (bound != sums.end()) {
    #             ans = min(ans, static_cast<int>(bound - (sums.begin() + i - 1)));
    #         }
    #     }
    #     return (ans != INT_MAX) ? ans : 0;
    # }


    #Brute Force: O(n^2) time and O(1) space
    #int minSubArrayLen(int s, vector<int>& nums)
    # {
    #     int n = nums.size();
    #     if (n == 0)
    #         return 0;
    #     int ans = INT_MAX;
    #     vector<int> sums(n);
    #     sums[0] = nums[0];
    #     for (int i = 1; i < n; i++)
    #         sums[i] = sums[i - 1] + nums[i];
    #     for (int i = 0; i < n; i++) {
    #         for (int j = i; j < n; j++) {
    #             int sum = sums[j] - sums[i] + nums[i];
    #             if (sum >= s) {
    #                 ans = min(ans, (j - i + 1));
    #                 break; 
    #             }
    #         }
    #     }
    #     return (ans != INT_MAX) ? ans : 0;
    # }

#https://leetcode.com/problems/minimum-size-subarray-sum/
#https://leetcode.com/problems/minimum-size-subarray-sum/solution/