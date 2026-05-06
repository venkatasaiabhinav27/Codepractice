class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxsum = INT_MIN, cursum = 0;
        for(int num:nums) {
            if (cursum < 0) {
                cursum = 0;
            }
            cursum += num;
            if (cursum > maxsum) {
                maxsum = cursum;
            }
        }
        return maxsum;
    }
};