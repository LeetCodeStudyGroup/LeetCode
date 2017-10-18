class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.nums.append(number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        cache = set()
        for num in self.nums:
            if value - num in cache:
                return True
            cache.add(num)
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
