class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_list = s.split(" ")
        result = ""
        for i in range(len(s_list) - 1, -1, -1):
            result = result + " " + s_list[i]
        return result
