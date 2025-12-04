class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        res = 0
        
        for car in directions:
            if car == 'R':
                stack.append(car)
            elif car == 'S':
                # If there are cars moving Right in the stack, they all crash into this 'S'
                while stack and stack[-1] == 'R':
                    res += 1
                    stack.pop()
                stack.append('S')
            elif car == 'L':
                if stack and stack[-1] == 'R':
                    # L hits R. 2 collisions. Both become S.
                    res += 2
                    stack.pop()
                    # Now the current car is effectively 'S'. 
                    # Check if previous R's crash into this new 'S' pile.
                    while stack and stack[-1] == 'R':
                        res += 1
                        stack.pop()
                    stack.append('S') # The resulting pile is stationary
                elif stack and stack[-1] == 'S':
                    # L hits S. 1 collision. L becomes S.
                    res += 1
                    stack.append('S')
                else:
                    # L moves left into open space (empty stack or prev is L)
                    stack.append('L')
                    
        return res