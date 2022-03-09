#O(log(r)+log(c)) time complexity and O(1) space complexity

def searchMatrix(matrix, target):
    rows=len(matrix)
    cols=len(matrix[0])
    low=0
    high=rows-1
    reqrow=-1
    while high>=low:
        mid=(low+high)//2
        if matrix[mid][cols-1]==target:
            return True
        if matrix[mid][cols-1]>target:
            reqrow=mid
            high=mid-1
        else:
            low=mid+1
    low=0
    high=cols-1
    while high>=low:
        mid=(high+low)//2
        if matrix[reqrow][mid]==target:
            return True
        if matrix[reqrow][mid]>target:
            high=mid-1
        else:
            low=mid+1
    return False


#Alternate O(log(n)) time complexity and O(1) space complexity where n is total number of elements in the matrix

def searchMatrix(matrix, target):
    if not matrix or target is None:
        return False

    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1
    
    while low <= high:
        mid = (low + high) / 2
        num = matrix[mid / cols][mid % cols]

        if num == target:
            return True
        elif num < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False



#https://leetcode.com/problems/search-a-2d-matrix/