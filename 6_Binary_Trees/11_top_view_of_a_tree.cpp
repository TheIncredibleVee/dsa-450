//Time complexity O(n) and space complexity O(n)

vector<int> topView(Node *root){
    
    vector<int> res;
    queue<pair<Node *,int>> q;
    q.push({root,0});
    map<int, int> mp;
    while(!q.empty()){
        auto temp=q.front().first;
        int h=q.front().second;
        q.pop();
        if(mp.find(h)==mp.end()){
            mp[h]=temp->data;
        }
        if(temp->left){
            q.push({temp->left, h-1});
        }
        if(temp->right){
            q.push({temp->right, h+1});
        }
    }
    for(auto x:mp){
        res.push_back(x.second);
    }
    return res;
}

//My approach, but will screw with the order of traversal order
//Push the first elem of level to stack and last to queue


// vector<int> topView(Node *root){
    // stack<int> st;
    // queue<int> qu;
    // queue<Node *> q;
    // q.push(root);
    // bool flag1=true;
    // bool flag2=false;
    // while(!q.empty()){
    //     int n=q.size();
    //     // cout<<"n\t"<<n<<endl;

    //     for(int i=0;i<n;++i){
    //         if(n>1){
    //             flag1=true;
    //             flag2=true;
    //         }
    //         // cout<<"flag1\t"<<flag1<<endl;
    //         // cout<<"flag2\t"<<flag2<<endl;
    //         auto temp= q.front();
    //         q.pop();
    //         if(i==0 && flag1){
    //             st.push(temp->data);
    //         }
    //         if(i==n-1 && flag2){
    //             qu.push(temp->data);
    //         }
    //         if(temp->left){
    //             q.push(temp->left);
    //             flag1=true;
    //         }else{
    //             flag1=false;
    //         }
    //         if(temp->right){
    //             flag2=true;
    //             q.push(temp->right);
    //         }else{
    //             flag2=false;
    //         }
    //     }                                                                                                                                                                                                                                                                       
    // }
    // vector<int> res;
    // while(!st.empty()){
    //     res.push_back(st.top());
    //     st.pop();
    // }
    // while(!qu.empty()){
    //     res.push_back(qu.front());
    //     qu.pop();
    // }
    // return res;
    
// }

//https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1
//https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/