alkanes = ["methane", "ethane", "propane", "butane", "pentane", "hexane", "heptane", "octane", "nonane", "decane"]

h, w = map(int, input().split())

carbon_count = 0
for i in range(h):
    for c in input():
        if c == 'C':
            carbon_count += 1

print(alkanes[carbon_count - 1])

# answer source: stan