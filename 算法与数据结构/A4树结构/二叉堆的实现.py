class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):  # KEY上浮的操作
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:  # 插入的值比父节点的值还小，则交换位置
                temp = self.heapList[i//2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2  # 继续沿路径向上

    def minChild(self, i):
        if (i * 2 + 1) > self.currentSize:  # 说明只有唯一的子节点
            return i * 2
        else:  # 返回较小的子节点
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):  # KEY下沉的操作
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc

    def insert(self, k):
        self.heapList.append(k)  # 把数据添加到末尾
        self.currentSize += 1
        self.percUp(self.currentSize)  # 新KEY上浮

    def delMin(self):
        retval = self.heapList[1]  # 移走堆顶
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)  # 新顶下沉
        return retval

    # 从无序表生成'堆'，用下沉法，可以把时间复杂度控制在 O(n)
    def buildHeap(self, alist):
        i = len(alist) // 2  # 从最后节点的父节点开始，因为叶节点无需下沉
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        print(len(self.heapList), i)
        while (i > 0):
            print(self.heapList, i)
            self.percDown(i)
            i -= 1
        print(self.heapList, i)










