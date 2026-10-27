class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        cheapest_price=prices[0]
        profit=0

        for i in prices:
            if i<cheapest_price:
                cheapest_price=i
            
            result=i-cheapest_price

            if result>profit:
                profit=result

        return profit



        