class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        heap, index, dp = [(0, 0)], [1] * len(primes), [1]
        for i in range(len(primes)):
            heap.append((primes[i], i))
        for i in range(1, n):
            val, factor = heap[1]
            while val == dp[i - 1]:
                self.update(heap, primes, index, dp, factor)
                val, factor = heap[1]
            dp.append(val)
        return dp[-1]

    def update(self, heap, primes, index, dp, i):
        heap[1] = primes[i] * dp[index[i]], i
        index[i] += 1
        self.heapify(heap, 1)

    def heapify(self, heap, root):
        left, right = root * 2, root * 2 + 1
        inx = root
        if left < len(heap) and heap[inx][0] > heap[left][0]:
            inx = left
        if right < len(heap) and heap[inx][0] > heap[right][0]:
            inx = right
        if inx != root:
            heap[root], heap[inx] = heap[inx], heap[root]
            self.heapify(heap, inx)

    def nthSuperUglyNumber2(self, n, primes):
        cnts = [0] * len(primes)
        result = [1]
        for i in range(n - 1):
            vals = [primes[x] * result[cnts[x]] for x in range(len(primes))]
            inx = 0
            for j in range(1, len(primes)):
                if vals[inx] > vals[j]:
                    inx = j
            for j in range(len(primes)):
                if vals[j] == vals[inx]:
                    cnts[j] += 1
            result.append(vals[inx])
        return result[-1]
