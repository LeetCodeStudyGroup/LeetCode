class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dfs([], n)

    def canPlace(self, curList, j):
        left = right = j
        for inx in range(len(curList) - 1, -1, -1):
            left -= 1
            right += 1
            if curList[inx] == left or curList[inx] == right or curList[inx] == j:
                return False
        return True

    def dfs(self, curList, n):
        if n == len(curList):
            return 1

        cnt = 0
        for j in range(n):
            if self.canPlace(curList, j):
                curList.append(j)
                cnt += self.dfs(curList, n)
                curList.pop()
        return cnt
