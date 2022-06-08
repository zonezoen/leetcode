from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result_dict = {}
        list_length = len(strs)
        ret_str = ""
        min_item_lenth = 0
        for item in strs:
            min_item_lenth = min(len(item),min_item_lenth)
        for index in range(min_item_lenth):

            for item in strs:
                    result_dict[item[index]] = result_dict.get(item[index], 0) + 1
            if result_dict.get(item[index], 0) < list_length:
                break
            if result_dict.get(item[index], 0) == list_length:
                ret_str = ret_str + item[index]

        return ret_str
