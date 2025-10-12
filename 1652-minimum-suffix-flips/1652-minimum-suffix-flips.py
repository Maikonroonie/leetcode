class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        curr = '0'  # aktualny stan bieżącego bitu
        for c in target:
            if curr != c:
                flips += 1
                # flipujemy całą resztę → zmieniamy curr
                curr = '1' if curr == '0' else '0'
        return flips

#brute n^2 przez flipowanie calosci, a w lepszej wersji trzyammy tylko stan curr 
'''class Solution:
    def minFlips(self, target: str) -> int:
        # flipujemy wszystkie od indesku i do konca
        # robimy greedy idac od poczatku chcemy zeby dany idneks byl dobrze i idziemy
        #dalej interesuje nas greedy solution
        # czyli robimy to co jest dobre w danej chwili
        res = 0
        p=0
        n = len(target)
        s = "0" *n

        while p < n:
            if s[p] != target[p]: #robimy flipa
                res+=1
                flipped = ''.join('1' if c == '0' else '0' for c in s[p:])
                s = s[:p] + flipped
                p+=1
            else:
                p+=1
        return res
        '''



