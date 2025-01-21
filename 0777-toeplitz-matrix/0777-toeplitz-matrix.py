class Solution(object):
    def isToeplitzMatrix(self, matrix):
        # m+n-1 diagnals
        diag=collections.defaultdict(set)
        #rows-col
        m=len(matrix)
        n=len(matrix[0])
        for r in range(m):
            for c in range(n):
                x = r - c
                if not diag[x]:
                    diag[x].add(matrix[r][c])
                elif matrix[r][c] in diag[x]:
                    continue
                else: 
                    return False
        return True