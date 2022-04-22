//time complexity O(n) and space complexity O(n)

vector <int> bottomView(Node *root) {
    vector<int> res;
    queue<pair<Node *, int>> q;
    q.push({root,0});
    map<int, int> mp;
    while(!q.empty()){
        auto temp=q.front().first;
        int h=q.front().second;
        q.pop();
        mp[h]=temp->data;
        if(temp->left){
            q.push({temp->left,h-1});
        }
        if(temp->right){
            q.push({temp->right,h+1});
        }
    }
    for(auto x:mp){
        res.push_back(x.second);
    }
    return res;
}

//https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1
//https://www.geeksforgeeks.org/bottom-view-binary-tree/
//https://www.youtube.com/watch?v=fPhgtqKdG5k