# https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    OPEN = ["(", "[", "{"]
    def isValid(self, s: str) -> bool:
        data = list()
        for symbol in s:
            if symbol in self.OPEN:
                data.append(symbol)
            elif len(data) <= 0:
                return False
            elif symbol == ")":
                if data[-1] == '(':
                    data.pop()
                else:
                    return False
            elif symbol == "]":
                if data[-1] == '[':
                    data.pop()
                else:
                    return False
            elif symbol == "}":
                if data[-1] == '{':
                    data.pop()
                else:
                    return False
        return len(data) == 0
