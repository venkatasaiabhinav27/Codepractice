class Solution {
public:
    int longestPalindrome(string s) {
        if (s.size() == 0)
            return 0;
        unordered_map<char, int> pal;
        for(char c: s) {
            pal[c]++;
        }
        int longest = 0;
        for(auto it= pal.begin(); it!= pal.end(); it++) {
            if (it->second%2 == 0) {
                longest+=it->second;
            } else if (it->second/2 >= 1) {
                longest+=it->second-1;
            }
        }
        if (longest < s.size()) {
            longest++;
        }
        return longest;
    }
};