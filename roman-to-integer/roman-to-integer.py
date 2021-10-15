class Solution:
    def romanToInt(self, s: str) -> int:
        I =1
        V =5
        X=10
        L=50
        C=100
        D=500
        M=1000
        Max =0
        dec =0
        for i in range(len(s)-1,-1,-1):
            if(s[i]=='I'):
                if(Max<=I):
                    dec+=I
                    Max = I
                else:
                    dec-=I
            elif(s[i]=='V'):
                if(Max<=V):
                    dec+=V
                    Max = V
                else:
                    dec-=V
            elif(s[i]=='X'):
                if(Max<=X):
                    dec+=X
                    Max =X
                else:
                    dec-=X
            elif(s[i]=='L'):
                if(Max<=L):
                    dec+=L
                    Max = L
                else:
                    dec-=L
            elif(s[i]=='C'):
                if(Max<=C):
                    dec+=C
                    Max = C
                else:
                    dec-=C
            elif(s[i]=='D'):
                if(Max<=D):
                    dec+=D
                    Max =D
                else:
                    dec-=D
            elif(s[i]=='M'):
                if(Max<=M):
                    dec+=M
                    Max = M
                else:
                    dec-=M
        return dec
            
            
        