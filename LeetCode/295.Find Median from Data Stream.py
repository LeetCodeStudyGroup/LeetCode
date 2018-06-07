class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap, self.minheap = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.minheap) == 0:
            self.minheap.append(num)
        elif len(self.minheap) == 1 and len(self.maxheap) == 0:
            if num > self.minheap[0]:
                self.maxheap.append(Neg(self.minheap[0]))
                self.minheap[0] = num
            else:
                self.maxheap.append(Neg(num))
        else:
            val = num
            if val > self.minheap[0]:
                tmp = heapq.heappop(self.minheap)
                heapq.heappush(self.minheap, val)
                val = tmp
            if val < self.maxheap[0].val:
                tmp = self.max_heappop(self.maxheap)
                self.max_heappush(self.maxheap, val)
                val = tmp

            if len(self.minheap) > len(self.maxheap):
                self.max_heappush(self.maxheap, val)
            else:
                heapq.heappush(self.minheap, val)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minheap) > len(self.maxheap):
            return float(self.minheap[0])
        return float(self.minheap[0] + self.maxheap[0].val) / 2
    
    def max_heappush(self, h, val):
        heapq.heappush(h, Neg(val))
        
    def max_heappop(self, h):
        return heapq.heappop(h).val

class Neg:
    def __init__(self, val):
        self.val = val

    def __cmp__(self, other):
        return -cmp(self.val, other.val)

class MedianFinder2(object):

    def __init__(self):
        self.nums = []

    def addNum(self, num):
        if len(self.nums) == 0:
            self.nums.append(num)
        else:
            self.nums.insert(self.findPos(num), num)

    def findMedian(self):
        if len(self.nums) == 0:
            return None
        mid = len(self.nums) / 2
        if len(self.nums) % 2 == 0:
            return float(self.nums[mid - 1] + self.nums[mid]) / 2
        return float(self.nums[mid])

    def findPos(self, num):
        start, end = 0, len(self.nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if num > self.nums[mid]:
                start = mid
            else:
                end = mid
        if self.nums[end] <= num:
            return end + 1
        if self.nums[start] <= num:
            return start + 1
        return start

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
