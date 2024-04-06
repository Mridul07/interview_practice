class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        actions = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in actions:
                stack.append(int(token))
            else:
                element1 = int(stack.pop())
                element2 = int(stack.pop())
                if token == "+":
                    stack.append(element2+element1)
                elif token == "-":
                    stack.append(element2-element1)
                if token == "*":
                    stack.append(element2*element1)
                if token == "/":
                    stack.append(int(element2/element1))
        
        return stack.pop()