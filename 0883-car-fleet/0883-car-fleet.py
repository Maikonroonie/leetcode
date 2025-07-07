class Solution(object):
    def carFleet(self, target, position, speed):
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in pairs:
            time = float(target - pos) / spd
            # jeśli ten samochód dojeżdża później niż ostatni – nowa flota
            if not stack or time > stack[-1]:
                stack.append(time)
                # inaczej – zlewa się z flotą przed nim

        return len(stack)
