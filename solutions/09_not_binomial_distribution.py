import math

tests = int(input())
for counter in range(tests):
    inputting = input()
    i = inputting.split()
    n = int(i[0])
    p = float(i[1])
    if n < 10:
        print("Skip")
    else:
        prob = 0
        for bi in range(10):
            prob += (math.comb(n, bi)) * (p ** bi) * ((1 - p) ** (n - bi))
        if prob <= 0.15:
            print("Join")
        else:
            print("Skip")

# answer source: submission by Fourier Express