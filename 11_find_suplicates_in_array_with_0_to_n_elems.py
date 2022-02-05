#O(n) two pointer/cycle detection in linkedlist
def findDuplicate(nums):
    slow=fast=nums[0]
    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]
        if slow==fast:
            break
    slow=nums[0]
    while slow!=fast:
        slow=nums[slow]
        fast=nums[fast]
    return slow

#altenate's
#1. Sort the list
#2. Negative Marking
def negMarking(nums):
    for i in nums:
        elem=abs(i)-1
        nums[elem]=-nums[elem]
        if nums[elem]>0:
            return elem+1
    return -1
#3.Array hashmap
def findDuplicate(nums):
    while nums[0] != nums[nums[0]]:
        nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
    return nums[0]
#4. Binary Search O(nlogn)
#5. Sum of set bits (Not understood)


#https://leetcode.com/problems/find-the-duplicate-number/solution/
