class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s)==1 or len(s)== 0):
            return s
        stat,end = 0,0
        for i in range(len(s)):
            j = len(s)-1
            while(j>i):
                if(s[i]==s[j]):
                    st1 = s[i:j+1]
                    if(st1 == st1[::-1]):
                        if((end-stat)<(j-i)):
                            stat=i
                            end=j
                            break
                j-=1
        print(stat," ",end)
        return s[stat:end+1]
        