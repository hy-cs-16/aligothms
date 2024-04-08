graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9


from collections import deque


def bfs(_graph, q: deque, _visited):
    if len(q) == 0:
        return

    top = q.popleft()
    print(top, end=" ")

    for i in graph[top]:
        if not visited[i]:
            q.append(i)
            visited[i] = True

    bfs(_graph, q, deque)

def bfs2(_graph, start, _visited):
    _queue = deque([start])
    _visited[start] = True

    while len(_queue) != 0:
        top = _queue.popleft()
        print(top, end=' ')

        for i in _graph[top]:
            if not _visited[i]:
                _queue.append(i)
                _visited[i] = True


bfs2(graph, 1, visited.copy())

queue = deque()
queue.append(1)
visited[1] = True
bfs(graph, queue, visited.copy())

