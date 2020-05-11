from A1线性结构.栈的实现 import Stack

# 创建对象
s = Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())

s.push(True)
print(s.size())

s.push(2.3333333)
print(s.pop())
print(s.pop())
print(s.size())


