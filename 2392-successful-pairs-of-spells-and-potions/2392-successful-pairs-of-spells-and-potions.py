class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        spl = [(spells[i], i) for i in range(n)]
        spl.sort()
        potions.sort()
        pairs = [0 for _ in range(n)]

        for spell, i in spl:
            if spell == 0:
                pairs[i] = 0
            
            need = math.ceil(success/spell)
            first_ok = bisect.bisect_left(potions, need)
            pairs[i] = m - first_ok
        return pairs






