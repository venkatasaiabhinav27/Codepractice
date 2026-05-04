// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long min = 1, max = n;
        while (min <= n && max >= 0 && min <= max) {
            int mid = (min+max)/2;
            if (isBadVersion(mid)) {
                max = mid-1;
            } else {
                min = mid+1;
            }
        }
        return min;
    }
};