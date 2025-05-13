# 🔄 Reverse a Singly Linked List


```shell

🚀 Explanation & Approach:
To reverse a singly linked list, we iterate through the list and reverse the direction of the pointers.

We maintain three pointers:
- prev: Initially None, it keeps track of the previous node.
- curr: Initially head, it keeps track of the current node.
- next_node: Temporarily stores the next node, so we don’t lose reference to the rest of the list during reversal.

🔁 Step-by-Step:
1. Traverse the list using curr.
2. For each node, store the next node in next_node.
3. Reverse the current nodes pointer to point to prev.
4. Move prev and curr one step forward.
5. Continue until curr becomes None.
6. prev will point to the new head of the reversed list.

💻 Python Code:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next     # Step 1: Store next node
            curr.next = prev          # Step 2: Reverse pointer
            prev = curr               # Step 3: Move prev forward
            curr = next_node          # Step 4: Move curr forward

        return prev  # New head

🧪 Test Code:
# Helper to create linked list from list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper to convert linked list back to list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Run test
solution = Solution()
head = create_linked_list([1, 2, 3, 4, 5])
reversed_head = solution.reverseList(head)
print(linked_list_to_list(reversed_head))  # Output: [5, 4, 3, 2, 1]

📈 Time & Space Complexity:
- Time Complexity: O(n) – each node is visited once
- Space Complexity: O(1) – constant space for pointer manipulation

🏷️ Tags:
#LinkedList #Reverse #Pointers #Python #DataStructures #InterviewPrep
