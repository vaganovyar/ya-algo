arr = list(map(int, input().split()))
elem = int(input())
l = -1
r = len(arr)
while l + 1 < r:
    mid = (l + r) // 2
    if arr[mid] > elem:
        r = mid
    else:
        l = mid
print(l)
