//Time complexity O(n) and space complexity O(n)

vector<int> levelOrder(Node* root)
{
    queue<Node *> st;
    vector<int> res;
    st.push(root);
    while(!st.empty()){
        int top=st.front()->data;
        auto temp=st.front();
        st.pop();
        res.push_back(top);
        if(temp->left){
            st.push(temp->left);
        }
        if(temp->right){
            st.push(temp->right);
        }
    }
    
    return res;
}


// Pyhton Code:

// def levelOrder(self,root ):
//     res=[]
//     q=[]
//     if not root:
//         return res
//     q.append(root)
//     while len(q)>=1:
//         temp=q.pop(0)
//         res.append(temp.data)
//         if temp.left:
//             q.append(temp.left)
//         if temp.right:
//             q.append(temp.right)
//     return res


//https://practice.geeksforgeeks.org/problems/level-order-traversal/1#
//https://www.geeksforgeeks.org/level-order-tree-traversal/
