//Time complexity O(n^2) and space complexity O(n)

Node* constructtree(string s, int* start){
    // Assuming there is/are no negative
    // character/characters in the string
    if (s.size() == 0 || *start >= s.size())
        return NULL;
 
    // constructing a number from the continuous digits
    int num = 0;
    while (*start < s.size() && s[*start] != '(' && s[*start] != ')') {
        int num_here = (int)(s[*start] - '0');
        num = num * 10 + num_here;
        *start = *start + 1;
    }
 
    // creating a node from the constructed number from
    // above loop
    struct Node* root = NULL;
    if(num > 0)
        root = new Node(num);
 
    // As soon as we see first right parenthesis from the
    // current node we start to construct the tree in the
    // left
    if (*start < s.size() && s[*start] == '(') {
        *start = *start + 1;
        root->left = constructtree(s, start);
    }
    if (*start < s.size() && s[*start] == ')'){
      *start = *start + 1;
      return root;
    }
    // As soon as we see second right parenthesis from the
    // current node we start to construct the tree in the
    // right
    if (*start < s.size() && s[*start] == '(') {
        *start = *start + 1;
        root->right = constructtree(s, start);
    }
    if (*start < s.size() && s[*start] == ')')
        *start = *start + 1;
    return root;
}



//Alternate implementation

int findIndex(string str, int si, int ei)
{
    if (si > ei)
        return -1;
 
    // Inbuilt stack
    stack<char> s;
 
    for (int i = si; i <= ei; i++) {
 
        // if open parenthesis, push it
        if (str[i] == '(')
            s.push(str[i]);
 
        // if close parenthesis
        else if (str[i] == ')') {
            if (s.top() == '(') {
                s.pop();
 
                // if stack is empty, this is
                // the required index
                if (s.empty())
                    return i;
            }
        }
    }
    // if not found return -1
    return -1;
}
 
// function to construct tree from string
Node* treeFromString(string str, int si, int ei)
{
    // Base case
    if (si > ei)
        return NULL;
 
    // new root
    Node* root = newNode(str[si] - '0');
    int index = -1;
 
    // if next char is '(' find the index of
    // its complement ')'
    if (si + 1 <= ei && str[si + 1] == '(')
        index = findIndex(str, si + 1, ei);
 
    // if index found
    if (index != -1) {
 
        // call for left subtree
        root->left = treeFromString(str, si + 2, index - 1);
 
        // call for right subtree
        root->right = treeFromString(str, index + 2, ei - 1);
    }
    return root;
}

//https://www.geeksforgeeks.org/construct-binary-tree-string-bracket-representation/