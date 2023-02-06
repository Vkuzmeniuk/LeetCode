# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t_list(list(head))
        return head[round(len(head) / 2):]


sol = Solution()
print(sol.middleNode([1, 2, 3, 4, 5, 6]))
