from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

N: int = int(stdin.readline())

res: list[list[bool]] = [[True for _ in range(N)] for _ in range(N)]

def recursive_drill(x: int, y: int, width: int):
    global res
    removal_x: int = x + width
    removal_y: int = y + width
    for i in range(removal_y, removal_y + width):
        for j in range(removal_x, removal_x + width):
            res[i][j] = False
    
    next_width: int = width // 3
    next_x: int = x
    next_y: int = y
    for i in range(3):
        next_y += width * i
        for j in range(3):
            next_x += width * j
            if res[next_y][next_x]:
                recursive_drill(next_x, next_y, next_width)

recursive_drill(0, 0, N // 3)

for line in res:
    for flag in line:
        print("*" if flag else " ", end="")
    print()
