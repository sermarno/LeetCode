###################
### 121. Best Time to Buy and Sell Stock
### You are given an array prices where prices[i] is
### the price of a given stock on the ith day.
###
### You want to maximize your profit by choosing a single
### day to buy one stock and choosing a different day in
### the future to sell that stock.
###
### Return the maximum profit you can achieve from this
### transaction. If you cannot achieve any profit, return 0.
###################

######################### PROBLEM COVERS #########################
# 


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # e.g. buy on day 1 (price = 7) and sell on day 2
        # (price = 1), profit = -6 (must buy then sell)

        # No dict: index is always available in a loop if 
        # using (enumerate or range)
        # (e.g. for i in range(len(prices)))

        # only care about the lowest price so far, not every one
        # sell after buy - no looking back

        # make min price be inf for placeholder so any price
        # on list will be lower than first iteration
        min_price = float('inf')
        max_profit = 0

        # for each num in price list, if that value is less than the
        # min_price (currently infinity), that value becomes the
        # min_price (e.g. 7 < inf so 7 becomes min_price)
        # prices = [7, 1, 5, 3, 6, 4]
        for price in prices:
            if price < min_price:
                min_price = price
                # 1) min_price = 7
                # 2) min_price = 1 (1 < 7)
            else:
                profit = price - min_price
                # 3) profit = 4 (5 - 1)
                # 4) profit = 2 (3 - 1)
                if profit > max_profit:
                    # 3) 4 > 0
                    max_profit = profit
                    # 3) max_profit = 4
        return max_profit


        


s = Solution()
answer = s.maxProfit([7, 1, 5, 3, 6, 4])
print(answer)