for i in range(int(input())):
    input()
    data = list(map(int, input().split()))
    total = sum(data)
    least = float("INF")
    for j in range(1, total + 1):
        if total % j == 0:
            can = True
            buffer = 0
            cnt = 0
            for k in range(len(data)):
                buffer += data[k]
                cnt += 1
                if buffer > j:
                    can = False
                    break
                elif buffer == j:
                    buffer = 0
                    cnt -= 1
            if can: least = min(least, cnt)
    if least == float("INF"):
        print(0)
    else:
        print(least)

# answer source: submission by The Chosen Ones
