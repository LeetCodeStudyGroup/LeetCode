class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        [1, 1, 2, 5, 3 + 2 + 2]
        num_list = [1, 1]
        for i in range(2, n + 1):
            cnt = 0
            for j in range(0, i):
                cnt += num_list[j] * num_list[i - j - 1]
            num_list.append(cnt)
        return num_list[-1]

    def numTrees2(self, n):
        cnt = 0
        for i in range(n):
            cnt += self.count_tree(0, i - 1, i + 1, n - 1)
        return cnt

    def count_tree(self, lstart, lend, rstart, rend):
        if (lend - lstart) <= 0 and (rend - rstart) <= 0:
            return 1
        else:
            lcnt = rcnt = 0
            for i in range(lstart, lend + 1):
                lcnt += self.count_tree(lstart, i - 1, i + 1, lend)
            for i in range(rstart, rend + 1):
                rcnt += self.count_tree(rstart, i - 1, i + 1, rend)
            if lcnt == 0:
                lcnt = 1
            if rcnt == 0:
                rcnt = 1
            return lcnt * rcnt
