#Time complexity O(n*2^n) and space complexity O(n)

def printSubsequence(input, output):

    if len(input) == 0:
        print(output, end=' ')
        return
 
    printSubsequence(input[1:], output+input[0])
    printSubsequence(input[1:], output)


#Method 2(IN CPP)

# unordered_set<string> st;
#  void subsequence(string str){
#     for (int i = 0; i < str.length(); i++) {
#         for (int j = str.length(); j > i; j--) {
#             string sub_str = str.substr(i, j);
#             st.insert(sub_str);
 
#             for (int k = 1; k < sub_str.length(); k++) {
#                 string sb = sub_str;
#                 sb.erase(sb.begin() + k);
#                 subsequence(sb);
#             }
#         }
#     }
# }
 




#Method 3

def printSubSeqRec(str, n, index = -1, curr = ""):
    if (index == n):
        return
    if (len(curr) > 0):
        print(curr)

    i = index + 1

    while(i < n):
        curr = curr + str[i]
        printSubSeqRec(str, n, i, curr)
        curr = curr[0:-1]
        i = i + 1
        
def printSubSeq(str):
   printSubSeqRec(str, len(str))
 


#https://www.geeksforgeeks.org/print-subsequences-string/
