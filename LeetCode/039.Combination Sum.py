class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if len(candidates) > 0:
            sorted_candidates = sorted(candidates)
            self.find_sum(result, sorted_candidates, target, 0, 0, [])
        return result
        
    def find_sum(self, result, candidates, target, val, index, sets):
        new_val = val + candidates[index]
        if new_val == target:
            sets.append(candidates[index])
            result.append(sets)
        elif new_val < target:
            if index + 1 < len(candidates):
                self.find_sum(result, candidates, target, val, index + 1, list(sets))
            sets.append(candidates[index])
            self.find_sum(result, candidates, target, new_val, index, sets)
