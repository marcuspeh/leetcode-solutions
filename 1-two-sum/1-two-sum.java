class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int leftover = target - nums[i];
            
            if (hashMap.containsKey(leftover)) {
                return new int[] {i, hashMap.get(leftover)};
            }
            
            hashMap.put(nums[i], i);
        }
        return new int[]{};
    }
}