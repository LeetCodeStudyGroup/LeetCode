class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        rst, record, nums = '', {}, [''] * (len(s) + 1)
        for c in s:
            record[c] = record[c] + 1 if c in record else 1
        for k, v in record.iteritems():
            nums[v] += k * v
        for i in range(len(s), 0, -1):
            if len(nums[i]) > 0:
                rst += nums[i]
        return rst
