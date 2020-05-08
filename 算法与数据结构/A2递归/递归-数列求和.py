'''
问题：给定一个列表，返回所有数的和

'''

list1 = [1,3,5,7,8,9,2,4,6,7,8,90,0,2]

# 1 常规的循环累加求和
def listSum(numList):
    theSum = 0
    for i in numList:
        theSum += i
    return theSum

print(listSum(list1))

# 2 递归求和 （全括号排列）
# 求和是由一次次加法实现的，而加法有两个操作数
'''
    1 + 3 + 5 + 7 + 4
    = 1 + （3 + （5 + （7 + 4）））
    = 1 + （3 + （5 + 11）） 
    = 1 + （3 + 16）
    = 1 + 19
    = 20
'''

'''
递归函数的调用过程
sum(1,3,5,7) = 1 + sum(3,5,7) = 1 + sum(3 + sum(5,7)) = 1 + sum(3 + sum(5 + sum(7)))
递归函数的返回过程
    = 1 + sum(3 + sum(5 + sum(7)))
    = 1 + sum(3 + sum(5 + 7))
    = 1 + sum(3 + 12)
    = 1 + 15
    = 16
'''

# 问题 分解成相同问题，规模更小：数列的和 = '首个数' + '余下数列'的和
# listSum(list1) = first(list1) + listSum(rest(list1))
def listsum_recrusion(numList):
    # 最小规模
    if len(numList) == 1:
        return numList[0]
    # 减小规模
    else:
        #                   调用自身
        return numList[0] + listsum_recrusion(numList[1:])

print(listsum_recrusion(list1))






