t, x, y = map(int, input().split())
seen = [[False for i in range(t + 1)], [False for i in range(t + 1)]]
seen[0][0] = True
for a in range(len(seen)):
    for i in range(len(seen[a])):
        if not seen[a][i]: continue
        if i + x <= t: seen[a][i + x] = True
        if i + y <= t: seen[a][i + y] = True
        if a + 1 < len(seen): seen[a + 1][int(i / 2)] = True
res = t
while not seen[1][res]:
    res -= 1
print(res)

# answer source: submission by The Chosen Ones