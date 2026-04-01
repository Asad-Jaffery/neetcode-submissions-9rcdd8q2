class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operations = ("+", "-", "*", "/")
        for i in range(len(tokens)):

            if tokens[i] not in operations:
                s.append(int(tokens[i]))
            else:
                num1 = s.pop()
                num2 = s.pop()

                if tokens[i] == '+':
                    res = num2 + num1
                    s.append(res)

                elif tokens[i] == '-':
                    res = num2 - num1
                    s.append(res)

                elif tokens[i] == '*':
                    res = num2 * num1
                    s.append(res)

                elif tokens[i] == '/':
                    res = num2 / num1
                    s.append(int(res))

        return s[-1]




        