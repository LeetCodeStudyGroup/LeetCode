class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.do_permute(result, [], nums)
        return result

    def do_permute(self, result, selected, remainder):
    	if len(remainder) == 1:
    		selected.append(remainder.pop(0))
    		result.append(selected)
    	elif len(remainder) > 1:
    		for i in range(len(remainder)):
    			new_selected = selected[:]
    			new_remainder = remainder[:]
    			new_selected.append(new_remainder.pop(i))
    			self.do_permute(result, new_selected, new_remainder)
