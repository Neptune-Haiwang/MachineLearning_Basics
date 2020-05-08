import turtle
t = turtle.Turtle()

# 绘制等边三角形
def drawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()

# 取两个点的中点
def getMid(p1, p2):
    center_pos = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    return center_pos

def sierpinski(degree, points):
    colormaps = ['blue', 'red', 'green', 'white', 'yellow', 'orange']
    drawTriangle(points, colormaps[degree])  # 等边三角形
    if degree > 0:
        '''
        大三角的顶点：left, top, right
        左边小三角的顶点：left, (left&top的中点), (left&right的中点)
        上边小三角的顶点：(left&top的中点), top, (top&right的中点)
        右边小三角的顶点：(left&right的中点), (top&right的中点), right
        '''
        sierpinski((degree - 1),
                   {'left': points['left'],
                    'top': getMid(points['left'], points['top']),
                    'right': getMid(points['left'], points['right'])})
        sierpinski((degree - 1),
                   {'left': getMid(points['left'], points['top']),
                    'top': points['top'],
                    'right': getMid(points['top'], points['right'])})
        sierpinski((degree - 1),
                   {'left':  getMid(points['left'], points['right']),
                    'top': getMid(points['top'], points['right']),
                    'right': points['right']})

def drawSierpinski():
    #  大三角的三个顶点坐标
    points = {'left': (-200, -100),
              'top': (0, 200),
              'right': (200, -100)}
    # 画degree为5的三角形
    sierpinski(degree=3, points=points)

drawSierpinski()

t.hideturtle()
turtle.done()
