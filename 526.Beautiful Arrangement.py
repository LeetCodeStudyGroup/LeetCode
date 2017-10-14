class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return self.helper({}, N, 0, 1)

    def helper(self, cache, N, used, num):
        if num == N + 1:
            return 1

        key = (num, used)
        if key in cache:
            return cache[key]

        cache[key] = 0
        for i in range(N):
            if used & (1 << i) == 0 and (num % (i + 1) == 0 or (i + 1) % num == 0):
                cache[key] += self.helper(cache, N, used | (1 << i), num + 1)
        return cache[key]
