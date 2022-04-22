//TIme complexity o(n) and space complexity O(h)

treenode* mirrorTree(node* root){
    if (root == NULL)
        return root;
    node* t = root->left;
    root->left = root->right;
    root->right = t;
 
    if (root->left)
        mirrorTree(root->left);
    if (root->right)
        mirrorTree(root->right);
   
  return root;
}


//https://www.geeksforgeeks.org/create-a-mirror-tree-from-the-given-binary-tree/