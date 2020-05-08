def moveDisk(disk, fromPole, toPole):
    print(f'Moving disk[{disk}] from {fromPole} to {toPole}')


#               高度，  开始柱，   中间柱，   目标柱
def moveTower(height, fromPole, withPole, toPole):
    if height >= 1:
        moveTower(height-1, fromPole, toPole, withPole)
        moveDisk(height, fromPole, toPole)
        moveTower(height-1, withPole, fromPole, toPole)

moveTower(3, '#1', '#2', '#3')










