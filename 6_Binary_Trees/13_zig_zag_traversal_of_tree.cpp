//Time complexity O(n) and space complexity O(n)


vector <int> zigZagTraversal(Node* root){
    vector<int> res;
    queue<Node *> q;
    q.push(root);
    stack<int> st;
    queue<int> qu;
    bool flag=false;
    while(!q.empty()){
        int n=q.size();
        for(int i=0;i<n;++i){
            auto temp=q.front();
            q.pop();
            if(flag){
                st.push(temp->data);
            }
            else{
                qu.push(temp->data);
            }
            if(temp->left){
                q.push(temp->left);
            }
            if(temp->right){
                q.push(temp->right);
            }
        }
        if(flag){
            while(!st.empty()){
                res.push_back(st.top());
                st.pop();
            }
        }else{
            while(!qu.empty()){
                res.push_back(qu.front());
                qu.pop();
            }
        }
        flag=!flag;
    }
    return res;
}

//https://practice.geeksforgeeks.org/problems/zigzag-tree-traversal/1
//https://www.geeksforgeeks.org/zigzag-tree-traversal/