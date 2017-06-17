class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dfs([], set(), n)

    def canPlace(self, curList, mark, j):
        left = right = j
        for inx in range(len(curList) - 1, -1, -1):
            left -=1
            right +=1
            if curList[inx] == left or curList[inx] == right:
                return False
        return True

    def dfs(self, curList, mark, n):
        if n == len(curList):
            return 1

        cnt = 0
        for j in range(n):
            if j not in mark:
                if self.canPlace(curList, mark, j):
                    curList.append(j)
                    mark.add(j)
                    cnt += self.dfs(curList, mark, n)
                    curList.pop()
                    mark.remove(j)
        return cnt
