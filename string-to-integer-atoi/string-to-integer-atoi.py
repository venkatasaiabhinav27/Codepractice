class Solution:
    def myAtoi(self, s: str) -> int:
            if(len(s) == 0):
                return 0
            i = s[0]
            j = 0
            final = ""
            while((i != '-' and i!= "+") and (ord(i)<ord("0") or ord(i)>ord("9"))):
                if(i != " "):
                    return 0
                if(j+1 < len(s)):
                    j+=1
                else:
                    return 0
                i=s[j]
            if(s[j] == '-'):
                if(j+1 == len(s) or (ord(s[j+1])<ord("0") or ord(s[j+1])>ord("9"))):
                    return 0
                j = j+1
                while(j<len(s) and (ord(s[j])>=ord("0") and ord(s[j])<=ord("9"))):
                    final+=(s[j])
                    j+=1
                if((-1*int(final)) < (-2**31)):
                    return -2**31
                else:
                    return -1*int(final)
            else:
                if(s[j] == '+'):
                    if(j+1 == len(s) or (ord(s[j+1])<ord("0") or ord(s[j+1])>ord("9"))):
                        return 0
                    j+=1
                while(j<len(s) and (ord(s[j])>=ord("0") and ord(s[j])<=ord("9"))):
                    final+=(s[j])
                    j+=1
                if(int(final) > 2**31-1):
                    return 2**31-1
                else:
                    return int(final)