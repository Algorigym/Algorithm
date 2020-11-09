N, M, V = map(int, input().split())

matrix = [[0] * (N + 1) for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visit_list_dfs = [0] * (N + 1)


def dfs(V):
    visit_list_dfs[V] = 1  # 방문한 점 1로 표시
    print(V, end=' ')
    for i in range(1, N + 1):
        if (visit_list_dfs[i] == 0 and matrix[V][i] == 1):
            dfs(i)


visit_list_bfs = [0] * (N + 1)


def bfs(V):
    queue = [V]  # 들려야 할 정점 저장
    visit_list_bfs[V] = 1  # 방문한 점 1로 표시

    while queue:  # []이면 while문이 돌지 않는다.
        V = queue.pop(0)  # 첫 번째 원소 pop
        print(V, end=' ')
        for i in range(1, N + 1):
            if (visit_list_bfs[i] == 0 and matrix[V][i] == 1):
                queue.append(i)
                visit_list_bfs[i] = 1


dfs(V)
print()
bfs(V)
