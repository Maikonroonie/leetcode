class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n=len(price)
        memo = {}

        def dp(needs):
            if tuple(needs) in memo:
                return memo[tuple(needs)]
            
            res = sum(needs[i] * price[i] for i in range(n))

            for offer in special:
                new_needs = []
                valid = True
                for i in range(n): # iterate for each produkt in offer
                    if offer[i] > needs[i]:
                        valid = False
                        break # we cant buy more of somthing we need to buy the exact amount
                    new_needs.append(needs[i] - offer[i])
                
                if valid:
                    res = min(res, offer[-1] + dp(new_needs)) # offer[-1] is the price of an single offer
            
            memo[tuple(needs)] = res
            return res
        return(dp(needs))









