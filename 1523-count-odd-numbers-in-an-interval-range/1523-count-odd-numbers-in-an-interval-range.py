class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # chcemy zwrocic liczbe liczb nieparzystych z przedzialu <low, high>
        diff = high - low 
        if low % 2 != 0 or (low % 2 == 0 and high % 2 !=0):
            return diff//2 + 1
        else:
            return diff//2
