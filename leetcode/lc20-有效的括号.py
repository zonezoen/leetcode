class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2 or len(s) % 2 == 1:
            return False

        left = ["(", "{", "["]
        right = [")", "}", "]"]
        if s[0] in right:
            return False
        my_dict = {"(": ")", "{": "}", "[": "]"}
        m_list = []
        for item in s:
            if item in left:
                m_list.append(item)
            if item in right:
                if not m_list:
                    return False
                top_str = m_list.pop()
                if my_dict.get(top_str) == item:
                    continue
                else:
                    m_list.append(top_str)
        return True if len(m_list) == 0 else False


if __name__ == '__main__':
    s = Solution()
    s.isValid("(]")
