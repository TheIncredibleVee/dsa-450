//Time Complexity O(n) and space complexity O(n)


bool ispar(string x){
    stack<char> st;
    for (auto i:x){
        if(i=='{' || i=='(' || i=='['){
            st.push(i);
        }
        else{
            if(st.empty()){
                return false;
            }
            char top=st.top();
            if((top=='{' && i!='}') || (top=='[' and i!=']') || (top=='(' && i!=')')){
                return false;
            }
            st.pop();
        }
    }
    return st.empty();
}



//https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1
//https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/