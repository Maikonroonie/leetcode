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

