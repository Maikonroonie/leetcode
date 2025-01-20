class Solution(object):
    def generateMatrix(self, n):
        matrix=[ [0 for _ in range(n)] for _ in range(n)]
        row=0
        col=0
        i=1
        matrix[row][col]=i
        i+=1
        while i<=n*n:
            while col+1<n and matrix[row][col+1]==0:
                col=col+1
                matrix[row][col]=i
                i+=1
            while row+1<n and matrix[row+1][col]==0:
                row+=1
                matrix[row][col]=i
                i+=1
            while col>0 and matrix[row][col-1]==0:
                col-=1
                matrix[row][col]=i
                i+=1
            while row>0 and matrix[row-1][col]==0:
                row-=1
                matrix[row][col]=i
                i+=1
        return matrix

        
