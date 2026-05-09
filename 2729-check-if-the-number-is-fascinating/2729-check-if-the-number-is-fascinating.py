class Solution:
    def isFascinating(self, n: int) -> bool:
        num = n
        n2 = n * 2
        n3 = n * 3
        st = set()
        while num >= 1:
            dig = num % 10
            if dig == 0:
                return False
            if dig not in st:
                st.add(dig)
            else:
                return False
            num = num//10
        
        while n2 >= 1:
            dig = n2 % 10
            if dig == 0:
                return False
            if dig not in st:
                st.add(dig)
            else:
                return False
            n2 = n2//10
        while n3 >= 1:
            dig = n3 % 10
            if dig == 0:
                return False
            if dig not in st:
                st.add(dig)
            else:
                return False
            n3 = n3//10
        
        return True