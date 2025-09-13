class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {"a" : 0, "e" : 0, "i": 0, "o" : 0, "u":0}
        other = {}
        for chr in s:
            if chr in vowels:
                vowels[chr]+=1
            elif chr in other:
                other[chr]+=1
            else:
                other[chr] = 1
        
        max_vow = 0
        max_other = 0
        for key, val in vowels.items():
            max_vow = max(max_vow, val)
        for k, v in other.items():
            max_other = max(max_other, v)
        return max_vow + max_other