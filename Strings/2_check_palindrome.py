#Time complexity O(n) amd space complexity O(1)

def isPalindrome(self, s):
    if s==s[::-1]:
        return 1
    else:
        return 0


#https://practice.geeksforgeeks.org/problems/palindrome-string0817/1