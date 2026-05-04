class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> mag;
        for (char c: magazine) {
            mag[c]++;
        }
        for (char c: ransomNote) {
            if (mag.find(c) != mag.end()) {
                if (mag[c] == 1) {
                    mag.erase(c);
                } else {
                    mag[c]--;
                }
            } else {
                return false;
            }
        }
        return true;
    }
};