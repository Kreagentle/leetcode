class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        sent = ListNode(0)
        sent.next = head

        prev, temp = sent, head
        while temp:
            if temp.val == val:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next

        return sent.next