#Time complexity O(n) and space complexity O(1)

def stoNum(s):
    res=""
    for x in s:
        if x<'S':
            num=ceil((ord(x)-ord('A'))/3+1)+1
            times=(ord(x)-ord('A'))%3+1
            res+=str(num)*times
        elif x<'Z':
            temp=x-1
            num=ceil((ord(temp)-ord('A')+1)/3)+1
            times=(ord(temp)-ord('A'))%3+1
            res+=str(num)*times
        elif x=='Z':
            res+='9999'
    return res

#ALternate using dict
def printSequence(arr, input):
    n = len(input)
    output = ""
     
    for i in range(n):
     
        if(input[i] == ' '):
            output = output + "0"
        else:
            position = ord(input[i]) - ord('A')
            output = output + arr[position]
    return output
     
str = ["2", "22", "222",
       "3", "33", "333",
       "4", "44", "444",
       "5", "55", "555",
       "6", "66", "666",
       "7", "77", "777", "7777",
       "8", "88", "888",
       "9", "99", "999", "9999" ]


#https://www.geeksforgeeks.org/convert-sentence-equivalent-mobile-numeric-keypad-sequence/
