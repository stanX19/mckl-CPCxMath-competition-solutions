# binary search
# brick count = n(n + 1)/2, n = height

T = int(input())

for i in range(T):
    N, K = map(int, input().split())

    heights = [int(i) for i in input().split()]

    low = 0
    high = N

    while low < high:
        mid = low + (high - low) // 2  # (low + high) / 2
        bricks = (heights[mid] + 1) / 2 * heights[mid]

        if (bricks >= K):  # can still shift to left
            high = mid
        elif bricks < K:  # too less
            low = mid + 1

    if (low != N):
        print(low + 1)
    else:
        print("-1")

# answer source: stan