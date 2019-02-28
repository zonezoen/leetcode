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
                    # print(f"{prices[index2]} >> {prices[index]}")
                    result_list.append(prices[index2] - prices[index])
                else:
                    # print(f"{prices[index2]} << {prices[index]}")
                    pass
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


# run121()


# 122. 买卖股票的最佳时机 II
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def my_init(self):
        self.temp_min = 99999
        self.temp_max = 0

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 0:
            return 0
        self.my_init()
        result = []
        flag = 0  # 0 算小的，1 算大的
        for index, price in enumerate(prices):
            print("index: " + str(index))
            if price <= self.temp_min and flag == 0:
                self.temp_min = price
                print("赋值最小值：" + str(price))
            else:
                flag = 1
                print(price)
                print(self.temp_max)
                print('===============')
                if price > self.temp_max:
                    self.temp_max = price
                    if index == len(prices)-1:
                        result.append(self.temp_max - self.temp_min)
                else:

                    result.append(self.temp_max - self.temp_min)
                    flag = 0
                    self.temp_min = price
                    self.temp_max = 0

        print(result)
        return sum(result)


def run122():
    prices = [7, 1, 5, 3, 6, 4]
    prices = [1, 2, 3, 4, 5]
    s = Solution()
    result = s.maxProfit(prices)
    print(result)


# run122()

# 123. 买卖股票的最佳时机 III
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/
class Solution:
    def my_init(self):
        self.temp_min = 99999
        self.temp_max = 0

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 0:
            return 0
        self.my_init()
        result = []
        flag = 0  # 0 算小的，1 算大的
        for index, price in enumerate(prices):
            print("index: " + str(index))
            if price <= self.temp_min and flag == 0:
                self.temp_min = price
                print("赋值最小值：" + str(price))
            else:
                flag = 1
                print(price)
                print(self.temp_max)
                print('===============')
                if price > self.temp_max:
                    self.temp_max = price
                    if index == len(prices)-1:
                        result.append(self.temp_max - self.temp_min)
                else:

                    result.append(self.temp_max - self.temp_min)
                    flag = 0
                    self.temp_min = price
                    self.temp_max = 0

        result = (sorted(result,reverse=True))[0:2]

        print(result)
        return sum(result)
def run123():
    prices = [3,3,5,0,0,3,1,4]
    prices = [1,2,4,2,5,7,2,4,9,0]
    s = Solution()
    result = s.maxProfit(prices)
    print(result)
run123()
'''
对于任意一天考虑四个变量:
fstBuy: 在该天第一次买入股票可获得的最大收益
fstSell: 在该天第一次卖出股票可获得的最大收益
secBuy: 在该天第二次买入股票可获得的最大收益
secSell: 在该天第二次卖出股票可获得的最大收益
分别对四个变量进行相应的更新, 最后secSell就是最大
收益值(secSell >= fstSell)
'''
'''
1 1' 2 2'
8 0  8 0
7 1  7 1
5 3  6 1
'''