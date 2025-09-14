class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set('aeiou')

        def devowel(s: str) -> str:
            s = s.lower()
            return ''.join('*' if c in vowels else c for c in s)

        # 1) Preprocessing
        exact = set(wordlist)
        lower_first = {}
        devowel_first = {}
        for w in wordlist:
            wl = w.lower()
            dv = devowel(w)
            if wl not in lower_first:
                lower_first[wl] = w
            if dv not in devowel_first:
                devowel_first[dv] = w

        # 2) Odpowiadanie na zapytania
        res = []
        for q in queries:
            if q in exact:
                res.append(q)
            else:
                ql = q.lower()
                if ql in lower_first:
                    res.append(lower_first[ql])
                else:
                    qdv = devowel(q)
                    res.append(devowel_first.get(qdv, ""))
        return res


# brute force
'''
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = {"e", "i", "o", "u", "a", "E", "I", "O", "U", "A"}
        # convertuje wordlist i queyy
        def convert(arr, lst):
            n = len(lst)

            for i in range(n):
                st = lst[i]
                m = len(st)
                if_vow = [False for _ in range(m)]
                for j in range(m):
                    if st[j] in vowels:
                        if_vow[j] = True
                new_st = ""
                for j in range(m):
                    if if_vow[j]:
                        new_st += "*"
                    else:
                        new_st += st[j].lower()
                arr[i].append(new_st)
        
        x=len(wordlist)
        words = [[] for _ in range(x)]
        for i in range(x):
            words[i].append(wordlist[i])
            words[i].append(wordlist[i].lower())
        convert(words, wordlist)
        y = len(queries)
        quers = [[] for _ in range(y)]
        for i in range(y):
            quers[i].append(queries[i])
            quers[i].append(queries[i].lower())
        convert(quers, queries)
        #print(quers)
        #print(words)
        res = ["" for _ in range(y)]
        for i in range(y):
            flag = False
            for warun in range(3):
                if flag == False:
                    for j in range(x):
                        if quers[i][warun] == words[j][warun]:
                            res[i] = words[j][0]
                            flag = True
                            break
        return res
'''






