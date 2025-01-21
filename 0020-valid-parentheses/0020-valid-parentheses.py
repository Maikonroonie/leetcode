class Solution(object):
    def isValid(self, s):
        T=[0]
        for x in s:
            if x== '(' or x=='[' or x=='{':
                T.append(x)
            elif x==')' and T[-1]=='(' or x==']' and T[-1]=='[' or x=='}' and T[-1]=='{':
                T.pop()
            else:
                return False
        if T[-1]==0:
            return True
        else:
             return False
        
