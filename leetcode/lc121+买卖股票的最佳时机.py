from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pri = 10 ^ 4
        pre_pri = 10 ^ 4
        max_result = 0
        for index, day_pri in enumerate(prices):
            if index - 1 >= 0:
                min_pri = min(min_pri, prices[index - 1])
            else:
                min_pri = day_pri
            tmp_ret = day_pri - min_pri

            max_result = max(max_result, tmp_ret)
        return max_result
