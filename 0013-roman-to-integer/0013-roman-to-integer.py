class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map={
        "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900
        }
        sum=0
        i=len(s)-1
        while i >=0:
            if i>0 and s[i-1:i+1] in roman_map:
                sum+=roman_map[s[i-1:i+1]]
                i-=2
            else:
                sum+=roman_map[s[i]]
                i-=1
        return sum
print(Solution().romanToInt("III"))


