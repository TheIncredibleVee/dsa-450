//Time Complexity O(n^2) and space complexity O(n^2)
// If we use substring instead of temp in line around line no. 16, then tc becomes O(n^3)
int wordBreak(string A, vector<string> &B) {
    int n=B.size();
    unordered_set<string> hm(B.begin(), B.end());
    vector<bool> dp(A.length(), false);
    for(int i=0;i<A.length();++i){
        if(hm.find(A.substr(0,i+1))!=hm.end()){
            dp[i]=true;
            continue;
        }
        string temp="";
        temp+=A[i];
        for(int j=i-1;j>=0;j--){
            if(dp[j]){
                if(hm.find(temp)!=hm.end()){
                    dp[i]=true;
                    break;
                }
            }
            temp=A[j]+temp;
        }
    }
    return dp[A.length()-1];
}


//https://practice.geeksforgeeks.org/problems/word-break1352/1
//https://www.geeksforgeeks.org/word-break-problem-dp-32/
//https://www.geeksforgeeks.org/word-break-problem-trie-solution/
//https://www.geeksforgeeks.org/word-break-problem-using-backtracking/ (Variation)