class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in result:
                result[key].append(s)
            else:
                result[key] = [s]
        return result.values()

    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        char_nums = []
        for s in strs:
            nums = {}
            for c in s:
                if c in nums:
                    nums[c] += 1
                else:
                    nums[c] = 1
            char_nums.append(nums)

        char_nums_str = []
        for num in char_nums:
            s = ""
            for k in sorted(num.keys()):
                s += k + str(num[k])
            char_nums_str.append(s)

        symbols = {}
        for i in range(len(char_nums_str)):
            if char_nums_str[i] in symbols:
                symbols[char_nums_str[i]].append(strs[i])
            else:
                symbols[char_nums_str[i]] = [strs[i]]
        return symbols.values()
