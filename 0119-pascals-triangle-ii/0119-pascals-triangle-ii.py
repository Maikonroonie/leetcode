class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        T=[[1 for i in range(1,i+1)]for i in range(1,rowIndex +2)]
        for i in range(2,rowIndex+1):
            for j in range(1,i):
                T[i][j]=T[i-1][j-1]+T[i-1][j]
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        else:
            return T[rowIndex]
       