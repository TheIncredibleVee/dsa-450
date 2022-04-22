//Time Complexity O(n) and space complexity O(n)

vector<int> reverseLevelOrder(Node *root){
    vector<int> res;
    vector<vector<int>> subres;
    queue<Node *> q;
    if(!root){
        return res;
    }
    q.push(root);
    while(!q.empty()){
        vector<int> temp;
        int n=q.size();
        for(int i =0;i<n;++i){
            auto tp=q.front();
            q.pop();
            temp.push_back(tp->data);
            if(tp->left){
                q.push(tp->left);
            }
            if(tp->right){
                q.push(tp->right);
            }
        }
        subres.push_back(temp);
    }
    for(int i =subres.size()-1;i>=0;i--){
        for(auto x:subres[i]){
            res.push_back(x);
        }
    }
    return res;
}


//https://practice.geeksforgeeks.org/problems/reverse-level-order-traversal/1
//https://www.geeksforgeeks.org/reverse-level-order-traversal/