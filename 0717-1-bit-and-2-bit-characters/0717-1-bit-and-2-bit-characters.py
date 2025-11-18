class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # is last chr one bit character?
        n = len(bits)
        p = 0
        while p < n:
            if bits[p] == 1 and bits[p+1] == 1:
                p += 2
            elif bits[p] == 1 and bits[p+1] == 0:
                p += 2
            elif bits[p] == 0:
                if p == n-1:
                    return True
                else:
                    p += 1
        return False
