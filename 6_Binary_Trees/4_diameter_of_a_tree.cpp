//Time complexity O(n) and space complexity O(h)

int diameter(Node* root) {
    int res=0;
    height(root, res);
    return res;
}

int height(Node *root, int &res){
    if (!root){
        return 0;
    }
    int lh=height(root->left,res);
    int rh=height(root->right,res);
    res= max(res, lh+rh+1);
    return max(rh,lh)+1;
}

//Alternate implementation
//Time complexity O(n^2) and space complexity O(h)
int diameter(Node* root) {
    if(!root){
        return 0;
    }    
    int lh=height(root->left);
    int rh=height(root->right);
    int ld=diameter(root->left);
    int rd=diameter(root->right);
    return max({ld,rd,lh+rh+1});
}
int height(Node *root){
    if (!root){
        return 0;
    }
    return max(height(root->left), height(root->right))+1;
}

//https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1#
//https://www.cdn.geeksforgeeks.org/diameter-of-a-binary-tree-in-on-a-new-method/
//https://youtu.be/zUgxaZApKWA?list=PLqM7alHXFySHCXD7r1J0ky9Zg_GBB1dbk
//https://www.geeksforgeeks.org/diameter-of-a-binary-tree/