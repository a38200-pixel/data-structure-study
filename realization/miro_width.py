import copy
import os
import sys
import time
from collections import deque


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


MAZE_COLLECTION = [
    [
        ['1', '1', '1', '1', '1', '1'],
        ['e', '0', '1', '0', '0', '1'],
        ['1', '0', '0', '0', '1', '1'],
        ['1', '1', '1', '0', '1', '1'],
        ['1', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '0', '1'],
        ['1', '1', '1', '1', 'x', '1']
    ],
    [
        ['1', '1', '1', '1', '1', '1'],
        ['e', '0', '1', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '0', '1'],
        ['1', '0', '0', '1', '0', '1'],
        ['1', '0', '1', '1', '0', '1'],
        ['1', '1', '1', '1', 'x', '1']
    ],
    [
        ['1', '1', '1', '1', '1', '1'],
        ['e', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '0', '1'],
        ['1', '0', '0', '1', '0', '1'],
        ['1', '1', '0', '1', '0', '1'],
        ['1', '0', '0', '1', '0', '1'],
        ['1', '1', '1', '1', 'x', '1']
    ]
]


def find_start_and_exit(maze):
    start, exit_pos = None, None

    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'e':
                start = (r, c)
            elif maze[r][c] == 'x':
                exit_pos = (r, c)

    return start, exit_pos


def display_maze(maze, current_pos, queue, maze_num):
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"=== [미로 #{maze_num} 너비우선 탐색 시작] ===")
    print(f"현재 위치: {current_pos}")
    print(f"큐(다음 후보): {list(queue)}\n")

    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if (r, c) == current_pos:
                print("🐭", end=" ")
            elif maze[r][c] == 'V':
                print("✔️ ", end=" ")
            elif maze[r][c] == '1':
                print("🧱", end=" ")
            elif maze[r][c] == 'e':
                print("🏠", end=" ")
            elif maze[r][c] == 'x':
                print("🚩", end=" ")
            else:
                print("  ", end=" ")
        print()

    print("\n" + "=" * 30)
    time.sleep(0.2)


def solve_multiple_mazes_bfs(maze_list):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i, original_maze in enumerate(maze_list, start=1):
        maze = copy.deepcopy(original_maze)
        start, exit_pos = find_start_and_exit(maze)

        if start is None or exit_pos is None:
            print(f"미로 #{i}: 시작점 또는 출구를 찾을 수 없습니다.")
            continue

        queue = deque([start])
        visited = {start}
        parent = {start: None}

        while queue:
            curr = queue.popleft()
            r, c = curr

            if maze[r][c] == 'x':
                display_maze(maze, curr, queue, i)
                path = make_path(parent, curr)
                print(f"\n미로 #{i} 출구 발견!")
                print(f"최단 경로 길이: {len(path) - 1}")
                print(f"경로: {path}")
                time.sleep(1)
                break

            if maze[r][c] != 'e':
                maze[r][c] = 'V'

            display_maze(maze, curr, queue, i)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                next_pos = (nr, nc)

                if not (0 <= nr < len(maze) and 0 <= nc < len(maze[0])):
                    continue

                if maze[nr][nc] not in ['0', 'x']:
                    continue

                if next_pos in visited:
                    continue

                visited.add(next_pos)
                parent[next_pos] = curr
                queue.append(next_pos)
        else:
            print(f"\n미로 #{i}: 출구를 찾지 못했습니다.")
            time.sleep(1)


def make_path(parent, end):
    path = []
    curr = end

    while curr is not None:
        path.append(curr)
        curr = parent[curr]

    path.reverse()
    return path


solve_multiple_mazes_bfs(MAZE_COLLECTION)
