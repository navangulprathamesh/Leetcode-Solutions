class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.strip().split()
        low=0
        high=len(l)
        mid= low+((high-1-low)//2)
        for i in range(low,mid+1):
            temp=l[i]
            l[i]=l[high-i-1]
            l[high-i-1]=temp
        return " ".join(l)
