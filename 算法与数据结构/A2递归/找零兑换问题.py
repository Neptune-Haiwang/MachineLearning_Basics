# 找零兑换问题：递归解法代码
def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:  # 最小规模，直接返回
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)  # 减小规模，每次减去一种一个硬币面值
            if numCoins < minCoins:  # 挑选最小数量
                minCoins = numCoins
    return minCoins

# 找零兑换问题：递归解法改进
def recMC_adv(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:  # 最小规模，直接返回
        knownResults[change] = 1  # 记录最优解
        return 1
    elif knownResults[change] > 0:  # 等于0 说明是没有计算，64个位置都是0，大于0说明之前已经计算过了
        return knownResults[change]  # 查表成功，直接返回最优解
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC_adv(coinValueList, change-i, knownResults)  # 减小规模，每次减去一种一个硬币面值
            if numCoins < minCoins:  # 挑选最小数量
                minCoins = numCoins
                # 找到最优解，记录到表中
                knownResults[change] = minCoins
    return minCoins

# 找零兑换问题：动态规划
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    # 从一分开始到change逐个计算最少硬币数
    for cents in range(1, change+1):
        # 初始化一个最大值
        coinCount = cents
        newCoin = 1
        # 减去每个硬币，向后查找最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        # 得到当前最少硬币数，并记录在表中
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    # 返回最后一个结果
    return minCoins[change]

def printcoins(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin -= thisCoin



if __name__=="__main__":
    coinValueList = [1, 5, 10, 15, 21, 25]
    memo = [0] * 64
    amount = 63
    coinUsed = [0] * (amount + 1)
    coinCount = [0] * (amount + 1)

    # print(recMC(coinValueList, 63))
    # print(recMC_adv(coinValueList, 63, memo))
    print(dpMakeChange(coinValueList, amount, coinCount, coinUsed))
    printcoins(coinUsed, amount)






