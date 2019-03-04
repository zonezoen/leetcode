__auth__ = 'zone'
__date__ = '2019/3/3 下午9:50'


# 36. 有效的数独
# https://leetcode-cn.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board) -> bool:
        my_dict = {}

        for v_index in range(len(board)):
            v = int(v_index / 3)
            my_dict[v_index] = {}
            for h_index in range(len(board[v_index])):
                h = int(h_index / 3)
                sign = '{}{}'.format(v, h)

                if board[v_index][h_index] != '.':
                    key = board[v_index][h_index]
                    my_dict[v_index][key] = my_dict[v_index].get(key, 0) + 1
                    if my_dict[v_index][key] > 1:
                        return False

                    my_dict[sign] = my_dict.get(sign, {})
                    my_dict[sign][key] = my_dict[sign].get(key, 0) + 1
                    if my_dict[sign][key] > 1:
                        return False

                    h_sign = 'h_'+str(h_index)
                    my_dict[h_sign] = my_dict.get(h_sign, {})
                    my_dict[h_sign][key] = my_dict[h_sign].get(key, 0) + 1
                    if my_dict[h_sign][key] > 1:
                        return False
        return True
    # 最右解
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        s = set()
        for i in range(9):
            for j in range(9):
                if not board[i][j].isdigit():
                    continue

                row_tag = '{}({})'.format(i, board[i][j])
                if row_tag in s:
                    return False
                s.add(row_tag)

                col_tag = '({}){}'.format(board[i][j], j)
                if col_tag in s:
                    return False
                s.add(col_tag)

                m, n = (i // 3) * 3, (j // 3) * 3
                blk_tag = '{}({}){}'.format(m, board[i][j], n)
                if blk_tag in s:
                    return False
                s.add(blk_tag)
        return True


def run36():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    s = Solution()
    result = s.isValidSudoku(board)
    print(result)


run36()
