class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key  # 键
        self.payload = val  # 数据项
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for e in self.leftChild:
                    yield e
            yield self.key
            if self.hasRightChild():
                for e in self.rightChild:
                    yield e

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent  # 没有父节点的节点就是根结点

    def isLeaf(self):
        return not (self.rightChild and self.leftChild)  # 没有子节点的节点就是叶子节点

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, val, lc, rc):  # 更换节点值: 键，值，左子节点，右子节点，左右子节点的父节点都得是自己
        self.key = key
        self.payload = val
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    # 插入 key
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    # 删除方法，先找到再删掉，找不到则提示错误
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, currentNode):
        # 1 是叶节点，没有子节点， 则直接删除，->删除父节点对它的引用
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        # 2 被删的节点有一个子节点:-> 把这个唯一的子节点上移，替换掉被删节点的位置
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    # 左子节点删除
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    # 右子节点删除
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    # 根结点删除
                    currentNode.replaceNodeData()
            # TODO 代码功能未完成
        # 3 被删的节点有两个子节点：寻找一个合适的节点来替换被删节点的位置。：右子树中最小的一个，即 后继
        pass



    def __delitem__(self, key):
        self.delete(key)


mytree = BinarySearchTree()
mytree[3] = 'red'
mytree[4] = 'blue'
mytree[5] = 'yellow'
mytree[2] = 'at'








