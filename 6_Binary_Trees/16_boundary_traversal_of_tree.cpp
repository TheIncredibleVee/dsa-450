//Time complexity O(n) and space complexity O(n)

void inorder(Node *root, vector<int>& res){
        if(!root){
            return;
        }
        inorder(root->left,res);
        if(!root->left && !root->right){
            res.push_back(root->data);
            return;
        }
        inorder(root->right, res);
    }

    vector <int> boundary(Node *root){
        vector<int> res;
        res.push_back(root->data);
        if(!root->left && !root->right){
            return res;
        }
        auto temp=root->left;
        while(temp && (temp->left || temp->right)){
            res.push_back(temp->data);
            if(temp->left){
                temp=temp->left;
            }
            else{
                temp=temp->right;
            }
        }

        //level order leaf tarversal, but will screw the order
        // queue<pair<Node *,int>> q;
        // q.push({root,0});
        // map<int, vector<int>> mp;
        // while(!q.empty()){
        //     auto x=q.front().first;
        //     int h=q.front().second;
        //     q.pop();
        //     if(!x->left && !x->right){
        //         mp[h].push_back(x->data);
        //     }
        //     if(x->left){
        //         q.push({x->left,h-1});
        //     }
        //     if(x->right){
        //         q.push({x->right,h+1});
        //     }
        // }
        // for(auto x:mp){
        //     for(auto i:x.second){
        //         res.push_back(i);
        //     }
        // }
        vector<int> leaf;
        inorder(root, leaf);
        for(auto x:leaf){
            res.push_back(x);
        }
        auto temp2=root->right;
        stack<int> st;
        while(temp2 && (temp2->left || temp2->right)){
            st.push(temp2->data);
            if(temp2->right)
            {
                temp2=temp2->right;
            }
            else{
                temp2=temp2->left;
            }
        }
        while(!st.empty()){
            res.push_back(st.top());
            st.pop();
        }
        return res;
        
    }


//https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1
//https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/