class HashTable:
    def __init__(self):
        self.size = 11  # 散列表的大小应该设置为素数
        # 设置槽的数量
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashFunction(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def put(self, key, data):
        hashvalue = self.hashFunction(key)

        if self.slots[hashvalue] == None:  # key不存在，没有冲突
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:   # key已经存在，替换value
                self.data[hashvalue] = data  # 替换值
            else:  # 散列冲突，再散列，直到找到空槽或者key
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # 替换值

    def get(self, key):
        startslot = self.hashFunction(key)  # 标记散列值为查找起点
        data = None
        stop = False
        found = False
        pos = startslot
        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos] == key:  # 找到了KEY，返回数据
                found = True
                data = self.data[pos]
            else:  # 没有找到KEY, 再散列继续找
                pos = self.rehash(pos)
                if pos == startslot:
                    stop = True  # 回到起点，停，说明KEY不存在
        return data

    # 通过特殊方法实现 [] 访问
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

