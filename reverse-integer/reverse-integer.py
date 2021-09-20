class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s = s[::-1]
        if(s[len(s)-1] == '-'):
            s = s[0:(len(s)-1)]
            i = int(s) * -1
            if(i<-(2**31)):
                return 0
            else:
                return i
        i = int(s)
        if(i>((2**31)-1)):
           return 0
        else:
           return i