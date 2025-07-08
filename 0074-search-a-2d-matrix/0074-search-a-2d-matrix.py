class Solution(object):
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])

        l, r = 0, m-1
        top, bot = 0, n-1

        while top <= bot:
            mid = (top + bot)//2
            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][m-1] < target:
                top = mid + 1
            else: break #mamy odpowiedni wiersz

        if not (top <= bot):
            return False  # target nie mieści się w żadnym wierszu

        row = (top + bot) // 2

        # Binary search w znalezionym wierszu
        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True

        return False


        