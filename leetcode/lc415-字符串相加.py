class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_length = len(num1)
        num2_length = len(num2)
        carry = 0
        max_length = max(num1_length, num2_length)
        ans = ""
        for index in range(max_length):
            if index <= num1_length - 1:
                num1_item = int(num1[num1_length - 1 - index])
            else:
                num1_item = 0
            if index <= num2_length - 1:
                num2_item = int(num2[num2_length - 1 - index])
            else:
                num2_item = 0
            tmp_ret = num1_item + num2_item + carry
            carry = int(tmp_ret / 10)
            tmp_ret = tmp_ret % 10
            ans = str(tmp_ret) + ans
        if carry > 0:
            ans = str(carry) + ans
        return ans


if __name__ == '__main__':

    for index in range(4, 0):
        print(index)
