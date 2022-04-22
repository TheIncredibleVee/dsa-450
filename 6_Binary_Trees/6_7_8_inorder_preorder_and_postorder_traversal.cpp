//Time complexity O(n) and space complexity O(h)
//Recursive 

void inorder(Node* root){
    if (root == nullptr) {
        return;
    }
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

void preorder(Node* root){
    if (root == nullptr) {
        return;
    }
    cout << root->data << " ";
    preorder(root->left);
    preorder(root->right);
}

void postorder(Node* root){
    if (root == nullptr) {
        return;
    }
    postorder(root->left);
    postorder(root->right);
}


//Iterative
//Time complexity O(n) and space complexity O(n)

void inorderIterative(Node* root){
    stack<Node*> stack;
    Node* curr = root;
    while (!stack.empty() || curr != nullptr){
        if (curr != nullptr){
            stack.push(curr);
            curr = curr->left;
        }
        else {
            curr = stack.top();
            stack.pop();
            cout << curr->data << " ";
            curr = curr->right;
        }
    }
}

void preorderIterative(Node* root){
    if (root == nullptr)
    return;
    stack<Node*> stack;
    stack.push(root);
    while (!stack.empty()){
        Node* curr = stack.top();
        stack.pop();
        cout << curr->data << " ";
        if (curr->right) {
            stack.push(curr->right);
        }
        if (curr->left) {
            stack.push(curr->left);
        }
    }
}

//Optimized Preorder 
void preorderIterative(Node* root)
{
    if (root == nullptr) {
        return;
    }
 
    stack<Node*> stack;
    stack.push(root);
    Node* curr = root;
    while (!stack.empty())
    {
        if (curr != nullptr){
            cout << curr->data << " ";
 
            if (curr->right) {
                stack.push(curr->right);
            }
 
            curr = curr->left;
        }
        else {
            curr = stack.top();
            stack.pop();
        }
    }
}

void postorderIterative(Node* root){
    if (root == nullptr) {
        return;
    }
    stack<Node*> s;
    s.push(root);
    stack<int> out;
    while (!s.empty()){
        Node* curr = s.top();
        s.pop();
        out.push(curr->data);
        if (curr->left) {
            s.push(curr->left);
        }
 
        if (curr->right) {
            s.push(curr->right);
        }
    }
    while (!out.empty())
    {
        cout << out.top() << " ";
        out.pop();
    }
}

//https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/
//https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/
//https://www.techiedelight.com/postorder-tree-traversal-iterative-recursive/