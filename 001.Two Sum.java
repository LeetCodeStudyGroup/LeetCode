public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map2 = new HashMap<>();
        for(int i=0; i<nums.length; i++) {
            map2.put(nums[i],i);
        }
        for(int i=0;i<nums.length; i++) {
            int answer = target - nums[i];
            if(map2.containsKey(answer) && map2.get(answer) != i) {
                return new int[] {i, map2.get(answer)};
            }
        }
        
        return null;
    }
