class Solution:
    def romanToInt(self, s: str) -> int:
        Roman = {'I' :1,'V' :5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        Max =0
        dec =0
        for i in range(len(s)-1,-1,-1):
            if(Max<=Roman[s[i]]):
                    dec+=Roman[s[i]]
                    Max = Roman[s[i]]
            else:
                    dec-=Roman[s[i]]
        return dec
            
            
        