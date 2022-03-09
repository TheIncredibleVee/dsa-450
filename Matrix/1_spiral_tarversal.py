# O(n*m) time complexity and O(1) space complexity

def spirallyTraverse(self,matrix, r, c): 
    # code here 
    startRow=0
    endRow=r-1
    startCol=0
    endCol=c-1
    res=[]
    while startRow<=endRow and startCol<=endCol:
        for i in  range(startCol, endCol+1):
            res.append(matrix[startRow][i])
        startRow+=1
        for i in range(startRow, endRow+1):
            res.append(matrix[i][endCol])
        endCol-=1
        if endRow>=startRow:
            for i in range(endCol, startCol-1,-1):
                res.append(matrix[endRow][i])
            endRow-=1
        if endCol>=startCol:
            for i in range(endRow, startRow-1,-1):
                res.append(matrix[i][startCol])
            startCol+=1
    return res

#https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1