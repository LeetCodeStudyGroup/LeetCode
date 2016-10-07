class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = cur = i = 0
        while i < len(height):
            if height[i] > 0:
                j = i + 1
                while j < len(height):
                    if height[j] < height[i]:
                        cur += height[i] - height[j]
                    else:
                        result += cur
                        i = j
                        cur = 0
                        break
                    j += 1
                if i == j:
                    continue
                if j == len(height):
                    height[i] -= 1
                    cur = 0
                    continue
            i += 1
        return result
