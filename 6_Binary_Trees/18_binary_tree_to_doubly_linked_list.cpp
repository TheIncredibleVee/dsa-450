//Time complexity O(n) and space complexity O(1) [INPLACE]

void fixPrevPtr(node *root) 
{ 
    static node *pre = NULL; 

    if (root != NULL) { 
        fixPrevPtr(root->left); 
        root->left = pre; 
        pre = root; 
        fixPrevPtr(root->right); 
    } 
} 

// Changes right pointers to work 
// as next pointers in converted DLL 
node *fixNextPtr(node *root) { 
    node *prev = NULL; 
    // Find the right most node 
    // in BT or last node in DLL 
    while (root && root->right != NULL) 
        root = root->right; 
    // Start from the rightmost node, 
    // traverse back using left pointers. 
    // While traversing, change right pointer of nodes. 
    while (root && root->left != NULL) { 
        prev = root; 
        root = root->left; 
        root->right = prev; 
    }
    // The leftmost node is head 
    // of linked list, return it 
    return (root); 
} 

// The main function that converts 
// BST to DLL and returns head of DLL 
node *BTToDLL(node *root) { 
    // Set the previous pointer 
    fixPrevPtr(root); 
    // Set the next pointer and return head of DLL 
    return fixNextPtr(root); 
} 



//Time complexity O(n) and space complexity O(n)
Node * bToDLL(Node *root){
    Node *DLL;
    Node *temp;
    stack<Node *> st;
    auto node= root;
    while(!st.empty() || node!=NULL){
        if(node){
            st.push(node);
            node=node->left;
        }
        else{
            auto x=st.top();
            st.pop();
            int val=x->data;
            Node *curr_node = new Node;
            curr_node->data=val;
            curr_node->left= NULL;
            curr_node->right= NULL;
            if(!temp){
                DLL=curr_node;
                temp=DLL;
            }else{
                temp->right=curr_node;
                curr_node->left=temp;
                temp=temp->right;
            }
            node=x->right;
        }
    }
    return DLL;
}


//https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1
//https://www.geeksforgeeks.org/in-place-convert-a-given-binary-tree-to-doubly-linked-list/