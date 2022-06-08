# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# 滑动窗口
class Solution:
    # 闭眼盲打
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        my_list = []
        max_length = 0
        for right, val, in enumerate(s):
            if val not in my_list:
                my_list.append(val)
                max_length = max(max_length, len(my_list))
            else:
                while val in my_list:
                    my_list.remove(s[left])
                    left += 1
                my_list.append(val)
        return max_length

    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        current_length = 0
        max_length = 0
        has_item_set = set()
        str_length = len(s)
        for right_index in range(str_length):
            current_length += 1
            # 这个 while 循环是将左边界一直移动到重复字母那里
            # 假设字母 a 是重复的字符，那么 left 就要一直移动
            # 直到把第一个 a 字母从 set 里面去掉。
            while s[right_index] in has_item_set:
                has_item_set.remove(s[left])
                left += 1
                current_length -= 1
            has_item_set.add(s[right_index])
            max_length = max(current_length, max_length)
        return max_length

if __name__ == '__main__':
    s = Solution()
    ret = s.lengthOfLongestSubstring("pwwkew")
    print(ret)
    for i in range(3,5):
        print(i)