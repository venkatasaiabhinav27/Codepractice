class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> mapS = new HashMap<>();

        for(char c:s.toCharArray()) {
            mapS.put(c, 1+mapS.getOrDefault(c, 0));
        }

        for(char c:t.toCharArray()) {
            if (mapS.get(c) == null) {
                return false;
            } else {
                if (mapS.get(c) == 1) {
                    mapS.remove(c);
                } else {
                    mapS.put(c, mapS.get(c) - 1);
                }
            }
        }

        if (mapS.size() == 0) {
            return true;
        }

        return false;
    }
}