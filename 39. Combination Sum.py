import copy

class Solution:

    def removeDuplication(self, nums):
        nums.sort()

        results = []
        results.append(nums[0])

        for num in nums:
            if num != results[-1]:
                results.append(num)

        return results

    def sumOfCombination(self, combination):
        sum = 0
        for num in combination:
            sum += num

        return sum

    def dfs(self, nums, startIndex, target, tempCombination, results):
        if self.sumOfCombination(tempCombination) == target:
            temp = copy.deepcopy(tempCombination)
            results.append(temp)
            return

        if self.sumOfCombination(tempCombination) > target:
            return

        for i in range(startIndex, len(nums)):
            tempCombination.append(nums[i])
            self.dfs(nums, i, target, tempCombination, results)
            tempCombination.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if candidates is None or len(candidates) == 0:
            return

        # 去重
        nums = self.removeDuplication(candidates)

        tempCombination = []
        results = []

        self.dfs(nums, 0, target, tempCombination, results)

        return results
