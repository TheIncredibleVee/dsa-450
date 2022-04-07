//Time Complexity O(n!*n) and Space Complexity O(n!)
#include<bits/stdc++.h>
using namespace std;

void recUtil(string s, vector<string> &res, string output){
    if(0==s.length()){
        res.push_back(output);
        return;
    }
    for(int i=0;i<s.length();++i){
        recUtil(s.substr(0,i)+s.substr(i+1),res,output+s[i]);
    }
    return;
}

vector<string>find_permutation(string S){
    vector<string> res;
    string output="";
    recUtil(S, res,output);
    sort(res.begin(), res.end());
    return res;
}


//https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1#