#Time complexity O(n) space complexity O(n)

from collections import defaultdict
 
def printDups(st):
 
    count = defaultdict(int)
    for i in range(len(st)):
        count[st[i]] += 1
 
    for it in count:
        if (count[it] > 1):
            print(it, ", count = ", count[it])
 

 #https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/