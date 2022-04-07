//Time Complexity O(n^2) and space complexity O(n)

int count(vector<int>nums, int k,int n,int indx,vector<int> &dp){
    if(n==indx)return 0;
    if(dp[indx]!=-1)return dp[indx];
    
    int a=INT_MAX;
    int sum=-1;
    
    
    for(int i=indx;i<n;i++){
        sum+=nums[i]+1;
        if(sum<=k){
            if(i==n-1) 

            { 
                a=0;
                break;
            }
            int temp=k-sum;
            a=min(a,count(nums,k,n,i+1,dp)+(temp*temp));
        }
        else break;
    }
    return dp[indx]=a;
}

int solveWordWrap(vector<int>nums, int k) {
    vector<int>dp(nums.size(),-1);
    return count(nums,k,nums.size(),0,dp);
} 



//https://practice.geeksforgeeks.org/problems/word-wrap1646/1