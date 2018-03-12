class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if haystack == None or needle == None or len(haystack) < len(needle):
            return -1
        if len(needle) == 0 or needle == "":
            return 0

        for i in range(0, len(haystack)):
            if len(needle) > len(haystack[i:]):
                return -1
            
            for j in range(0, len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                
                if j == len(needle) - 1:
                    return i
                
        return -1
