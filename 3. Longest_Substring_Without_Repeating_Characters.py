class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)==0 or len(s)==1:
            return len(s)
        
        final=[]
        str1=""
        i=0
        while(i<len(s)):
            if(s[i] in str1):
                final.append(len(str1))
                index1=str1.index(s[i])
                str1=str1[index1+1:]
                
            else:
                str1+=s[i]
                i+=1
        if(i==len(s)):
            final.append(len(str1))
        return max(final)
        
