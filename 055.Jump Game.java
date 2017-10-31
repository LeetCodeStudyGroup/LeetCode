/*
    Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Determine if you are able to reach the last index.

    For example:
    A = [2,3,1,1,4], return true.

    A = [3,2,1,0,4], return false.
     */

    public boolean canJump(int[] nums) {
        int size = nums.length;
        if (size == 0)
            return true;
        boolean[] canArrive = new boolean[nums.length];
        canArrive[size - 1] = nums[size - 1] != 0;
        for (int i=0; i<size-1; i++) {
            canArrive[i] = false;
        }

        for (int i=size-1; i>=0; i--) {
            int jLimit = i+nums[i]+1<size ? i+nums[i]+1 : size;
            for (int j=i; j<jLimit; j++) {
                if (canArrive[j]) {
                    canArrive[i] = true;
                    break;
                }
            }
        }

        return canArrive[0];
    }
