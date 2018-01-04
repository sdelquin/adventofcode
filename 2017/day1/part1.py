with open("input") as f:
    input = f.readline().strip()

matches = []
input_size = len(input)
for i in range(input_size):
    next = (i + 1) % input_size
    if input[i] == input[next]:
        matches.append(int(input[i]))
print(sum(matches))
