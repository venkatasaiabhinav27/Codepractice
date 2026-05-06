class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
     unordered_set<int> freq;
     for(int num: nums) {
        if (freq.find(num) != freq.end()) {
            return true;
        }
        freq.insert(num);
     }
     return false;
    }
};