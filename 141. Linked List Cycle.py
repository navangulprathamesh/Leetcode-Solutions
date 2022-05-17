# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        p=head
        dict2={}
        
        while(p!=None and p not in dict2.keys()  ):
            
            dict2[p]=True
            p=p.next
        print(p)
        if(p==None):
            return False
        elif(dict2[p]==True):
            return True
        else:
            return False
        
