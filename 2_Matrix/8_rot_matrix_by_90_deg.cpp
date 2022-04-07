//Time complexity O(n^2) and Space complexity O(1)


void rotate90clockwise(int mat[n][n]){
    for(int i=0;i<n;++i){
        for(j=0;j<i;++j){
            swap(mat[i][j], mat[j][i]);
        }
    }
    for(int i=0;i<n;++i){
        for(int j=0;j<n/2;++j){
            swap(mat[i][j], mat[i][n-1-j]);
        }
    }
}

void rotate90clockwise(int mat[n][n]){
    for(int i=0;i<n;++i){
        for(j=n-1;j>=0;j--){
            cout<<mat[j][i];
        }
    }
}

void rotate180clockwise(int mat[n][n]){
    for(int i=0;i<n/2;i++){
        for(int j=i;j<n-1-i;j++){
            int temp=mat[i][j];
            mat[i][j]=mat[n-1-j][i];
            mat[n-1-j][i]=mat[n-1-i][n-1-j];
            mat[n-1-i][n-1-j]=mat[j][n-1-i];
            mat[j][n-1-i]=temp;
        }
    }
}



//https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/