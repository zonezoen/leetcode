# 124. 二叉树中的最大路径和
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/


# 121. 买卖股票的最佳时机
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    # 很遗憾，用了最差的方法 -- 遍历，超时了
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 0:
            return 0
        result_dict = {}
        result_list = []
        for index in range(len(prices)):
            for index2 in range(index, len(prices)):
                if prices[index2] > prices[index]:
                    print(f"{prices[index2]} >> {prices[index]}")
                    result_list.append(prices[index2] - prices[index])
                else:
                    print(f"{prices[index2]} << {prices[index]}")
        print(result_list)
        result = 0
        if len(result_list) > 0:
            result = max(result_list)
        return result

    """
    解题思路：
    人脑的思维：
        第 i 天的最大收益 = 第 i 天的价格 - 前 i 天的最低价格
        前 i 天的最大收益 = max(前 i-1 天的最大收益，第 i 天的最大收益)
    先统计前 i 天的最低价格，然后再使用上面的公式进行计算。
    """

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_price, min_price = 0, 99999
        for price in prices:
            min_price = min(min_price, price)
            max_price = max(max_price, price - min_price)
        return max_price


def run121():
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    result = s.maxProfit(prices)
    print(result)


run121()
# 122. 买卖股票的最佳时机 II
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/


# 123. 买卖股票的最佳时机 III
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/
