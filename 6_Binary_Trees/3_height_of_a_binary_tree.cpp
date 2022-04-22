// Time complexity O(n) and space complexity O(n) (stack overhead)

int height(struct Node* node){
    if(!node){
        return 0;
    }
    return max(height(node->left), height(node->right))+1;
}

//https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1#
//https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/
