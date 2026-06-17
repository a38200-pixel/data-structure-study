class CustomSet:
    def __init__(self, set_A, set_B):
        self.set_A = set_A
        self.set_B = set_B

    # 합집합 구하기
    def get_union(self):
        union_result = []
        
        # 먼저 A의 모든 원소를 결과에 넣습니다.
        for element in self.set_A:
            union_result.append(element)

        # 결과에 없는 것만 넣음
        for element in self.set_B:
            if element not in union_result:
                union_result.append(element)
                
        return union_result

    # 교집합 구하기
    def get_intersection(self):
        intersection_result = []
        
        # B에도 들어있는지 확인하고 넣음
        for element in self.set_A:
            if element in self.set_B:
                intersection_result.append(element)
                
        return intersection_result

    # 차집합 구하기
    def get_difference(self):
        difference_result = []
        
        #  B에는 없는 것만 넣음
        for element in self.set_A:
            if element not in self.set_B:
                difference_result.append(element)
                
        return difference_result


# --- 테스트 코드 ---

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]

my_set = CustomSet(list_1, list_2)

print(f"집합 A: {my_set.set_A}")
print(f"집합 B: {my_set.set_B}")
print("-" * 30)
print(f"합집합 결과: {my_set.get_union()}")
print(f"교집합 결과: {my_set.get_intersection()}")
print(f"차집합 결과: {my_set.get_difference()}")