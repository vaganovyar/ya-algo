arr = list(map(int, input().split()))
n = len(arr)
for i in range(n - 1):
    max_num = arr[0]
    max_pos = 0
    for j in range(n - i):
        if arr[j] > max_num:
            max_num = arr[j]
            max_pos = j
    arr[max_pos], arr[n - i - 1] = arr[n - i - 1], arr[max_pos]

print(*arr)
