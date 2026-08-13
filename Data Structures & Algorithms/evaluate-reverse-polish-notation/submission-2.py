class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a/b),
        }
        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                num2=stack.pop()
                num1=stack.pop()
                res = ops[token](num1, num2)
                stack.append(res)
        return stack[0]
        