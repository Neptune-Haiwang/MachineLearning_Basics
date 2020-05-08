数据结构与算法Python版 https://www.bilibili.com/video/BV1h7411m7BK?p=8
原视频来源   https://www.icourse163.org/course/0809PKU068-1206307812
# 1 算法的时间复杂度与空间复杂度分析 
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

# 2 python基础数据类型的性能
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

# 3 线性结构：栈stack，队列queue，双端队列deque，列表list
## 什么是线性结构
    - 线性结构定义：一种有序数据项的集合，其中每个数据都有唯一的前驱和后继（第一个没有前驱，最后一个没有后继）
    - 不同的线性结构的区别在于数据项的增减方式
## 3.1 栈stack ->代码实现> myStack.py
    - 只在栈顶进行添加移除操作，（后进先出LIFO）
    - 栈的应用：反转次序：浏览器回退操作，最先back的是刚刚访问的网页，再一步一步向后退。；进制转换
    - 栈的常见操作：
        Stack(): 创建空栈
        push(item): 添加元素item
        pop(): 移除栈顶元素，并返回，修改原栈
        peek(): 查看栈顶元素，并返回，不修改原栈
        isEmpty(): 判断栈是否为空
        size(): 返回栈中元素个数
## 3.2 队列queue ->代码实现> myQueue.py
    - 队列是一种有次序的数据集合，新数据在队尾加入，移除数据总是在队首移除（先进先出FIFO）
    - 队列的应用：打印机打印任务；计算机中进程调度；键盘缓冲
## 3.3 双端队列deque ->代码实现> myDeque.py
    - 数据从两端都可以添加与删除

# 4 递归recrusion 
    - 把某个问题分解成规模更小的相同问题，然后在算法中调用自身来完成。
    - 递归三定律：
        * 必须有一个最基本的结束条件 -> 最小规模问题的直接解决
        * 必须能改变状态向基本条件演进 -> 减小问题规模
        * 必须调用自身 -> 解决减小了规模的相同问题
## 递归可视化 
    - python内置的turtle海龟作图系统
        - 意象是模拟海龟在沙滩上爬行而留下的足迹
            forward(n); backward(n)  # 用来爬行：划线
            left(a); right(a)  # 用来转向：旋转一定角度
            penup(); pendown()   # 抬笔，放笔
            pensize(s); pencolor(c)  # 笔属性：划的线的一些属性设置
### 分形fractal树: 
    - 整体与部分是相似的，自相似：如雪花，树，云朵，山脉，海岸线



B站：探索迷宫 06：03






