"""
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to
sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
import pytest
from typing import List


class Solution:
    # This solution is getting: `Time Limit Exceeded`
    def max_profit(self, prices: List[int]) -> int:
        profit = 0
        current_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                current_profit = prices[j] - prices[i]
                if current_profit > profit:
                    profit = current_profit

        return profit


    def max_profit_2(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

@pytest.fixture()
def solution():
    return Solution()

@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
    ]
)
def test_max_profit(prices, expected, solution):
    assert solution.max_profit(prices) == expected


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
    ]
)
def test_max_profit_2(prices, expected, solution):
    assert solution.max_profit_2(prices) == expected
