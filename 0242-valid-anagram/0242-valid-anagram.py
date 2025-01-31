class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        #n=len(s)
        #T1=[]
        #T2=[]
       # for i in range(n):
          #  T1.append(s[i])
         #   T2.append(t[i])
        #T1.sort()
        #T2.sort()
        #for i in range(n):
          #  if T1[i]!=T2[i]:
         #       return False
        #return True
        return sorted(s) == sorted(t)

