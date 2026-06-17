def selection_sort(arr):
    arr = arr[:]

    for i in range(len(arr) - 1):
        least = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[least]:
                least = j

        arr[i], arr[least] = arr[least], arr[i]

    return arr


def insertion_sort(arr):
    arr = arr[:]

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def bubble_sort(arr):
    arr = arr[:]

    for i in range(len(arr) - 1, 0, -1):
        changed = False

        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                changed = True

        if not changed:
            break

    return arr


def binary_search(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    print("선택 정렬:", selection_sort(data))
    print("삽입 정렬:", insertion_sort(data))
    print("버블 정렬:", bubble_sort(data))

    sorted_data = selection_sort(data)
    print("이진 탐색 6:", binary_search(sorted_data, 6))
