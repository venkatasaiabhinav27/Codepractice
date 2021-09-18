class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        if(len(s)==1):
            return 1;
        for i in range(len(s)):
            temparr = [s[i]]
            for j in range(i+1,len(s)):
                if(s[j] not in temparr):
                    temparr.append(s[j])
                    if(length < len(temparr)):
                        length = len(temparr)
                else:
                    if(length < len(temparr)):
                        length = len(temparr)
                    break
        return length
        