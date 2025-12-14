class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        n = len(corridor)
        all_seats = 0
        for x in corridor:
            if x == 'S':
                all_seats += 1
        if all_seats == 0 or all_seats % 2 == 1:
            return 0
        seat = 0
        res = 1
        plant = 0

        for x in corridor:
            if x == 'S':
                if seat == 2:
                    res = res * (plant + 1) % MOD
                    plant = 0
                    seat = 0
                seat += 1
            else:
                if seat == 2:
                    plant += 1
        return res


