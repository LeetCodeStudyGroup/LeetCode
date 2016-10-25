class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        T = [0] * len(needle)
        T[0] = -1
        cnd = 0
        pos = 2
        while pos < len(needle):
            #(first case: the substring continues)
            if needle[pos - 1] == needle[cnd]:
                cnd += 1
                T[pos] = cnd
                pos += 1
            #(second case: it doesn't, but we can fall back)
            elif cnd > 0:
                cnd = T[cnd]
            #(third case: we have run out of candidates.  Note cnd = 0)
            else:
                T[pos] = 0
                pos += 1

        index = i = j = 0
        while index < len(haystack):
            while i < len(haystack) and j < len(needle):
                if haystack[i] != needle[j]:
                    if T[j] == -1:
                        index += 1
                        i = index
                        j = 0
                    elif T[j] == 0:
                        index = i
                        i = index
                        j = 0
                    else:
                        index = i - T[j]
                        j = T[j]
                    break
                else:
                    i += 1
                    j += 1
            if j == len(needle):
                return index
            if i == len(haystack):
                break
        return -1

    def strStr2(self, haystack, needle):
        if haystack == needle:
            return 0
        last_index = -1
        i = 0
        while i < len(haystack):
            tmp = i
            j = 0
            while j < len(needle) and tmp < len(haystack):
                if haystack[tmp] == needle[0] and last_index < j:
                    last_index = tmp
                if haystack[tmp] != needle[j]:
                    break
                tmp += 1
                j += 1
            if j == len(needle):
                return i
            i = last_index if last_index > i else i + 1
        return -1
