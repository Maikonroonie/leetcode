class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        while numBottles >= numExchange:
            res += numExchange
            numBottles = numBottles - numExchange + 1 # +1 ta wymieniona
        res += numBottles
        return res