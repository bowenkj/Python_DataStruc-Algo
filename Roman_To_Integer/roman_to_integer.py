class Solution(object):
    def __init__(self):
        self.symbols = {}
        self.symbols['I'] = (1, 1)
        self.symbols['V'] = (2, 5)
        self.symbols['X'] = (3, 10)
        self.symbols['L'] = (4, 50)
        self.symbols['C'] = (5, 100)
        self.symbols['D'] = (6, 500)
        self.symbols['M'] = (7, 1000)
        self.symbols['IV'] = 4
        self.symbols['IX'] = 9
        self.symbols['XL'] = 40
        self.symbols['XC'] = 90
        self.symbols['CD'] = 400
        self.symbols['CM'] = 900

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if not n:
            return 0
        sum = 0
        skip = False
        index = 0
        while index < n:
            symbol = s[index]
            symbol_value = self.symbols[symbol][1]
            if index + 1 < n:
                next_symbol = s[index + 1]
                symbol_level, next_symbol_level = self.symbols[symbol][0], self.symbols[next_symbol][0]
                if symbol_level < next_symbol_level:
                    concat = s[index:index + 2]
                    sum += self.symbols[concat]
                    index += 2
                elif symbol_level == next_symbol_level:
                    sum += 2 * (symbol_value)
                    index += 2
                    if index < n:
                        next_next_symbol = s[index]
                        if symbol == next_next_symbol:
                            sum += symbol_value
                            index += 1
                else:
                    sum += symbol_value
                    index += 1
            else:
                sum += symbol_value
                index += 1
        return sum