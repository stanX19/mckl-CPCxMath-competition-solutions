T = int(input())

for i in range(T):
    N = int(input())
    data = [int(i) for i in input().split()]
    data_square = [i * i for i in data]

    print(sum(data), sum(data_square))

# answer source: stan