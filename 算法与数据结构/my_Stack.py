class Stack:
    def __init__(self):
        # 以列表的形式来保存元素，从而实现栈的一些操作
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        # 法一：栈底是首端 ->复杂度O(1)
        # 相当于list中的append方法
        self.items.append(item)
        # 法二: 栈顶是首端 -> 复杂度 O(n)
        # self.items.insert(0 ,item)

    def pop(self):
        # 法一：栈底是首端 ->复杂度O(1)
        # 相当于list中的pop方法
        return self.items.pop()
        # 法二: 栈顶是首端 -> 复杂度 O(n)
        # return self.items.pop(0)

    def peek(self):
        # 法一：栈底是首端
        # 列表中最后一个元素的索引是 -1
        return self.items[len(self.items) -1]
        # 法二: 栈顶是首端
        # return self.items[0]


    def size(self):
        return len(self.items)
