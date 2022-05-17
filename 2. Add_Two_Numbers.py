# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(l1):
            p=l1
            prev=None
            next=None
            while(p!=None):
                next=p.next;
                p.next=prev
                prev=p
                p=next
            return prev
        def solve(l1,l2):
            
            l3=None
            carry=0
            while(l1!=None and l2!=None):
                temp=l1.val+l2.val+carry
                cal=temp%10
                carry=temp//10
                
                p=ListNode(cal,l3)
                l3=p
                l1=l1.next
                l2=l2.next 
            if(l1!=None):
                while(l1!=None):
                    temp=l1.val+carry
                    cal=temp%10
                    carry=temp//10
                    p=ListNode(cal,l3)
                    l3=p
                    l1=l1.next
            if(l2!=None):
                while(l2!=None):
                    temp=l2.val+carry
                    cal=temp%10
                    carry=temp//10
                    p=ListNode(cal,l3)
                    l3=p
                    l2=l2.next
            if(carry):
                p=ListNode(carry,l3)
                l3=p
            return l3
        
        res=solve(l1,l2)
        return reverse(res)
         
        
