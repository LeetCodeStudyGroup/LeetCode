/*
    There are two sorted arrays nums1 and nums2 of size m and n respectively.

    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

    Example 1:
    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0

    Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5
 */

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int index1 = 0, index2 = 0;
        int count = (nums1.length + nums2.length) / 2 + 1;
        boolean isOne = (nums1.length + nums2.length) % 2 == 1;
        int smaller = 0;
        int current = 0;
        while (count != 0) {
            if (nums1.length > index1 && nums2.length > index2) {
                if (nums1[index1] < nums2[index2]) {
                    smaller = current;
                    current = nums1[index1];
                    index1++;
                } else {
                    smaller = current;
                    current = nums2[index2];
                    index2++;
                }
            } else if (nums1.length > index1) {
                smaller = current;
                current = nums1[index1];
                index1++;
            } else {
                smaller = current;
                current = nums2[index2];
                index2++;
            }
            count--;
        }

        if (isOne)
            return current/1.0;

        return (smaller + current) / 2.0;
    }
