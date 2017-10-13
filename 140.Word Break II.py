class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        mem = defaultdict(list)
        mem[''].append('')
        return self.dfs(s, wordDict, mem)

    def dfs(self, s, wordDict, mem):
        if s in mem:
            return mem[s]

        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                lst = self.dfs(s[i + 1:], wordDict, mem)
                if len(lst) == 0:
                    continue
                elif len(lst) == 1 and lst[0] == '':
                    mem[s].append(s[:i + 1])
                else:
                    for string in lst:
                        mem[s].append(s[:i + 1] + ' ' + string)
        return mem[s]
