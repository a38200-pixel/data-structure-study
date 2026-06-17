class Pointer:
    def __init__(self, start_bucket):
        self.bucket = start_bucket  # 현재 검사 중인 해시 주소(버킷 번호)

class HashTable:
    def __init__(self, size):
        self.size = size
        # 빈버킷은 None으로 초기화
        self.table = [None] * self.size

    # 해시 함수: 데이터 값을 버킷 번호로 변환 (가장 기본인 나머지 연산)
    def hash_fn(self, key):
        return key % self.size

    # 삽입
    def insert(self, key):
        # 시작 주소를 계산해서 curr 객체에 저장
        curr = Pointer(self.hash_fn(key))
        start_bucket = curr.bucket # 한 바퀴 돌았는지 체크용
        
        while True:
            # 버킷이 비어있거나, 지워진 버킷('DELETED')이라면 데이터를 넣음
            if self.table[curr.bucket] is None or self.table[curr.bucket] == 'DELETED':
                self.table[curr.bucket] = key
                print(f"-> {key} 삽입 완료! (주소: {curr.bucket})")
                return True
                
            # 버킷이 이미 차 있다면, 다음 버킷으로 한 칸 이동
            curr.bucket = (curr.bucket + 1) % self.size
            
            # 한 바퀴 다 돌았는데도 빈버킷이 없으면 테이블이 full임
            if curr.bucket == start_bucket:
                print("-> 에러: 해시 테이블이 가득 찼습니다!")
                return False

    # 탐색
    def search(self, key):
        curr = Pointer(self.hash_fn(key))
        start_bucket = curr.bucket
        
        while self.table[curr.bucket] is not None:
            # 내가 찾는 값을 발견하면 주소(버킷 번호)를 반환
            if self.table[curr.bucket] == key:
                return curr.bucket
                
            # 다른 값이 있다면 다음 버킷으로 넘어가서 계속 찾습니다.
            curr.bucket = (curr.bucket + 1) % self.size
            
            if curr.bucket == start_bucket:
                break
                
        return -1  # None을 만나거나 한 바퀴 돌 때까지 못 찾으면 -1 반환

    # 삭제
    def delete(self, key):
        # 먼저 탐색 함수를 사용해 그 값이 어느 버킷에 있는지 찾음
        bucket_idx = self.search(key)
        
        if bucket_idx != -1:
            # 길 안끊기게 버킷을 비우는 대신 'DELETED' 남김
            self.table[bucket_idx] = 'DELETED'
            print(f"-> {key} 삭제 완료! (주소: {bucket_idx})")
            return True
            
        print(f"-> 에러: 삭제하려는 {key}가 테이블에 없습니다.")
        return False

    # 출력 함수
    def display(self):
        print("현재 해시 테이블 상태:", self.table)


# --- 테스트 코드 ---
ht = HashTable(7)

print("--- 데이터 삽입 테스트 ---")
ht.insert(10)  # 10 % 7 = 주소 3
ht.insert(20)  # 20 % 7 = 주소 6
ht.insert(17)  # 17 % 7 = 주소 3 (주소 3이 차 있어서 다음 빈버킷인 주소 4로 들어감)
ht.display()

print("\n--- 탐색 테스트 ---")
target = 17
result = ht.search(target)
print(f"{target}은(는) {result}에 있습니다.") # 출력 = 주소 4

print("\n--- 삭제 테스트 ---")
ht.delete(20)
ht.display() # 주소 6번이 'DELETED'로 바뀜

print("\n--- 삭제 후 탐색 테스트 ---")
# 20이 지워진 자리를 지나서 17을 잘 찾는지 확인
result_after = ht.search(17)
