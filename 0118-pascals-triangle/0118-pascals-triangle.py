class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        T=[[1 for i in range(1,i+1)]for i in range(1,numRows +1)]
        for i in range(2,numRows):
            for j in range(1,i):
                T[i][j]=T[i-1][j-1]+T[i-1][j]
        return T


        