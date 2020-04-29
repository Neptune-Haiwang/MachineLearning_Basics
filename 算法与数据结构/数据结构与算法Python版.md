数据结构与算法Python版 https://www.bilibili.com/video/BV1h7411m7BK?p=8
原视频来源   https://www.icourse163.org/course/0809PKU068-1206307812
# 算法的时间复杂度与空间复杂度分析 
## 时间复杂度 -> Big O Notation
    - 常数 1
    - 对数 log(n)
    - 线性 n
    - 对数线性 n * log(n)
    - 平方 n^2
    - 立方 n^3
    - 指数 2^n
    - 阶乘 n! 比 指数 2^n 还耗时间
- 时间与空间的复杂度需要一个平衡与取舍
## python数据类型的性能
    - list与dict对比的操作：
                   list                             dict     
        索引      自然数i                          不可变类型值key
        添加      append, extend, insert          b[k] = v
        删除      pop, remove                     pop
        更新      a[i] = v                        b[k] = v
        正查      a[i], a[i: j]                   b[k], copy
        反查      index[v], count(v)              无
        其他      reverse, sort                   has_key, update
### list列表 -> 执行时间随着列表的规模增大而线性上升
    - 四种生成前N个整数列表的方法
        * 循环列表连接： （运行速度最慢）
                a = []
                for i in range(1000):
                    a = a + [i]
        * append追加元素：（运行速度一般）
                a = []
                for i in range(1000):
                    a = a.append(i)
        * 列表推导式：（运行速度较快）
                a = [i for i in range(1000)]
        * range函数转列表：（运行速度最快）
                a = list(range(1000))
### dict字典 -> 执行时间与规模无关，是常数

# 线性结构：栈stack，队列queue，双端队列deque，列表list
## 什么是线性结构
    - 线性结构定义：一种有序数据项的集合，其中每个数据都有唯一的前驱和后继（第一个没有前驱，最后一个没有后继）
    - 不同的线性结构的区别在于数据项的增减方式
## 栈stack
- 只在栈顶进行添加移除操作，后进先出LIFO
- 栈的特性：反转次序：例如浏览器的后退操作，最先back的是刚刚访问的网页，再一步一步向后退。
- 栈的常见操作：
    Stack(): 创建空栈
    push(item): 添加元素item
    pop(): 移除栈顶元素，并返回，修改原栈
    peek(): 查看栈顶元素，并返回，不修改原栈
    isEmpty(): 判断栈是否为空
    size(): 返回栈中元素个数
### 栈的应用: 括号匹配的校验操作
- 括号匹配算法：第一个左括号（最早打开），就应该匹配最后一个右括号（最后遇到），次序反转的识别， 符合栈的特性






