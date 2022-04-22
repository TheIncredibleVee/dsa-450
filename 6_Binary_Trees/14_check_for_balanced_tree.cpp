//Time complexity O(n) and space complexity O(h)
//Efficient
bool rec(Node * root, int& height){
    if(!root){
        height=0;
        return true;
    }
    int lh,rh;
    bool left= rec(root->left, lh);
    bool right= rec(root->right, rh);
    height= 1+max(lh,rh);
    if(abs(lh-rh)>=2){
        return false;
    }
    return left && right;
}

bool isBalanced(Node *root){
    int h;
    return rec(root, h);
}

//Naive implementation
//Time complexity O(n*n) and space complexity O(h)
// int height(Node* root){
//     if(!root){
//         return 0;
//     }
//     return 1+max(height(root->right), height(root->left));
// }
// //Function to check whether a binary tree is balanced or not.
// bool isBalanced(Node *root)
// {
//     if(!root){
//         return true;
//     }
//     if( abs(height(root->left) - height(root->right) )<=1 && isBalanced(root->left) && isBalanced(root->right) ){
//         return true;
//     }
//     else{
//         return false;
//     }
// }

//https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1
//https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/