class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = []

        def solve(opened, closed):

            if opened == closed == n:
                res.append("".join(stack))

            if opened < n:
                stack.append('(')
                solve(opened + 1, closed)
                stack.pop()
            
            if closed < opened:
                stack.append(')')
                solve(opened, closed + 1)
                stack.pop()

        solve(0, 0)
        return res