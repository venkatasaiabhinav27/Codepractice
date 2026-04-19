class Solution {
    public boolean isValid(String s) {
        Stack<Character> brcs = new Stack<>(); 
        for (int i = 0; i < s.length() ; i++) {
            System.out.println(s.charAt(i));
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[') {
                brcs.push(s.charAt(i));
            } else if (s.charAt(i) == ')' || s.charAt(i) == '}' || s.charAt(i) == ']') {
                if (brcs.isEmpty()) {
                    return false;
                }
                char poppeedVal = brcs.pop();
                if ((s.charAt(i) == ')' && poppeedVal != '(') ||
                    (s.charAt(i) == '}' && poppeedVal != '{') ||
                    (s.charAt(i) == ']' && poppeedVal != '[')) {
                        return false;
                    }
            } else {
                return false;
            }
        }
        if (brcs.size() == 0) {
            return true;
        }
        return false;
    }
}