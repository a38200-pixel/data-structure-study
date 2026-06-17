class ArrayList:
    def __init__(self):
        self.MAX_SIZE = 10
        self.items = [None] * self.MAX_SIZE  
        self.length = 0

    # Insert(pos, e): pos 위치에 새로운 요소 e를 삽입
    def Insert(self, pos, e):
        if not self.IsFull() and 0 <= pos <= self.length:
            for i in range(self.length, pos, -1):
                self.items[i] = self.items[i-1]
            self.items[pos] = e
            self.length += 1
        else:
            print("Error: Invalid Position or List Full")

    # Delete(pos): pos 위치에 있는 요소를 꺼내고(삭제) 반환
    def Delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.length:
            item = self.items[pos]
            for i in range(pos, self.length - 1):
                self.items[i] = self.items[i+1]
            self.items[self.length - 1] = None
            self.length -= 1
            return item
        return None

    # isEmpty(): 리스트가 비어 있는지 검사
    def isEmpty(self):
        return self.length == 0

    # IsFull(): 리스트가 가득 차 있는지 검사
    def IsFull(self):
        return self.length == self.MAX_SIZE

    # getEntry(pos): pos 위치에 있는 요소를 반환
    def getEntry(self, pos):
        if 0 <= pos < self.length:
            return self.items[pos]
        return None

    # Size(): 리스트 안의 요소의 개수를 반환
    def Size(self):
        return self.length

    # Clear(): 리스트를 초기화
    def Clear(self):
        self.items = [None] * self.MAX_SIZE
        self.length = 0

    # Find(item): 리스트에서 item이 있는지 찾아 인덱스를 반환
    def Find(self, item):
        for i in range(self.length):
            if self.items[i] == item:
                return i
        return -1

    # Replace(pos, item): pos에 있는 항목을 item으로 바꿈
    def Replace(self, pos, item):
        if 0 <= pos < self.length:
            self.items[pos] = item

    # Sort(): 리스트의 항목들을 정렬
    def Sort(self):
        # 선택 정렬 방식 사용
        for i in range(self.length - 1):
            least = i
            for j in range(i + 1, self.length):
                if self.items[j] < self.items[least]:
                    least = j
            self.items[i], self.items[least] = self.items[least], self.items[i]

    # Merge(lst): 다른 리스트 lst를 리스트에 추가
    def Merge(self, lst):
        # lst는 ArrayList 객체라고 가정
        for i in range(lst.Size()):
            self.Append(lst.getEntry(i))

    # Display(): 리스트를 화면에 출력
    def Display(self):
        print("[", end="")
        for i in range(self.length):
            print(self.items[i], end=", " if i < self.length-1 else "")
        print("]")

    # Append(e): 리스트의 맨 뒤에 새로운 항목을 추가
    def Append(self, e):
        if not self.IsFull():
            self.items[self.length] = e
            self.length += 1
        else:
            print("Error: List Full")

# 테스트
L = ArrayList()
L2 = ArrayList() # Merge 테스트용 추가 리스트

print("--- Append로 데이터 채우기 ---")
L.Append(10)
L.Append(30)
L.Append(20)
L.Display() # 12번 Display

print("\n--- Insert 및 Delete 테스트 ---")
L.Insert(1, 15) # 1번 위치에 15 삽입 -> [10, 15, 30, 20]
print("1번 위치에 15 삽입 후:", end=" ")
L.Display()

deleted = L.Delete(2) # 2번 위치(30) 삭제 -> [10, 15, 20]
print(f"2번 위치 삭제된 값: {deleted}, 삭제 후:", end=" ")
L.Display()

print("\n--- isEmpty 및 IsFull 테스트 ---")
print(f"리스트가 빔? : {L.isEmpty()}")
print(f"리스트가 가득 참? : {L.IsFull()}")

print("\n--- getEntry 및 Size 테스트 ---")
print(f"1번 위치의 요소는? : {L.getEntry(1)}")
print(f"현재 리스트의 크기는? : {L.Size()}")

print("\n--- Find 및 Replace 테스트 ---")
idx = L.Find(20)
print(f"값 20이 있는 인덱스: {idx}")
L.Replace(idx, 25) # 20을 25로 교체
print("20을 25로 교체 후:", end=" ")
L.Display()

print("\n--- Sort(정렬) 테스트 ---")
L.Append(5)  # [10, 15, 25, 5]
print("정렬 전:", end=" ")
L.Display()
L.Sort()
print("정렬 후:", end=" ")
L.Display()

print("\n--- Merge(합치기) 테스트 ---")
L2.Append(100)
L2.Append(200)
print("합칠 리스트 L2:", end=" ")
L2.Display()
L.Merge(L2)
print("L2를 합친 후 L:", end=" ")
L.Display()

print("\n--- Clear(초기화) 테스트 ---")
L.Clear()
print("Clear 실행 후 Size:", L.Size())
L.Display()