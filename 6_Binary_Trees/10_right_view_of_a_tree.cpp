//Time complexity O(n) and space complexity O(h)
//Recursive
void rightViewRec(Node *root, vector<int> &res, int level, unordered_set<int> &s){
    if(!root){
        return;
    }
    if(s.find(level)==s.end()){
        res.push_back(root->data);
    }
    rightViewRec(root->right, res, level+1, s);
    rightViewRec(root->left, res, level+1, s);
}
vector<int> rightView(Node *root){
    
    vector<int> res;
    unordered_set<int> s;
    rightVeiwRec(root, res, 0, s);
    return res;
}
//Iterative
//Time complexity O(n) and space complexity o(n)
// vector<int> rightView(Node *root){
    // vector<int> res;
    // if(!root){
    //     return res;
    // }
    // queue<Node *> q;
    // q.push(root);
    // while(!q.empty()){
    //     int n=q.size();
    //     for(int i=0;i<n;i++){
    //         auto temp= q.front();
    //         q.pop();
    //         if(i==n-1){
    //             res.push_back(temp->data);
    //         }
    //         if(temp->left){
    //             q.push(temp->left);
    //         }
    //         if(temp->right){
    //             q.push(temp->right);
    //         }
    //     }
    // }
    // return res
// }

//https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1
//https://www.geeksforgeeks.org/print-right-view-binary-tree-2/