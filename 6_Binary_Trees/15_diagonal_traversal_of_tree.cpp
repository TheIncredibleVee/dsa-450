//Time complexity O(n) and space complexity O(n)

vector<int> diagonal(Node *root){
    vector<int> res;
    queue<Node *>q;
    q.push(root);
    while(!q.empty()){
        auto temp=q.front();
        q.pop();
        while(temp){
            res.push_back(temp->data);
            if(temp->left){
                q.push(temp->left);
            }
            temp=temp->right;
        }
    }
    return res;
}


//My approach, will not print in right order as needed.

// vector<int> diagonal(Node *root){
    // vector<int> res;
    // queue<pair<Node *,int>> q;
    // q.push({root,0});
    // map<int, vector<int>> mp;
    // while(!q.empty()){
    //     auto temp=q.front().first;
    //     int h=q.front().second;
    //     q.pop();
    //     mp[h].push_back(temp->data);
    //     if(temp->left){
    //         q.push({temp->left, h+1});
    //     }
    //     if(temp->right){
    //         q.push({temp->right,h });
    //     }
    // }
    // for(auto x: mp){
    //     for(auto i:x.second){
    //         res.push_back(i);
    //     }
    // }
    // return res;
// }

//https://practice.geeksforgeeks.org/problems/diagonal-traversal-of-binary-tree/1/
//https://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/