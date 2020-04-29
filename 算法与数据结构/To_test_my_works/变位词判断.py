'''
问题：'变位词'：两个词之间存在组成字母的重新排列的关系，如 heart | earth, python| typhon
        简化起见，假设参与判断的两个词仅由小写字母构成，且长度相等。

目标：写一个布尔函数，以两个词作为参数，返回这两个词是否为变位词

思路一：逐字符检查：把词1中的字符逐个到词2中检查是否存在，看是否所有字符都能找到即可。
思路二：排序对比: 先转化为列表，然后按字母顺序排序，再对比。
思路三：暴力穷举法：生成S1的所有字符的全排列，再在S2中查看 （N个字符全排列：共有 N! 个可能的字符串个数。）
思路四：计数比较：对比每个词中每个字母的出现次数（设定每个字母的计数器）（ACSII字符码，顺序的），如果26个字母的出现次数一样，则两个一定是变位词
'''

def solution1(s1, s2):
    ''' 时间复杂度：两层嵌套循环  -> O(n^2)
    :param s1:
    :param s2:
    :return:
    '''
    list_s2 = list(s2)  # 把S2单词复制到列表
    p = 0
    still_OK = True  # 标识符
    while p < len(list_s2) and still_OK:
        p2 = 0
        found = False
        while p2 < len(list_s2) and (not found):  # 当没有找到当前字符时
            if s1[p] == list_s2[p2]:  # 在列表中查找字符
                found = True
            else:
                p2 += 1
        if found:
            list_s2[p2] = None  # 找到了字符，则给个None标示一下
        else:
            still_OK = False  # 没找到，则不OK
        p += 1
    return still_OK

def solution2(s1, s2):
    '''时间复杂度：一个循环 O(n), 但两个sort()排序是大约O(nlogn) -> O(nlogn)
    :param s1:
    :param s2:
    :return:
    '''
    list1 = list(s1)
    list2 = list(s2)
    list1.sort()
    list2.sort()
    p = 0
    match = True
    while p < len(s1) and match:
        if list1[p] == list2[p]:
            p += 1
        else:
            match = False
    return match




if __name__=='__main__':
    # print(solution1('heart', 'earth'))
    print(solution2('heart', 'earth'))
