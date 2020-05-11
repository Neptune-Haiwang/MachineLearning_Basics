# 冒泡排序 bubble sort：发现大的就逆序交换
def bubbleSort(aList):
    for passnum in range(len(aList)-1, 0, -1):  # 比对次数从N-1开始减小，到1为止
        for i in range(passnum):
            if aList[i] > aList[i+1]:
                # temp = aList[i]
                # aList[i] = aList[i+1]
                # aList[i+1] = temp
                # python也支持直接交换
                aList[i], aList[i+1] = aList[i+1], aList[i]
    print(aList)

# 选择排序 selection sort: 每次迭代找到最大项的为止，然后循环完了再把本轮的最大项移到最后
def selectionSrt(aList):
    for fillslot in range(len(aList)-1, 0, -1):
        pos_of_max = 0
        for p in range(1, fillslot+1):
            if aList[p] > aList[pos_of_max]:
                pos_of_max = p
        temp = aList[fillslot]
        aList[fillslot] = aList[pos_of_max]
        aList[pos_of_max] = temp
    print(aList)

# 插入排序 insertion sort: 维持一个前半部分排序好的小列表然后扩展到全表，寻找新项的插入位置
def insertionSort(aList):
    for index in range(1, len(aList)):
        currentValue = aList[index]  # 新项/插入项
        pos = index
        while pos > 0 and aList[pos-1] > currentValue:
            aList[pos] = aList[pos-1]
            pos -= 1
        aList[pos] = currentValue  # 插入新项
    print(aList)

def getInsertionSort(aList, start, gap):
    for index in range(start+gap, len(aList), gap):
        currentValue = aList[index]  # 新项/插入项
        pos = index
        while pos >= gap and aList[pos-gap] > currentValue:
            aList[pos] = aList[pos-gap]
            pos -= gap
        aList[pos] = currentValue  # 插入新项

# 希尔排序shell sort: 以插入排序为基础，对无序表进行'间隔'划分子列表，每个子列表都进行插入排序
def shellSort(aList):
    sublistcount = len(aList) // 2
    while sublistcount > 0:
        for start in range(sublistcount):
            getInsertionSort(aList, start, sublistcount)
        print('After increments of size ', sublistcount, ', the list is: ', aList)
        sublistcount //= 2

# 归并排序 merge sort：递归算法，分成两半缩小规模，对两半再归并排序
def mergeSort_old(aList):
    if len(aList) > 1:
        mid = len(aList) // 2
        left = aList[ : mid]
        right = aList[mid: ]
        # 递归调用
        mergeSort_old(left)
        mergeSort_old(right)

        i = j = k = 0
        # 拉链式交错 把左右部分从小到大归并到结果列表中
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                aList[k] = left[i]
                i += 1
            else:
                aList[k] = right[j]
                j += 1
            k += 1
        # 归并左半部分剩余项
        while i < len(left):
            aList[k] = left[i]
            i += 1
            k += 1
        # 归并右半部分剩余项
        while j < len(right):
            aList[k] = right[j]
            j += 1
            k += 1
    return aList

# 归并排序 merge sort 新的python版本到算法：
def mergeSort_python(aList):
    if len(aList) <= 1:  # 递归的基本结束条件
        return aList
    # 分解问题，递归调用
    mid = len(aList) // 2
    left = mergeSort_python(aList[: mid])  # 左边排序
    right = mergeSort_python(aList[mid:])  # 右边排序
    # 合并左右半部，完成排序
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged

# 快速排序quick sort：依据一个中间值，数据分成两半，先分解再排序， 递归
def partition(aList, first, last):
    pass

def quickSort_helper(aList, first, last):
    if first < last:
        splitpoint = partition(aList, first, last)
        quickSort_helper(aList, first, splitpoint-1)
        quickSort_helper(aList, splitpoint+1, last)

def quickSort(aList):
    quickSort_helper(aList, 0, len(aList)-1)
    print(aList)


if __name__=="__main__":
    unorderedTestList = [5, 1, 2, 38, 57, 153, 8, 0, 9, 100, 172, 127, 10, 23, 42, 8, 17]

    bubbleSort(unorderedTestList)
    selectionSrt(unorderedTestList)
    insertionSort(unorderedTestList)
    print('+' * 50)

    shellSort(unorderedTestList)
    print('+' * 50)

    print(mergeSort_old(unorderedTestList))
    print(mergeSort_python(unorderedTestList))
    print('+' * 50)
    # quickSort(unorderedTestList)
