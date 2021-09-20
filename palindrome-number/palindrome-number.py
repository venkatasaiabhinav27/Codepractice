class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        org=x
        p = 0
        while(x != 0):
            p*=10
            p+=x%10
            x//=10
        if(p==org):
            return True
        return False
        