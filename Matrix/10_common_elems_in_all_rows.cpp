//Time Complexity O(n^2) and Space Complexity O(n)

vector<int> printCommonElements(int mat[M][N]){
    vector<int> res;
    unordered_map<int,int> m;
    for(int i=0;i<M;i++){
        for(int j=0;j<N;++j){
            if(m[mat[i][j]]==i){
                m[mat[i][j]++];
                if(i==M-1 && m[mat[i][j]]==M){
                    res.push_back(mat[i][j]);
                }
            }
        }
    }
    return res;
}

vector<int> printCommonElements(int mat[M][N]){
    vector<int> res;
    unordered_set<int> s1,s2;
    for(int i=0;i<N;++i){
        s1.insert(mat[0][i]);
    }
    for(int i=1;i<M;i++){
        for(int j=0;j<N;++j){
            if(i%2){
                if(s1.find(mat[i][j])!=s1.end()){
                    s2.insert(mat[i][j]);
                }
            }else{
                if(s2.find(mat[i][j])!=s2.end()){
                    s1.insert(mat[i][j]);
                }
            }
        }
        if(i%2){
            s1.clear();
        }else{
            s2.clear();
        }
    }
    for(auto x:s1){
        res.push_back(x);
    }
    for(auto x:s2){
        res.push_back(x);
    }
    return res;

}


//https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/