class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n=len(tasks)
# wlasciwie maski da sie tu uzyc tylko z tego powodu ze z polecnia wynika ze jesli zaczniemy dane zadanie
# to musimy je zrobic cale w jednej sesji przez co przez maske mozna latwo sledzic postęp, 1 - wykonane 
# zadanie 0 - nie wykonane type shiii


#dp[mask] - minimalna liczba sesji potrzebna do wykonania zadan z maski
# dla maski bit 1 oznacza ze zdanie jest juz wykonane
        total = [0 for _ in range(1<<n)]
        for mask in range(1<<n):
            s=0
            for i in range(n):              #liczymy sumy czasu dla kazdej maski (kazdego podzbioru)
                if mask & (1<<i):
                    s+=tasks[i]
            total[mask] = s

        dp = [inf for _ in range(1<<n)]
        dp[0] = 0 # brak zadan - zero sesji

        for mask in range(1<<n):
            sub = mask # sub to serce tego kodu
            while sub:
                if total[sub] <= sessionTime:
                    dp[mask] = min(dp[mask], dp[mask ^ sub] +1) # zadania w mask ktore nie nalezą do sub, 
                    # +1 bo dodajemy tą sesje ktora wlasnie sie wykonala 

                sub = (sub -1) & mask # przechodzimy po wszystkich podmaskach
# why (sub -1) & mask sub - 1 zmienia najmniej znaczyacy bit 1 na 0, a reszte po prawej ustawia na 1
# ale po tym moga powstac bity ktore nie naleza do mask wiec robimy & mask
    

        return dp[(1<<n) -1]





        