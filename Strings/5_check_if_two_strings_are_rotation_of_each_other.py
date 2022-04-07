

#Method 1:
def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
    if size1 != size2:
        return 0
 
    temp = string1 + string1
 
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0

#Method 2:

def check_rotation(s, goal):
 
    if (len(s) != len(goal)):
        return False
 
    q1 = []
    for i in range(len(s)):
        q1.insert(0, s[i])
 
    q2 = []
    for i in range(len(goal)):
        q2.insert(0, goal[i])
 
    k = len(goal)
    while (k > 0):
        ch = q2[0]
        q2.pop(0)
        q2.append(ch)
        if (q2 == q1):
            return True
 
        k -= 1
 
    return False

#Method 3 (C++):

# bool checkString(string &s1, string &s2, int indexFound, int Size)
# {
# 	for(int i=0;i<Size;i++){
# 		if(s1[i]!=s2[(indexFound+i)%Size])return false;
# 	}

# 	return true;
# }

# int main() {
	
# string s1="abcd";
# string s2="cdab";

# if(s1.length()!=s2.length()){
# 	cout<<"s2 is not a rotation on s1"<<endl;
# }
# else{
	
# 	vector<int> indexes; 
# 	int Size = s1.length();
# 	char firstChar = s1[0];
# 	for(int i=0;i<Size;i++){
# 		if(s2[i]==firstChar){
# 			indexes.push_back(i);
# 		}
# 	}
# 	bool isRotation=false;
# 	for(int idx: indexes){
# 		isRotation = checkString( s1, s2, idx, Size);
# 		if(isRotation)
# 			break;
# 	}
# 	if(isRotation)cout<<"s2 is rotation of s1"<<endl;
# 	else cout<<"s2 is not a rotation of s1"<<endl;
# 	}
# 	return 0;
# }



#https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/