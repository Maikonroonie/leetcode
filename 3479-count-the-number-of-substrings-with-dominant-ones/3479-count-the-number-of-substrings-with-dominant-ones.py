# brute force with prefix sum to make it little bit less brute force
'''
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def is_g(ones, zeros):
            return ones >= zeros * zeros

        # prefix[i] = liczba jedynek w s[0..i] (inclusive)
        prefix = [0] * n
        if n > 0:
            prefix[0] = 1 if s[0] == '1' else 0
            for i in range(1, n):
                prefix[i] = prefix[i-1] + (1 if s[i] == '1' else 0)

        for i in range(n):
            for j in range(i, n):
                ones_in_window = prefix[j] - (prefix[i-1] if i > 0 else 0)
                length = j - i + 1
                zeros = length - ones_in_window
                if is_g(ones_in_window, zeros):
                    res += 1

        return res
'''


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pre = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == "0":
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]

        res = 0
        for i in range(1, n + 1):
            cnt0 = 1 if s[i - 1] == "0" else 0
            j = i
            while j > 0 and cnt0 * cnt0 <= n:
                cnt1 = (i - pre[j]) - cnt0
                if cnt0 * cnt0 <= cnt1:
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                j = pre[j]
                cnt0 += 1
        return res
