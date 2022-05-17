class Solution:
    def reverse(self, x: int) -> int:
        
        ans=""
        if(x<0):
            ans="-"
            x=str(x)[1:]
        else:
            x=str(x)
        list1=str(int(x[::-1]))
        ans=ans+list1
        if(int(ans)>=-(2**31) and int(ans)<=(2**31-1)):
            return ans
        else:
            return 0
