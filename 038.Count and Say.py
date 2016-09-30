class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        base = '1'
        result = '1'
        for x in range(n - 1):
            base = result
            result = []
            count = 0
            symbol = None
            for i in range(len(base)):
                if symbol != base[i]:
                    if symbol != None:
                        result.append(str(count))
                        result.append(symbol)
                    symbol = base[i]
                    count = 0
                count += 1
            result.append(str(count))
            result.append(symbol)
        return ''.join(result)
