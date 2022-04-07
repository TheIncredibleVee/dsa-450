//O(n+m) time complexity and O(1) space complexity



int rowWithMax1s(vector<vector<int> > arr, int n, int m) {
    int res=-1;
    int mx=m-1;
    for(int i=0;i<n;++i){
        if(arr[i][mx]==0){
            continue;
        }
        while(mx>=0 && arr[i][mx]==1){
            mx--;
        }
        if(mx<0){
            return i;
        }
        res=i;
    }
    return res;
}


//https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1
//https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/