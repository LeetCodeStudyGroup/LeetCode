class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        is_pos = True
        if n < 0: 
            n, is_pos = -n, False
        val = 1
        while n != 0:
            if n % 2 == 1:
                val *= x
            x *= x
            n >>= 1
        return val if is_pos else 1 /val

    def myPow2(self, x, n):
        if n == 0: 
            return 1
        elif n < 0: 
            return 1 / self.myPow(x, -n)
        elif n % 2 == 0:
            val = self.myPow(x, n / 2)
            return val * val
        else:
            return x * self.myPow(x, n - 1)
