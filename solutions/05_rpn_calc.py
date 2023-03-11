def c_division(a:int, b:int) -> int:
    if abs(a) < abs(b):
        return 0;
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return abs(a) // abs(b)  # floor division
    if (a > 0 and b < 0) or (a < 0 and b > 0):
        return -(abs(a) // abs(b))  # floor division

buf = input()
nums = []

for s in buf.split():
    if s in ['+', '-', '*', '/']:
        n2 = nums[-1]
        n1 = nums[-2]
        nums.pop(-1)
        nums.pop(-1)
        if s == '+':
            nums.append(n1 + n2)
        elif s == '-':
            nums.append(n1 - n2)
        elif s == '*':
            nums.append(n1 * n2)
        elif s == '/':
            nums.append(c_division(n1, n2))
    else:
        nums.append(int(s))

print(int(nums[0]))

# answer source: stan