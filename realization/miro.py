import time
import random
import os

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
    print(f"=== [미로 #{maze_num} 탐색 시작] ===")
    print(f"현재 위치: {current_pos}")
    print(f"스택(남은 갈림길): {stack}\n")
    
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
    print("\n" + "="*30)
    time.sleep(0.2)

def solve_multiple_mazes(maze_list):
    for i, maze in enumerate(maze_list):
        # 시작(e)과 끝(x) 찾기
        start, end = None, None
        for r in range(6):
            for c in range(6):
                if maze[r][c] == 'e': start = (r, c)
                if maze[r][c] == 'x': end = (r, c)

        # 시작위치 추가
        stack = [start]
        
        while stack:
            curr = stack.pop()
            r, c = curr
            
            #현재위치가 출구이면 탐색 성공
            if maze[r][c] == 'x':
                display_maze(maze, curr, stack, i+1)
                print(f"\n 미로 #{i+1} 출구 발견")
                break

            # 방문했음 표시 
            if maze[r][c] != 'V':
                if maze[r][c] != 'e': 
                    maze[r][c] = 'V'
                display_maze(maze, curr, stack, i+1)

                # 주변 탐색 및 스택 삽입
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우
                random.shuffle(directions)

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
                        if maze[nr][nc] in ['0', 'x'] and (nr, nc) not in stack:
                            stack.append((nr, nc))
# 실행
solve_multiple_mazes(MAZE_COLLECTION)