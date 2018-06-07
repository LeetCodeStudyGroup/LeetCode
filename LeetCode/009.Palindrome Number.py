class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        numbers = []
        while x > 0:
            numbers.append(x % 10)
            x /= 10
            
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] != numbers[j]:
                return False
            i += 1
            j -= 1
        return True
        