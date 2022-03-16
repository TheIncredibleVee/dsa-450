//Time Complexity: O(log(max-min)*n*logn) and space complexity O(1)

int kthSmallest(int mat[MAX][MAX], int n, int k)
{
    
    int low=mat[0][0];
    int high=mat[n-1][n-1];
    while(high>low){
        int mid=(high+low)/2;
        int count=0;
        //cout<<low<<"\t"<<high<<"\t"<<mid<<endl;
        for(int i=0;i<n;++i){
            if(mat[i][n-1]<=mid){
                count+=n;
                continue;
            }
            if (mat[i][0]>mid){
                break;
            }
            count+=upper_bound(mat[i],mat[i]+n, mid)-mat[i];
        }
        if(count>=k){
            high=mid;
        }
        else{
            low=mid+1;
        }
    }
    return low;
    
}

//Alternate using heap 
//Time Complexity O(n+k*logn) and space complexity O(n)
//Note in case of k<n, we can set make min heap of k size and we just need kth rows and kth col pop k elemnts to get the result. Time complxitiy is O(k+klogk). We can also sort the first col and return 

int kthSmallest(int mat[MAX][MAX], int n, int k){
    auto cmp = [&](pair<int,int> a, pair<int,int> b){
        return mat[a.first][a.second]>mat[b.first][b.second];
    }
    priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(cmp)> pq(cmp);    
    for(int i=0;i<n;++i){
        pq.push({i,0});
    }
    for(int i=1;i<k;++i){
        auto curr=pq.top();
        pq.pop();
        if(curr.second+1<n){
            pq.push({curr.first,curr.second+1});
        }
    }
    return mat[pq.top().first][pq.top().second];
}
//Other Method: Use heap of k size and pop and push for k+1 to n*n elems and return heap's top()
//Store matrix in array and sort it and return kth element


//https://practice.geeksforgeeks.org/problems/kth-element-in-matrix/1#
//https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array-set-1/