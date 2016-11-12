class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        table, val = {}, 0
        for num in nums:
            table[num] = table[num] + 1 if num in table else 1
            val = max(table[num], val)
        frequents = [None] * val
        for key in table:
            if frequents[table[key] - 1] == None:
                frequents[table[key] - 1] = []
            frequents[table[key] - 1].append(key)
        result = []
        i, j = k, val - 1
        while i > 0:
            while frequents[j] == None:
                j -= 1
            result.extend(frequents[j])
            i, j = i - len(frequents[j]), j - 1
        return result

    def topKFrequent2(self, nums, k):
        table = {}
        for num in nums:
            table[num] = table[num] + 1 if num in table else 1
        frequents = []
        for key in table:
            frequents.append((key, table[key]))
        for i in range((len(frequents) - 1) / 2, -1, -1):
            self.heapify(frequents, i, len(frequents))
        result = []
        for i in range(k):
            result.append(frequents[0][0])
            frequents[0], frequents[len(frequents) - 1 - i] = frequents[len(frequents) - 1 - i], frequents[0]
            self.heapify(frequents, 0, len(frequents) - 1 - i)
        return result

    def heapify(self, nums, root, size):
        left, right, inx = root * 2 + 1, root * 2 + 2, root
        if left < size and nums[inx][1] < nums[left][1]:
            inx = left
        if right < size and nums[inx][1] < nums[right][1]:
            inx = right
        if inx != root:
            nums[root], nums[inx] = nums[inx], nums[root]
            self.heapify(nums, inx, size)
    
