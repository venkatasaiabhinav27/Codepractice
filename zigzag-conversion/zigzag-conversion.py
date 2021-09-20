class Solution:
    def convert(self,s: str, numRows: int) -> str:
        st = []
        n = numRows
        for j in range(numRows):
            st.append("")
        i =0
        pos=0
        if numRows==1:
            return s
        while(i < len(s)):
            if(pos==0):
                for j in range(numRows):
                    if i<len(s):
                        st[pos]+=(s[i])
                        pos+=1
                        i+=1
            else:
                if numRows==pos:
                    pos-=2
                if pos!=0:
                    st[pos]+=s[i]
                    pos-=1
                    i+=1
        zigzag=""
        for i in st:
            zigzag+=i
        return zigzag
        