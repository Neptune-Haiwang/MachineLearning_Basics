class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        '''
        把item添加到队尾，无返回值
        :param item:
        :return:
        '''
        self.items.insert(0, item)

    def dequeue(self):
        '''
        从队首移除数据项，返回值为队首数据项
        :return:
        '''
        return self.items.pop()

    def size(self):
        return len(self.items)
