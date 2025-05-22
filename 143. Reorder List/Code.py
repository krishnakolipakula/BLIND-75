# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse_order(head):
            prev=None
            current=head
            while current!=None:
                next_node=current.next
                current.next=prev
                prev=current
                current=next_node
            return prev
        temp=head
        i=1
      #breaking down the linked list into two till the mid
        while temp.next!=None:
            temp=temp.next
            i+=1
        mid=i//2
        j=1
        temp1=head
        while j<=mid:
            temp1=temp1.next
            j+=1
        new_head=temp1.next
        temp1.next=None
        #reversing the second linke list
        new_head=reverse_order(new_head)
        #insertion of each element in list2 to list 1 between nodes
        current,second=head,new_head
        i,f=0,0
        while second!=None:
            insert=second
            second=second.next
            insert.next=None
            new_head=second
            next_node=current.next
            current.next=insert
            insert.next=next_node
            current=current.next.next
        return head
