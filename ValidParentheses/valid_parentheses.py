class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        heap = []
        counter = {}
        for i in s:
            if i in [")","]","}"]:
                if not len(heap):
                    return False
                last = heap.pop()
                if not((last == "(" and i == ")") or (last == "{" and i == "}") or (last == "[" and i == "]")):
                    return False
            else:
                heap.append(i)
        return False if len(heap) else True
