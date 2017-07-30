class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        if n > 0:
            self.dfs(result, [], n)
        return result

    def canPlace(self, curList, j):
        left = right = j
        for inx in range(len(curList) - 1, -1, -1):
            left -=1
            right +=1
            if curList[inx] == left or curList[inx] == right or curList[inx] == j:
                return False
        return True

    def dfs(self, result, curList, n):
        if n == len(curList):
            res = []
            for inx in curList:
                line = ''
                for j in range(n):
                    if j == inx:
                        line += 'Q'
                    else:
                        line += '.'
                res.append(line)
            result.append(res)
            return

        for j in range(n):
            if self.canPlace(curList, j):
                curList.append(j)
                self.dfs(result, curList, n)
                curList.pop()
