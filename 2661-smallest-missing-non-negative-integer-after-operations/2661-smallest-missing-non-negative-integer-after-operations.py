class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # tablia reszt ile mamy reszt danego rodzaju
        cnt = [0] * value
        for a in nums:
            r = a % value
            cnt[r] += 1
        # teraz idziemy po kazdej kolejnej liczbie od zera i 
        #sprawdzamy jej reszte przy dzeieleniu przez value
        # i teraz sprawdzamy czy w cnt mamy jeszcz dostepne dla tej reszty
        # jesli tak to cnt[r] zmiejszamy o jeden i idziemy dalej (x += 1)
        # jak cnt[r] == 0 to znaczy ze musimy juz zwrocic i to jest pierwsza liczba
        # ktorej nie osiagniemy (MEX)
        x = 0
        while True:
            r = x % value
            if cnt[r] == 0:
                return x
            cnt[r] -= 1
            x += 1