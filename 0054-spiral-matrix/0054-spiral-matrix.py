class Solution:
    #T[[j*3+i+1 for i in range(n)] for j in range(m)]
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        mi, ni = 0, 0
        n=len(matrix[0])
        T=[0 for i in range((m*n))]
        licznik, i=0, 1
        a, b=0, 1
        c=m*n
        while licznik<(c):
            if i%4==1:
                while ni<n:
                    T[licznik]=matrix[mi][ni]
                    ni+=1
                    licznik+=1
                ni-=1
                mi+=1
                n-=1
            elif i%4==2:
                while mi<m:
                    T[licznik]=matrix[mi][ni]
                    mi+=1
                    licznik+=1
                mi-=1
                ni-=1
                m-=1
            elif i%4==3:
                while ni>=a:
                    T[licznik]=matrix[mi][ni]
                    licznik+=1
                    ni-=1
                ni+=1
                mi-=1
                a+=1
            elif i%4==0:
                while mi>=b:
                    T[licznik]=matrix[mi][ni]
                    licznik+=1
                    mi-=1
                mi+=1
                ni+=1
                b+=1
            i+=1
        return T
                   



        
