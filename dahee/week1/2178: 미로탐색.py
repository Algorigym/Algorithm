n, m = map(float, input().split())
n =

# 미로
maze = []

# 몇번째만에 방문했는지 기록하기 위한 list
v_maze = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    tmp = input()
    row = []
    for c in tmp:
        row.append(int(c))
    maze.append(row)

# BFS를 위한 que
que = []

# 0,0부터 시작
que.append([0, 0])
v_maze[0][0] = 1

while True:

    # que가 빌때까지 수행.
    if len(que) == 0:
        break

    # que는 FIFO
    r, c = que.pop(0)

    # 상하좌우를 검사한다.
    if r-1 >= 0:
        # 갈수 있는 길이면서 한번도 방문하지 않았던곳만 체크.
        if maze[r-1][c] == 1 and v_maze[r-1][c] == 0:
            que.append([r-1, c])
            # 몇번째만에 방문했는지 v_maze에 기록.
            v_maze[r - 1][c] += v_maze[r][c]+1
    if r+1 < len(maze):
        if maze[r+1][c] == 1 and v_maze[r+1][c] == 0:
            que.append([r+1, c])
            v_maze[r + 1][c] = v_maze[r][c]+1
    if c-1 >= 0:
        if maze[r][c-1] == 1 and v_maze[r][c-1] == 0:
            que.append([r, c-1])
            v_maze[r][c-1] = v_maze[r][c]+1
    if c+1 < len(maze[0]):
        if maze[r][c+1] == 1 and v_maze[r][c+1] == 0:
            que.append([r, c+1])
            v_maze[r][c+1] = v_maze[r][c]+1
print(v_maze[(n-1)][(m-1)])

# 출처: https://soojong.tistory.com/entry/알고리즘파이썬-백준-2718-미로탐색 [인생박물관]
