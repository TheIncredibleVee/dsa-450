//O(log(max-min)*r*log(c)) time complexity and O(1) space complexity where time complexity can be simplified to O(32*r*log(c)) as the number has ab upper bound of 32 bits and log of 2^32 will be 32 only.


int median(vector<vector<int>> &matrix, int r, int c){
    long long total=(r*c)+1;
    int mx=INT_MIN;
    int mn=INT_MAX;
    for(long long i=0;i<r;++i){
        mx=max(matrix[i][c-1], mx);
        mn=min(mn, matrix[i][0]);
    }
    long long low=mn;
    long long high= mx;
    while(high>low){
        long long count=0;
        long long to_find=(high+low)/2;
        for(long long i=0;i<r;++i){
            count+=upper_bound(matrix[i].begin(), matrix[i].end(),to_find)-matrix[i].begin();
        }
        if(count<total/2){
            low=to_find+1;
        }
        else{
            high=to_find;
        }
    }
    return low;
}


//https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1
//https://www.geeksforgeeks.org/find-median-row-wise-sorted-matrix/