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
        old2New = {}
        newHead = RandomListNode(head.label)
        while head is not None:
            old2New[head] = newHead
            head = head.next
            nextNewHead = RandomListNode(head.label) if head else None
            newHead.next = nextNewHead
            newHead = nextNewHead
        head = oldHead
        newHead = old2New[head]
        while head is not None:
            random = head.random
            if random:
                newRandom = old2New[random]
                newHead.random = newRandom
            head = head.next
            newHead = newHead.next
        return old2New[oldHead]

