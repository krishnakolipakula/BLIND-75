Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        i=1
        while temp.next!= None:
            temp=temp.next
            i+=1
        #required removable position is i-n+1
        temp1=head
        k=i-n+1
        if i==1:
            head=None
            return head
        elif k==1:
            head=head.next
            return head
        else:
            j=1
            temp2=head
            while j!=k:
                temp2=temp1
                temp1=temp1.next
                j+=1
            temp2.next=temp1.next
            return head 


        
