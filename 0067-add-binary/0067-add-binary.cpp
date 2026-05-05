class Solution {
public:
    string addBinary(string a, string b) {
        int carry = 0;
        string output = ""; 
        int apos = a.size()-1, bpos = b.size()-1;
        int sum;
        while(apos > -1 || bpos > -1) {
            sum = 0;
            if (apos > -1 && a[apos] == '1') {
                sum += 1;
            }
            if (bpos > -1 && b[bpos] == '1') {
                sum += 1;
            }
            if (carry == 1) {
                sum = sum+1;
            }
            if (sum == 3) {
                output = '1' + output;
                carry = 1;
            } else if (sum == 2) {
                output = '0' + output;
                carry = 1;
            } else if (sum == 1) {
                output = '1' + output;
                carry = 0;
            } else {
                output = '0' + output;
                carry = 0;
            }
            apos--;
            bpos--;
        }

        if (carry == 1) {
            output = '1' + output;
        }
        return output;
    }
};