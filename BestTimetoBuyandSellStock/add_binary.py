class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m, n = len(a), len(b)
        if m < n:
            a, b = b, a  # keep length of a larger than or equal to the one of b

        i, j = len(a) - 1, len(b) - 1

        carry = 0
        ans = ""
        while j > -1:
            temp_a, temp_b = int(a[i]), int(b[j])
            temp_sum = temp_a + temp_b
            if carry:
                temp_sum += 1
            carry = 1 if temp_sum > 1 else 0
            ans = str(temp_sum % 2) + ans
            i -= 1
            j -= 1
        while i > -1:
            temp = int(a[i])
            if carry:
                temp += 1
            else:
                ans = a[:i + 1] + ans
                break
            carry = 1 if temp > 1 else 0
            ans = str(temp % 2) + ans
            i -= 1
        if carry:
            ans = '1' + ans
        return ans