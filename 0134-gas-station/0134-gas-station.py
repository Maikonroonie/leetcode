class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        fuel = 0
        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                start = i + 1
                fuel = 0
        return start

        #greddy aproach:
        # jesli w jakims momencie zbiornik paliwa spadnie ponizej zera, to zaden z punktow pomiedzy
        # poprzednim starte do teraz nie moze być punktem startu, wiec idziemy
        # o jeden indeks dalej i dalej robimy to samo
