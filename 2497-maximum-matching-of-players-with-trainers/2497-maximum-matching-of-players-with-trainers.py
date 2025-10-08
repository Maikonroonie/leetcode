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
        