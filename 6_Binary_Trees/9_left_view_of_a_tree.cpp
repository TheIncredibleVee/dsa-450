// Time complexity O(n) and space complexity O(n)
//Iterative Solution

vector<int> leftView(Node *root){
    queue<Node *> q;
    vector<int> res;
    if(!root){
        return res;
    }
    q.push(root);
    while(!q.empty()){
        int n=q.size();
        for(int i=0;i<n;++i){
            if(i==0){
                res.push_back(q.front()->data);
            }
            auto temp=q.front();
            q.pop();
            if(temp->left){
                q.push(temp->left);
            }
            if(temp->right){
                q.push(temp->right);
            }
        }
    }
    return res;
}

//Recursive solution
//Time complexity O(n) and space complexity O(h) 
void leftViewRec(Node *root, vector<int> &res, int level, unordered_set<int> &s){
    if(!root){
        return;
    }
    if(s.find(level)==s.end()){
        res.push_back(root->data);
    }
    s.insert(level);
    leftViewRec(root->left, res, level+1, s);
    leftViewRec(root->right, res, level+1, s);
}

vector<int> leftView(Node *root){
    vector<int> res;
    unordered_set<int> s;
    leftViewRec(root, res, 0, s);
    return res;
}    



//https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1#
//https://www.geeksforgeeks.org/print-left-view-binary-tree/
