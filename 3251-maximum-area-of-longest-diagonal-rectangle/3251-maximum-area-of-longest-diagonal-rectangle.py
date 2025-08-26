class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        n=len(dimensions)
        max_diag = 0
        area = 0
        for i, (x, y) in enumerate(dimensions):

            diag = sqrt(x*x + y*y)
            if diag > max_diag:
                max_diag = diag
                area = x*y
            elif diag == max_diag:
                if area < x*y:
                    max_diag = diag
                    area = x*y
        return area