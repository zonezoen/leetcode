# 解法在《代码随想录》PDF看到的

from typing import List, Optional

class Solution:


    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        start_index = 1
        self.backtracing(n,k,path,start_index,result)
        return result

    def backtracing(self, n, k, path: List,start_index,result):
        if len(path) == k:
            print("run here")
            print(path)
            result.append(path[:])
            return
        for num in range(start_index,n+1):
            path.append(num)
            print(path)
            self.backtracing(n, k, path,num+1,result)
            path.pop()