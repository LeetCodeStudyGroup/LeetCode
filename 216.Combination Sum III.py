class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        stack = []
        for i in range(1, 10):
            for _ in range(len(stack)):
                ary, sum = stack.pop(0)
                if len(ary) == k - 1:
                    if n - sum >= i and n - sum <= 9:
                        ary.append(n - sum)
                        res.append(ary)
                else:
                    new = ary[:]
                    new.append(i)
                    stack.append((ary, sum))
                    stack.append((new, sum + i))
            stack.append(([i], i))
        return res
