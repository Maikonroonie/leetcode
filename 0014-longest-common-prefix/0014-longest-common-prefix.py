
class TrieNode:
    __slots__ = ("children", "end")
    def __init__(self):
        self.children = {}       # char -> TrieNode
        self.end = False         # czy kończy się tu słowo

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # 1) Zbuduj trie
        root = TrieNode()
        for s in strs:
            node = root
            for ch in s:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.end = True

        # 2) Zejdź jedyną ścieżką dopóki jest jedno dziecko i nie trafimy na koniec słowa
        res = []
        node = root
        while True:
            if node.end:                # jakiś string kończy się tutaj -> dalej nie ma wspólnego prefiksu
                break
            if len(node.children) != 1: # rozgałęzienie lub brak dzieci -> stop
                break
            (ch, nxt), = node.children.items()  # jedyne dziecko
            res.append(ch)
            node = nxt

        return "".join(res)


#class Solution:
  #  def longestCommonPrefix(self, strs: List[str]) -> str:
        # brute force approach
        '''
        res = ''
        n = len(strs)
        k = inf
        for i in range(n):
            k = min(len(strs[i]), k)
        
        for i in range(k):
            st = strs[0][i]
            for j in range(1, n):
                if strs[j][i] != st:
                    return res
            res += st
        return res
        # poruwnywanie najmniejszego i najwiekszego stringa rozwiazauje ten problem duzo optymalniej
        if not strs:
            return ""
        a = min(strs)
        b = max(strs)
        i = 0
        while i < len(a) and i < len(b) and a[i] == b[i]:
            i += 1
        return a[:i]
        '''
        # najlepsze rozwiazanie jest dzieki triee, drzewa prefiksowego 




