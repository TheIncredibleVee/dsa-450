//Time Complexity O(n^2) and Space Complexity O(n^2)

int specificPair(vector<vector<int> > mat, int n){
    int res=INT_MIN;
    vector<vector<int> > temp(n, vector<int>(n));
    temp[n-1][n-1]=mat[n-1][n-1];
    int maxRow=mat[n-1][n-1];
    int maxCol=mat[n-1][n-1];
    for(int i=n-2;i>=0;--i){
        temp[n-1][i]=max(mat[n-1][i], maxRow);
        maxRow=max(maxRow, mat[n-1][i]);
        temp[i][n-1]=max(mat[i][n-1], maxCol);
        maxCol=max(maxCol, mat[i][n-1]);
    }
    for(int i=n-2;i>=0;--i){
        for(int j=n-2;j>=0;j--){
            res=max(res, mat[i][j]-temp[i+1][j+1]);
            temp[i][j]=max({mat[i][j], temp[i+1][j],temp[i][j+1]});       
        }
    }
    return res;
}


//https://www.geeksforgeeks.org/find-a-specific-pair-in-matrix/
