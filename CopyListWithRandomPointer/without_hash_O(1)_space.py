# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        oldHead = head
        if head is None:
            return None
        newHead = RandomListNode(head.label)
        temp = newHead
        while head is not None:
            headNext = head.next # may be None
            newHead.next = headNext
            head.next = newHead
            head = headNext
            newHead = RandomListNode(head.label) if head else None
        head = oldHead
        while head is not None:
            if head.random is not None:
                head.next.random = head.random.next
            head = head.next.next
        a = oldHead
        b = a.next
        c = b.next
        d = c.next if c else None
        while a is not None:
            a.next = c
            b.next = d
            if not c:
                break
            a = c
            b = d
            c = b.next
            d = c.next if c else None
        return temp