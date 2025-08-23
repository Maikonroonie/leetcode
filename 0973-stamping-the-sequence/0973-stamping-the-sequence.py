class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(target), len(stamp)
        move = 0
        ans = []
        max_move = 10*n
        
        def check(string):
            for i in range(m):
                if string[i] == stamp[i] or string[i] == "?":
                    continue
                else:
                    return False
            return True
        
        while move < max_move:
            prev = move
            for i in range(n-m+1):
                if check(target[i:i+m]):
                    move+=1
                    ans.append(i)
                    target = target[:i] + '?'*m + target[i+m:]
                    if target == '?'*n:
                        return ans[::-1]
            if prev == move:
                return []
        return []
        