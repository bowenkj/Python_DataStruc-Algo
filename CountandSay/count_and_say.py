class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        say = '1'
        while n > 1:
            len_say = len(say)
            i = 0
            temp = say[0]
            next_say = ""
            while i < len_say:
                cnt = 0
                while i < len_say and say[i] == temp:
                    cnt += 1
                    i += 1
                next_say += str(cnt) + temp
                if i == len_say:
                    break
                # here: say[i] != temp
                temp = say[i]
            say = next_say
            n -= 1
        return say
