def find_path_dfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    stack = [start]
    visited = set()
    parent = {start: None}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        current = stack.pop()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        if current in visited:
            continue

        visited.add(current)
        r, c = current

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            next_pos = (nr, nc)

            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] == 0 and next_pos not in visited:
                    stack.append(next_pos)
                    if next_pos not in parent:
                        parent[next_pos] = current

    return None


if __name__ == "__main__":
    # 0: 이동 가능, 1: 벽
    maze = [
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
    ]

    path = find_path_dfs(maze, (0, 0), (3, 3))
    print("DFS 경로:", path)
