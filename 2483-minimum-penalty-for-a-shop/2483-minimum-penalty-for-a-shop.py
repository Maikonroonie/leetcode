class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix_Y = [ 0 for _ in range(n)]
        if customers[0] == 'Y':
            prefix_Y[0] = 1
        
        for i in range(1, n):
            if customers[i] == 'Y':
                prefix_Y[i] = prefix_Y[i-1] + 1
            else:
                prefix_Y[i] = prefix_Y[i-1]
        print(prefix_Y)
        
        penalty = prefix_Y[n-1]
        day = 0

        for close in range(1, n + 1):
            # - 1 everywher
            Y_before = prefix_Y[close - 1]
            N_before = close - Y_before
            Y_after = prefix_Y[n-1] - prefix_Y[close - 1]
            N_after = n - Y_before - N_before - Y_after
            new_pen = N_before + Y_after
            if new_pen < penalty:
                penalty = new_pen
                day = close
            

            #penalty = min(penalty, N_before + Y_after)
           # print((Y_before,N_before))
            #print((Y_after,N_after))
        
        return day




