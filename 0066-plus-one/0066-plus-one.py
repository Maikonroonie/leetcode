class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)
        x=digits[l-1]
        wynik=[0 for i in range(l+1)]
        przes=1
        for i in range(1,l+1):
            a=digits[-i]
            suma=a+przes
            wynik[-i]=suma%10
            przes=suma//10
        if przes>0:
            wynik[0]=przes
        else:
            wynik=wynik[1:]
        return wynik
