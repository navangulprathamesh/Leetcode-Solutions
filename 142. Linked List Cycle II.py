# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        dict2={}
        i=0
        while(p!=None and p not in dict2.keys()  ):
            
            dict2[p]=True
            p=p.next
            i+=1
        
        if(p==None):
            return None
        elif(dict2[p]==True):
            return p
        else:
            return None
