import turtle
# 1 创建对象
t = turtle.Turtle()


# 递归作图：五角星
def drawPentagram(t):
    t.pencolor('red')
    t.pensize(3)
    for i in range(5):
        t.forward(100)  # 海龟向前走100步
        t.right(144)  # 海龟向右转144度
    t.hideturtle()

# 递归作图：螺旋
def drawSprial(t, lineLen):
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        drawSprial(t, lineLen-5)

# 递归作图：画二叉树
def tree(t, branch_len):
    if branch_len > 5:  # 树干太短不画，即递归结束条件
        t.forward(branch_len)  # 画树干
        t.right(20)  # 右倾斜20度
        tree(t, (branch_len - 15))  # 递归调用， 画右边的小树，树干-15
        t.left(40)  # 向左旋转40度，即此时是左倾斜20度
        tree(t, (branch_len - 15))  # 递归调用， 画左边的小树，树干-15
        t.right(20)  # 向右旋转20度，即回正
        t.backward(branch_len)  # 海龟退回原位置

def drawTree(t):
    t.left(90)
    t.penup()
    t.backward(100)
    t.pendown()
    t.pencolor('green')
    t.pensize(2)
    tree(t, 75)  # 画 树干长度为75 的二叉树
    t.hideturtle()


# 2 画图函数调用
# drawPentagram(t)
# drawSprial(t, 100)
drawTree(t)


# 3 作图结束
turtle.done()

