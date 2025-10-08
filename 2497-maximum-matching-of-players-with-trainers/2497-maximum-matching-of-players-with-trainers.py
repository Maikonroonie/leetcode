class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0  #player
        j = 0  #trainer
        m, n = len(players), len(trainers)
        res = 0

        while i < m and j < n:
            if players[i] <= trainers[j]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res

# ta wersja z bisectem jest mlogn ale mogla by byc lepsza gdyby np bylo malo zawodnikow a bardzo duzo trenerow czli male n i duze m to to mogloby byc lepsze
        '''
        import bisect

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res = 0
        lo = 0
        n = len(trainers)
        for p in players:
            idx = bisect.bisect_left(trainers, p, lo, n)
            if idx == n:
                break
            res += 1
            lo = idx + 1
        return res

        '''