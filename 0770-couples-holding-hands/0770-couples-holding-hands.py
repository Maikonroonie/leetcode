class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # we want to have a cycle 0,1,2,3,4,5 ... wherever
        # and return the amount of minimums swaps to achive that
        n=len(row)
        
        d = {person : seat for seat, person in enumerate(row)}
        cnt = 0

        for i in range(0, n, 2):
            x = row[i]
            if x%2==0:
                partner = x + 1
            else:
                partner = x - 1
            
            if row[i+1] != partner:
                seat = d[partner]
                row[i+1], row[seat] = row[seat], row[i+1]
                d[partner] = i+1
                d[row[seat]] = seat
                cnt += 1

        return cnt
        