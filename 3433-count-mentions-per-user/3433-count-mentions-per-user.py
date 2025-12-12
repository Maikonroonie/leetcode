class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        n = numberOfUsers
        res = [0 for _ in range(n)]
        offline = [None for _ in range(n)]
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        all = 0
        for event in events:
            mes, time, users = event
            if mes == "OFFLINE":
                offline[int(users)] = int(time) + 59
            else:
                if users == "ALL":
                    all+=1
                elif users == "HERE":
                    for i in range(n):
                        if offline[i] == None or int(time) > offline[i]:
                            res[i] += 1
                else: # split
                    ids_list = users.split()  # To da listę: ['id0', 'id1', 'id0']
                    for token in ids_list:
                        id = int(token[2:])
                        res[id] += 1
        
        for i in range(n):
            res[i] += all
        return res