class Node:
    def __init__(self, initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        '''
        修改数据项
        :param newData:
        :return:
        '''
        self.data = newData

    def setNext(self, newNext):
        '''
        修改下一个的指向的引用
        :param newNext:
        :return:
        '''
        self.next = newNext



temp = Node(93)
print(temp.getData())






