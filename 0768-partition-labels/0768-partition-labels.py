#moje rozwiazanie lekko przekombinowane ale w zasadzie z grubsza to samo co we flagowym rozwiazaniu
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res=[]
        cur_cnt=0
        n=len(s)
        d = defaultdict(int) # domyslnie ustawia zero wszedzie
        seen = set()
        score = 0
        for i in s:
            d[i]+=1
       # print(d)
        for st in s:
            if st not in seen:
                score+=d[st]
                seen.add(st)
            

            d[st] -= 1
            score-=1
            cur_cnt+=1
        
            if score == 0:
                seen = set()
                res.append(cur_cnt)
                cur_cnt=0

        return res
#flagowe rozwiazanie
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res'''
