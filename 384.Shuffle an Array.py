class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums
        self.shuffled = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        for i in range(len(self.nums)):
            r = random.randint(0, len(self.nums) - 1)
            self.shuffled[i], self.shuffled[r] = self.shuffled[r], self.shuffled[i]
        return self.shuffled

class Solution2(object):
    def __init__(self, nums):
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))
