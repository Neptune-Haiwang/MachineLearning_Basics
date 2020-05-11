'''探索迷宫
把迷宫分成行列整齐的方格，区分出墙壁和通道。
即每个方格都有行列位置：矩阵，
采用不同字符来分别代表：墙壁，通道，海龟投放点

'''


class Maze:
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsMaze = 0
        self.mazeList = []
        mazeFile = open(mazeFileName, 'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[: -1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col += 1
            rowsInMaze += 1
            self.mazeList.append(rowList)
            columnsMaze = len(rowList)


def searchFrom(maze, startRow, startColumn):
    # 1.1 碰到墙壁，返回失败
    maze.updatePosition(startRow, startColumn)
    if maze[startRow][startColumn] == OBSTACLE:
        return False
    # 1.2 碰到面包屑（已尝试走过的可以走的点），或者死胡同，返回失败
    if (maze[startRow][startColumn] == TRIED) or (maze[startRow][startColumn] == DEAD_END):
        return False
    # 1.3 碰到了出口， 返回成功
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    # 1.4 撒一下面包屑，继续探索
    maze.updatePosition(startRow, startColumn, TRIED)
    # 2.1 向北南西东四个方向依次探索，OR操作有短路效应（即一个为TRUE,则后续的不管是啥，结果都为TRUE）
    found = searchFrom(maze, startRow-1, startColumn) or searchFrom(maze, startRow+1, startColumn) or \
            searchFrom(maze, startRow, startColumn-1) or searchFrom(maze, startRow, startColumn+1)
    # 2.2 如果探索成功则标记为当前点，否则标记为死胡同
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found







