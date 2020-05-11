# 顺序查找：无序表, 算法复杂度O(n)
def sequentialSearch(aList, item):
    pos = 0
    found = False
    while pos < len(aList) and not found:
        if aList[pos] == item:
            found = True
        else:
            pos += 1  # 下标顺序增长
    return found

# 顺序查找：有序表, 算法复杂度O(n)
def orderedSequentialSearch(aList, item):
    pos = 0
    found = False
    stop = False
    while pos < len(aList) and not found and not stop:
        if aList[pos] == item:
            found = True
        else:
            if aList[pos] > item:
                # 排序好的表，此时获取到的值大于目标值，则停止查找
                stop = True
            else:
                pos += 1  # 下标顺序增长
    return found

# 二分查找：有序表, 算法复杂度O(log n)
def binarySearch(aList, item):
    first = 0
    last = len(aList) - 1
    found = False
    while first <= last and not found:
        mid_point = (first + last) // 2  # 求商，去余数
        if aList[mid_point] == item:  # 比对中间项
            found = True
        else:  # 缩小对比范围
            if item < aList[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1
    return found

# 二分查找：有序表, 递归解法
def binarySearch_Recrusion(aList, item):
    if len(aList) == 0:
        return False  # 结束条件
    else:
        mid_point = len(aList) // 2
        if aList[mid_point] == item:
            return True
        else:
            if item < aList[mid_point]:
                return binarySearch_Recrusion(aList[ :mid_point], item)
            else:
                return binarySearch_Recrusion(aList[mid_point+1: ], item)


if __name__ == '__main__':
    unorderedTestList = [5, 1, 2, 38, 57, 153, 8, 0, 9, 10, 23, 42, 8, 17]
    orderedList = [0, 1, 2, 3, 6, 8, 12, 17, 19, 32, 74, 88, 89, 100, 112]

    # print(sequentialSearch(unorderedTestList, 23))
    # print(sequentialSearch(unorderedTestList, 13))
    # print('+' * 20)
    # print(orderedSequentialSearch(orderedList, 17))

    print(binarySearch(orderedList, 17))
    print(binarySearch_Recrusion(orderedList, 17))
