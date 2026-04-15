class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack and ast < 0:
                stack.append(ast)
            elif ast > 0:
                stack.append(ast)
            elif stack and ast < 0:
                while stack:
                    x = stack.pop()
                    if x < 0:
                        stack.append(x)
                        stack.append(ast)
                        break
                    elif abs(x) > abs(ast):
                        stack.append(x)
                        break
                    elif x == -ast:
                        break
                    else:
                        if stack:
                            continue
                        else:
                            stack.append(ast)
                            break
        return stack


        