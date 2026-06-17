# 1. 스택 클래스 정의
class CustomStack:
    def __init__(self):
        self.stack = []

    # [add] 데이터 추가하기 (맨 위에 쌓기)
    def add(self, element):
        self.stack.append(element)
        print(f"-> {element} 데이터가 추가 되었습니다.")

    # [pop] 데이터 꺼내기 (맨 위에서 빼기)
    def pop(self):
        # 스택이 비어있는지 먼저 확인해야 에러가 안 납니다.
        if len(self.stack) == 0:
            print("스택이 비어있어 데이터를 꺼낼 수 없습니다.")
            return None
        
        # 리스트의 맨 마지막 원소를 제거하면서 가져옵니다.
        target = self.stack.pop()
        print(f"-> {target} 데이터가 pop 되었습니다.")
        return target

    # [peek] 맨 위 데이터 확인
    def peek(self):
        if len(self.stack) == 0:
            return None
        
        # 리스트의 마지막 인덱스([-1])를 조회.
        return self.stack[-1]


# --- 테스트 코드 ---

my_stack = CustomStack()
print("초기 스택 :", my_stack.stack)

my_stack.add(10)
my_stack.add(20)
my_stack.add(30)
print("현재 스택 :", my_stack.stack)

# 맨 위에 뭐가 있는지 확인
print(f"peek: {my_stack.peek()}")

# Pop
print(f"Pop 된 데이터: {my_stack.pop()}") # 30
print(f"Pop 된 데이터: {my_stack.pop()}") # 20
print("Pop 한 후 스택 상태:", my_stack.stack) # [10]만 남아있음