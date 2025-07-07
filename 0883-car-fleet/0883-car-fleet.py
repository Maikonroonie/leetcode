class Solution(object):
    def carFleet(self, target, position, speed):
        stack=[]
        n=len(position)
        pos_speed = [ (0, 0) for _ in range(n)]

        for i in range(n):
            pos_speed[i] = (position[i], speed[i])
        
        pos_speed.sort(key = lambda x: x[0], reverse = True)

        # time to target = (target - position)/speed
        for pos, speed in pos_speed:
            time = float(target - pos)/speed
            if not stack or time > stack[-1]: # nowa flota
                stack.append(time)
                
        return len(stack)


