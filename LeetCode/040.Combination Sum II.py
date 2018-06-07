class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if len(candidates) > 0:
            self.find_result(result, sorted(candidates), target, 0, 0, [])
        return result

    def find_result(self, result, candidates, target, val, index, sets):
        new_val = val + candidates[index]
        if new_val == target:
            sets.append(candidates[index])
            result.append(sets)
        elif new_val < target and index + 1 < len(candidates):
            new_index = index
            while new_index + 1 < len(candidates):
                if candidates[new_index] != candidates[new_index + 1]:
                    self.find_result(result, candidates, target, val, new_index + 1, list(sets))
                    break
                new_index += 1
            sets.append(candidates[index])
            self.find_result(result, candidates, target, new_val, index + 1, list(sets))
