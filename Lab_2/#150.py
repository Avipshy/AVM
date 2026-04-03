class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack = []

        for element in tokens:
            if element == '+':
                stack.append(stack.pop() + stack.pop())

            elif element == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            elif element == '*':
                stack.append(stack.pop() * stack.pop())

            elif element == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))

            else:
                stack.append(int(element))
        
        return stack[0]