import time
import os
import copy

MAZE_COLLECTION = [
    # 미로 1
    [
        ['1', '1', '1', '1', '1', '1'],
        ['e', '0', '1', '0', '0', '1'],
        ['1', '0', '0', '0', '1', '1'],
        ['1', '1', '1', '0', '1', '1'],
        ['1', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '0', '1'],
        ['1', '1', '1', '1', 'x', '1']
    ],
    # 미로 2
    [
        ['1', '1', '1', '1', '1', '1'],
        ['e', '0', '1', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '0', '1'],
        ['1', '0', '0', '1', '0', '1'],
        ['1', '0', '1', '1', '0', '1'],
        ['1', '1', '1', '1', 'x', '1']
    ],
    # 미로 3
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


def display_maze(maze, current_pos, stack, maze_num):
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"=== [미로 #{maze_num} 전략적 탐색 시작] ===")
    print(f"현재 위치: {current_pos}")
    print(f"스택(남은 후보): {stack}\n")

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


def manhattan_distance(pos, end):
    
    # 현재 위치 pos에서 출구 end까지의 거리 계산
    # 거리 = 행 차이 + 열 차이
    return abs(pos[0] - end[0]) + abs(pos[1] - end[1])


def solve_multiple_mazes_strategic(maze_list):
    for i, original_maze in enumerate(maze_list):
        # 원본 미로가 훼손되지 않도록 복사
        maze = copy.deepcopy(original_maze)

        start, end = None, None

        # 시작점 e와 출구 x 찾기
        for r in range(len(maze)):
            for c in range(len(maze[0])):
                if maze[r][c] == 'e':
                    start = (r, c)
                elif maze[r][c] == 'x':
                    end = (r, c)

        if start is None or end is None:
            print(f"미로 #{i + 1}: 시작점 또는 출구를 찾을 수 없습니다.")
            continue

        stack = [start]
        visited = set()

        while stack:
            curr = stack.pop()
            r, c = curr

            # 이미 방문한 곳이면 건너뜀
            if curr in visited:
                continue

            visited.add(curr)

            # 현재 위치가 출구이면 성공
            if maze[r][c] == 'x':
                display_maze(maze, curr, stack, i + 1)
                print(f"\n미로 #{i + 1} 출구 발견!")
                time.sleep(1)
                break

            # 방문 표시
            if maze[r][c] != 'e':
                maze[r][c] = 'V'

            display_maze(maze, curr, stack, i + 1)

            # 상, 하, 좌, 우
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            candidates = []

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                next_pos = (nr, nc)

                if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
                    if maze[nr][nc] in ['0', 'x'] and next_pos not in visited:
                        distance = manhattan_distance(next_pos, end)
                        candidates.append((distance, next_pos))

            # 출구와 가까운 칸이 우선순위가 높음
            candidates.sort(reverse=True)

            # stack은 마지막에 들어간 것이 먼저 나오므로
            # 가까운 칸이 마지막에 들어가도록 reverse=True 사용
            for distance, next_pos in candidates:
                if next_pos not in stack:
                    stack.append(next_pos)

        else:
            print(f"\n미로 #{i + 1}: 출구를 찾지 못했습니다.")
            time.sleep(1)


# 실행
solve_multiple_mazes_strategic(MAZE_COLLECTION)