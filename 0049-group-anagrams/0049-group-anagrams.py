class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        d = defaultdict(list)
        for word in strs:
            arr = []
            for ch in word:
                arr.append(ch)
            arr.sort()
            w = "".join(arr)
            d[w].append(word)
        A = []
        for key, val in d.items():
            A.append(val)
        return A