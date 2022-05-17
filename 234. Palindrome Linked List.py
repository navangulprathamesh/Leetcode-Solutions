# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(q):
            prev=None
            next=None
            k=q
            while(k!=None):
                next=k.next
                k.next=prev
                prev=k
                k=next
            return  prev
        slow=head
        if(slow.next!=None):
            fast=slow.next
        else:
            fast=head
        while(fast.next!=None):
            slow=slow.next
            fast=fast.next
            if(fast.next!=None):
                fast=fast.next
        new=reverse(slow.next)
        p=head
        while(new!=None):
            
            if(p.val!=new.val):
                return False
            p=p.next
            new=new.next
        return True
        
        
        
        
