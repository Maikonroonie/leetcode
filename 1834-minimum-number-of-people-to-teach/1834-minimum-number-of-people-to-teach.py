class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        #there is n+1 pepple
        to_teach = set()
        for u, v in friendships:
            u-=1
            v-=1
            can_comunicate = False

            for lang in languages[u]:
                if lang in languages[v]:
                    can_comunicate = True
                    break
            if not can_comunicate:
                to_teach.add(u)
                to_teach.add(v)
        
        min_to_teach = len(languages) +1

        for lang in range(1, n+1):
            cnt = 0
            for u in to_teach:
                if lang not in languages[u]:
                    cnt+=1
            min_to_teach = min(min_to_teach, cnt)
        return min_to_teach



