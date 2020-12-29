"""
See Below for original Problem:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""

import unittest


class Solution:
    def maxProfit_BruteForce(self, prices: [int]) -> int:

        # vars
        currentMaxProfit: int = 0
        indexOfMax = []  # the buy, sell range
        temp: int = 0

        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                # calculate the max profit of current range
                temp = prices[j] - prices[i]

                # swap max if greater
                if temp > currentMaxProfit:
                    currentMaxProfit = temp
                    indexOfMax = [prices[i], prices[j]]

        print("The max profit is", currentMaxProfit, "via: ", indexOfMax)
        return currentMaxProfit

    '''
    Strategy: i.e [7,1,5,3,6,4] or [7,6,4,3,1]
    - One Pass
    - Predetermine: find the minvalue i.e 1. Find the max value= 7.
    - Loop throug end of prices[]. Use IF and ELSE loop where IF checks if index is lowestBuy price. Else is calcualtion
    - 
    '''

    def maxProfit_OnePass(self, prices: [int]) -> int:

        # vars
        currentMaxProfit: int = 0
        indexOfMax = []  # the buy, sell range
        minBuyPrice = max(prices) # <-- idea: we default the min price as the worse case scenerio before loop

        # iterate through end of prices
        for i in range(0, len(prices)):

            # IF a lower buyprice is found, then swap
            if (prices[i] < minBuyPrice): # <-- We then re-evaluate what's lower buying price
                #swap
                minBuyPrice = prices[i]

            # ELSE IF, 
            elif (prices[i] - minBuyPrice > currentMaxProfit):
                currentMaxProfit = prices[i] - minBuyPrice

        return currentMaxProfit

class Solution_UnitTest(unittest.TestCase):
    def test_01(self):
        result = Solution().maxProfit_OnePass([7, 1, 5, 3, 6, 4])
        self.assertEqual(result,5, "Expected value of 5" )

    def test_02(self):
        result = Solution().maxProfit_OnePass([9,8,4,1,2])
        self.assertEqual(result,1, "Expected value of 1")
        

if __name__ == "__main__":
    #myObj = Solution()
    #print(myObj.maxProfit_OnePass([7, 1, 5, 3, 6, 4]))
    unittest.main()
