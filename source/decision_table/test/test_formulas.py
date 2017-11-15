import unittest


class Test(unittest.TestCase):

    def test_(self):
        self.assertEqual(4, postfixEval('2 2 +'))
        self.assertEqual(5, postfixEval('1 2 2 * +'))

    def test_infix_to_postfix(self):
        self.assertEqual('A B * C D * +',
                         infixToPostfix('A * B + C * D'))
        self.assertEqual('A B + C * D E - F G + * -',
                         infixToPostfix('( A + B ) * C - ( D - E ) * ( F + G )'))


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = []
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while opStack and (prec[opStack[-1]] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.append(token)

    while opStack:
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def postfixEval(expr):
    vars = {
        'x': 2,
        'y': 8
    }
    operands = []
    tokens = expr.split()

    for token in tokens:
        if token in "0123456789":
            operands.append(int(token))
        elif token in "+-/*":
            operand2 = operands.pop()
            operand1 = operands.pop()
            result = doMath(token, operand1, operand2)
            operands.append(result)

    return operands.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
