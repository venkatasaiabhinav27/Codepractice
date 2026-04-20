class Solution {
    public boolean isPalindrome(String s) {
        String sLower = s.toLowerCase();
        System.out.println(sLower);
        int left = 0, right = s.length()-1;
        while (left < right) {
            while ((sLower.charAt(left) < 'a' || sLower.charAt(left) > 'z') && (sLower.charAt(left) < '0' || sLower.charAt(left) > '9')) {
                left++;
                if (left >= s.length()) {
                    return true;
                }
            }

            while ((sLower.charAt(right) < 'a' || sLower.charAt(right) > 'z') && (sLower.charAt(right) < '0' || sLower.charAt(right) > '9')) {
                right--;
                if (right < 0) {
                    return true;
                }
            }
            if (sLower.charAt(left) != sLower.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}