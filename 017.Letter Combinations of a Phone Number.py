class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        table = [[' '], ['*'], ['a', 'b', 'c'], ['d', 'e', 'f'], \
            ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], \
            ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        result = []
        for d in digits:
            if len(result) == 0:
                result.extend(table[int(d)])
            else:
                i = 0
                new_result = []
                for c in table[int(d)]:
                    for item in result:
                        new_result.append(item + c)
                result = new_result
        return result
