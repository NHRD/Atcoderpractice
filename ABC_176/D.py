h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
maze = []

for i in range(0, h):
    s = list(map(str, input().split()))
    maze.append(s)
    s = []

#print(maze)

i = ch
j = cw