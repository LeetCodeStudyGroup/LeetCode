class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        next = 0
        result.append(next)
        for i in range(pow(2, n) - 1):
            next = self.convert(next, i)
            result.append(next)
        return result

    def convert(self, val, times):
    	if times % 2 == 0:
    		return self.not_n(val , 0)
    	else:
    		tmp = val
    		i = 0
    		while True:
    			if tmp & 1 == 1:
    				break
    			tmp = tmp >> 1
    			i += 1
    		return self.not_n(val , i + 1)

    def not_n(self, num, cnt):
    	mask = 1 << cnt
    	return  num + mask if num & mask == 0 else num - mask
