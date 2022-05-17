class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        flag=1
        i=0
        j=len(s)-1   
        count=len([i for i in s if i in ["a","e","i","o","u","A","E","I","O","U"]])
        k=0
        while(k<count//2):    
            if(s[i] in ["a","e","i","o","u","A","E","I","O","U"]):
                if(s[j] in ["a","e","i","o","u","A","E","I","O","U"]):
                    temp=s[i]
                    s[i]=s[j]
                    s[j]=temp
                    i=i+1
                    k=k+1
                    j=j-1
                else:
                    j=j-1
            else:
                i=i+1
            
        return "".join(s)
        
