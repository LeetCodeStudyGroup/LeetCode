class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        if n > 0:
            self.dfs(result, [], set(), n)
        return result

    def canPlace(self, curList, mark, j):
        left = right = j
        for inx in range(len(curList) - 1, -1, -1):
            left -=1
            right +=1
            if curList[inx] == left or curList[inx] == right:
                return False
        return True

    def dfs(self, result, curList, mark, n):
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
            if j not in mark:
                if self.canPlace(curList, mark, j):
                    curList.append(j)
                    mark.add(j)
                    self.dfs(result, curList, mark, n)
                    curList.pop()
                    mark.remove(j)
        
