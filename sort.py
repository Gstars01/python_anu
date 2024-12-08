def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        print(f"{i}번째 회전")
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # 요소를 교환합니다.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
            else:
                print("변환 없음")
        print("\n\n")

    return arr

print(bubble_sort([5, 2, 9, 1, 5, 6]))
