arr = list(map(int, input().split()))
n = len(arr)
for i in range(n):
    place = 0
    while place < i and arr[place] < arr[i]:
        place += 1
    for j in range(place, i):
        arr[j], arr[i] = arr[i], arr[j]

print(*arr)
