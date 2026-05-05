class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int rep = 0, val = 0;
        unordered_map<int, int> freq;
        for (int num:nums) {
            freq[num]++;
            if (freq[num] > rep) {
                val = num;
                rep = freq[num];
            }
        }
        return val;
    }
};