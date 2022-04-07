//Time Complexity O(n) and space complexity O(n)

long long int lps(string s) {
	long long int n =s.length();
	long long int i =1;
	long long int res=0;
	long long int dp[n+1]={0};
	while(i<n){
		if(s[i]==s[res]){
			res++;
			dp[i++]=res;
		}
		else if(res==0){
			dp[i++]=0;
		}else{
			res=dp[res-1];
		}
	}
	return dp[n-1];
}   

//Python

// def lps(self, s):
// 	res=0
// 	n=len(s)
// 	dp=[0]*n
// 	i=1
// 	while i<n:
// 		if s[i]==s[res]:
// 			dp[i]=res+1
// 			res+=1
// 			i+=1
// 		elif res==0:
// 			dp[i]=0
// 			res=0
// 			i+=1
// 		else:
// 			res=dp[res-1]
// return dp[n-1]




// Regex SOln
// import re

// s = "ABCABCABCABCABC" # Example input

// print(len(re.findall(r'^(\w*).*\1$',s)[0]))

//https://practice.geeksforgeeks.org/problems/longest-prefix-suffix2527/1
//https://www.geeksforgeeks.org/longest-prefix-also-suffix/
//https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/