class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.value <= l2.value:
            new_head = l1
            l1 = l1.next
        else:
            new_head = l2
            l2 = l2.next

        temp = new_head
        while l1 is not None and l2 is not None:
            if l1.value <= l2.value:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        temp.next = l1 if l1 is not None else l2

        return new_head