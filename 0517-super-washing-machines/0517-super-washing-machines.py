class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total_dresses = sum(machines)
        
        if total_dresses % n != 0:
            return -1 # we check if it is even possible to split dresses to all machines equally
        
        target_dresses = total_dresses // n
        moves = 0
        dresses_so_far = 0 # prefix sum
        
        for i in range(n):
            dresses_so_far += machines[i] - target_dresses
            # The maximum value of abs(dresses_so_far) indicates the 
            # maximum number of dresses that needs to be moved in a single move
            moves = max(moves, abs(dresses_so_far), machines[i] - target_dresses)
        
        return moves
        # we take max of this two: dreses_so_far, machines[i] - target_dresses
        #wehre machines[i] - target_dresses is the overload so the waching machine have to give it away
        # and the dreses_so_far is the curent flow on each waching machine it means whethr 
        # we have to move some dress to the left / right (-/+)
        # and we take the maximum val of it                                   