class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # potrzebuje indeks wystapienia kazdej cyfry pierwszy i ostatni raz
        d = defaultdict(list)
        for i, ch in enumerate(s):
            if ch not in d:
                d[ch].append(i)
            elif len(d[ch]) == 1:
                d[ch].append(i)
            else:
                d[ch][-1] = i
        res = -1
        for st, A in d.items():
            if len(A) == 2:
                res = max(res, A[1] - A[0] - 1)
        return res

                