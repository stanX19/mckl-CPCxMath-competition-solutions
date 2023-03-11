word_count, max_length = map(int, input().split())
text = input()
words = text.split()

current_line = []
current_length = 0

for word in words:
    if len(word) + current_length <= max_length:
        current_line.append(word)
        current_length += len(word)
    else:
        print(" ".join(current_line))
        current_line = [word]
        current_length = len(word)

if current_line:
    print(" ".join(current_line))

# answer source: modified submission by DROP TABLE User;