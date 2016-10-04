class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.gen(result, n, n, '')
        return result
                
    def gen(self, result, l ,r, cur):
        if l == 0:
            result.append(cur + ')' * r)
        elif l == r:
            self.gen(result, l - 1 , r, cur + '(')
        elif l < r:
            self.gen(result, l - 1 , r, cur + '(')
            self.gen(result, l , r - 1, cur + ')')
