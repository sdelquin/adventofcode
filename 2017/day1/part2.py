with open("input") as f:
    input = f.readline().strip()

matches = []
input_size = len(input)
step = input_size // 2
for i in range(input_size):
    next = (i + step) % input_size
    if input[i] == input[next]:
        matches.append(int(input[i]))
print(sum(matches))
