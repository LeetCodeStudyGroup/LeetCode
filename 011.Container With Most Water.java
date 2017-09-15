/*
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
 n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
 Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
*/

    public int maxArea(int[] height) {
        if (height.length < 2)
            return 0;

        int leftIndex = 0;
        int rightIndex = height.length - 1;
        int max = 0;

        while (leftIndex < rightIndex) {
            max = Math.max(max, Math.min(height[rightIndex], height[leftIndex])* (rightIndex - leftIndex));

            if (height[leftIndex] < height[rightIndex])
                leftIndex++;
            else
                rightIndex--;
        }

        return max;
    }
