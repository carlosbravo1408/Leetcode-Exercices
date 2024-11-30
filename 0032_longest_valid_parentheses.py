#https://leetcode.com/problems/longest-valid-parentheses/


class Solution:
    # slowest approach
    def longestValidParentheses1(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        l, r = 0, 0
        indexes = []
        result = 0
        while l<len(s) and r<len(s):
            adder = 0
            for r in range(l, len(s)):
                if s[r] == "(":
                    adder += 1
                elif s[r] == ")":
                    adder -= 1
                if adder == 0:
                    if indexes and indexes[-1][1] == l-1:
                        indexes[-1] = (indexes[-1][0], r)
                    else:
                        indexes.append((l, r))
                    l = r
                    break
                elif adder < 0:
                    break
                elif adder == len(s):
                    return 0
            l += 1
        for index in indexes:
            if index[1]-index[0]+1 > result:
                result = index[1]-index[0]+1
        return result

    def longestValidParentheses(self, s: str) -> int:
        visited = [0 for _ in range(len(s))]
        for right, parenthesis in enumerate(s):
            if parenthesis == ")":
                if right > 0:
                    if s[right - 1] == "(":
                        if right > 1:
                            visited[right] = visited[right - 2] + 2
                        else:
                            visited[right] = 2
                    else:
                        left = right - visited[right-1] - 1
                        if s[left] != "(":
                            continue
                        if left > 0:
                            visited[right] = 2 + visited[right - 1] + visited[left - 1]
                        elif left == 0:
                            visited[right] = 2 + visited[right - 1]
        return max(visited)


if __name__ == '__main__':
    sol = Solution()
    # assert sol.longestValidParentheses("(()") == 2
    # assert sol.longestValidParentheses("()())(") == 4
    assert sol.longestValidParentheses(")()())") == 4
    assert sol.longestValidParentheses("(()((()))") == 8
    assert sol.longestValidParentheses("(()())") == 6

