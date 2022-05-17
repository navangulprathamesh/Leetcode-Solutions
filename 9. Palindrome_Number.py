class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        len1=len(x)
        flag=0
        for i in range(len1//2):
            if(x[i]!=x[len1-i-1]):
                return False
        return True    
