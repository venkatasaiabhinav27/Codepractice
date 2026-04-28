class Solution {
    public int search(int[] nums, int target) {
        int min = 0, max = nums.length-1;
        while (min > -1 && min <= max && max <nums.length) {
            int mid = (min+max)/2;
            if (nums[mid] == target) {
                return mid;
            } else if (target < nums[mid]) {
                max = mid-1;
            } else {
                min = mid+1;
            }
            // if (min == max) {
            //     return -1;
            // }
        }
        return -1;
    }
}