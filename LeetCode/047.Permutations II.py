class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
    	self.do_permute(result, [], sorted(nums))
    	return result

    def do_permute(self, result, selected, remainder):
        if self.all_same(remainder):
            for i in range(len(remainder)):
    		    selected.append(remainder.pop(0))
            if len(selected) > 0:
                result.append(selected)
    	else:
    		i = 0
    		while i < len(remainder):
    			if i == 0 or remainder[i] != remainder[i - 1]:
    				new_selected = selected[:]
    				new_remainder = remainder[:]
    				new_selected.append(new_remainder.pop(i))
    				self.do_permute(result, new_selected, new_remainder)
    			i += 1

    def all_same(self, nums):
    	for i in range(len(nums) - 1):
    		if nums[i] != nums[i + 1]:
    			return False
    	return True
