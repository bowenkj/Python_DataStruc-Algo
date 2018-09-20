# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        if head.next is None:
            return True
        left_start, a, b = head, head, head
        last, mid = None, None
        while b is not None and b.next is not None:
            last = a
            a = a.next
            b = b.next.next
        if b is None:  # even nodes
            left_end = last
            right_start = a
        else:  # odd nodes
            left_end = last
            mid = a
            right_start = a.next
        left_end.next = None

        # reverse the right part
        last = None
        temp = right_start
        nextt = temp.next
        while nextt is not None:
            temp.next = last
            last = temp
            temp = nextt
            nextt = nextt.next
        temp.next = last
        right_end = temp

        # comparing starts from left_start and right_end
        a, b = left_start, right_end
        ans = a.val == b.val
        while a is not None:
            if a.val != b.val:
                ans = False
                break
            a,b = a.next,b.next

        # reverse the right part
        last = None
        temp = right_end
        nextt = temp.next
        while nextt is not None:
            temp.next = last
            last = temp
            temp = nextt
            nextt = nextt.next
        temp.next = last

        # concatenate
        if mid is None:
            left_end.next = right_start
        else:
            left_end.next = mid

        return ans

a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(1)
a.next = b
b.next = c
c.next = d

S = Solution()
print S.isPalindrome(a)