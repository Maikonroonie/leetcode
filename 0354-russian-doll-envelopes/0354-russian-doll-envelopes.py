class Solution(object):
    def maxEnvelopes(self, envelopes):
        def lis(T): # longest increasing subsequence
            n=len(T)
            ans=[]
            ans.append(T[0])
            for i in range(1,n):
                if T[i]>ans[-1]:
                    ans.append(T[i])
                else:
                    l=0
                    r=len(ans)-1
                    while l<r:
                        mid=(l+r)//2
                        if ans[mid]>=T[i]:
                            r=mid
                        else:
                            l=mid+1
                    ans[l]=T[i]
            return len(ans)
        envelopes.sort( key = lambda x: (x[0], -x[1]))
     #   T=[]
      #  T.append(envelopes[0][1])
       # for i in range(1, len(envelopes)):
        #    if envelopes[i][0]!=envelopes[i-1][0]:
         #       T.append(envelopes[i][1])
        T = [x[1] for x in envelopes]

        return lis(T)            

