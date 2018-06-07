class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [ 'FizzBuzz' if x % 15 == 0 else 'Buzz' if x % 5 == 0 else 'Fizz' if x % 3 == 0 else str(x) for x in range(1, n + 1)]
        return map(lambda x: 'FizzBuzz' if x % 15 == 0 else 'Buzz' if x % 5 == 0 else 'Fizz' if x % 3 == 0 else str(x), range(1, n + 1))
