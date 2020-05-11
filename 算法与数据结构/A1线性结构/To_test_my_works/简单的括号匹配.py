from 栈的实现 import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':  # 碰到左括号，就加到栈中去
            s.push(symbol)
        else:  # 不是左括号，说明就是右括号
            if s.isEmpty():  # 为空，说明左右括号不平衡
                balanced = False
            else:  # 是右括号，且不为空，就把栈顶的左括号踢出去，
                s.pop()
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


print(parChecker('((()))'))
print(parChecker('((()'))


