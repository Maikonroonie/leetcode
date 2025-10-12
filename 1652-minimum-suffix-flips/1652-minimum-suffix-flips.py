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
