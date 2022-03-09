//O(n*n*log(n*n)) time complexity and O(n*n) space complexity


vector<vector<int>> sortedMatrix(int N, vector<vector<int>> Mat) {
    vector<int> temp;
    int n=N;
    for(int i=0;i<n;++i){
        for(int j=0;j<n;++j){
            temp.push_back(Mat[i][j]);
        }
    }
    sort(temp.begin(), temp.end());
    int row=0;
    int col=0;
    for(int i=0;i<n*n;++i){
        Mat[i/n][i%n]=temp[i];
    }
    return Mat;
    
}


//https://practice.geeksforgeeks.org/problems/sorted-matrix2333/1
