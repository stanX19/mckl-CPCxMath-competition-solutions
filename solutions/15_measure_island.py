def isValid2(screen, m, n, x, y, prevC, newC, result):
    if x < 0 or x >= m or \
            y < 0 or y >= n or \
            screen[y][x] == '.':
        result[1] = result[1] + 1
        return False
    if screen[y][x] != prevC \
            or screen[y][x] == newC:
        return False
    return True


# FloodFill function
def floodFill(screen,
              m, n, x,
              y, prevC, newC, result):
    queue = []

    # Append the position of starting
    # pixel of the component
    queue.append([x, y])

    # Check current pixel
    if screen[y][x] == prevC:
        result[0] = result[0] + 1
    else:
        return

    # Color the pixel with the new color
    screen[y][x] = newC

    # While the queue is not empty i.e. the
    # whole component having prevC color
    # is not colored with newC color
    while queue:

        # Dequeue the front node
        currPixel = queue.pop()

        posX = currPixel[0]
        posY = currPixel[1]

        # Check if the right adjacent pixel is valid
        if isValid2(screen, m, n, posX + 1, posY, prevC, newC, result):
            # Color with newC if valid and enqueue
            screen[posY][posX + 1] = newC
            queue.append([posX + 1, posY])
            result[0] = result[0] + 1
        # print(f'[{posX},{posY}] Check right = {result}')

        # Check if the left adjacent pixel is valid
        if isValid2(screen, m, n, posX - 1, posY, prevC, newC, result):
            screen[posY][posX - 1] = newC
            queue.append([posX - 1, posY])
            result[0] = result[0] + 1
        # print(f'[{posX},{posY}] Check left = {result}')

        # Check if the down adjacent pixel is valid
        if isValid2(screen, m, n, posX, posY + 1, prevC, newC, result):
            screen[posY + 1][posX] = newC
            queue.append([posX, posY + 1])
            result[0] = result[0] + 1
        # print(f'[{posX},{posY}] Check down = {result}')

        # Check if the upper adjacent pixel is valid
        if isValid2(screen, m, n, posX, posY - 1, prevC, newC, result):
            screen[posY - 1][posX] = newC
            queue.append([posX, posY - 1])
            result[0] = result[0] + 1
        # print(f'[{posX},{posY}] Check upper = {result}')


# main
N = int(input())
data = [['' for i in range(N)] for j in range(N)]
raw = []

for y in range(N):
    raw = input()
    for x in range(N):
        data[y][x] = raw[x]

# Current color at that co-ordinate
prevC = '#'

# New color that has to be filled
newC = '*'

# Initialize result [area, perimeter]
result = [0, 0]

for y in range(N):
    for x in range(N):
        temp = [0, 0]
        floodFill(data, N, N, x, y, prevC, newC, temp)
        if temp[0] > result[0]:
            result = temp
        if temp[0] == result[0] and temp[1] < result[1]:
            result = temp
print(f'{result[0]} {result[1]}')

# answer source: submission by jooguan