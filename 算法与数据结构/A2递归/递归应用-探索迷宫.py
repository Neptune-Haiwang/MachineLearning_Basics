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








