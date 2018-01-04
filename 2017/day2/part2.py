import re
import numpy as np

spreadsheet = []
with open("input") as f:
    for line in f:
        spreadsheet.append([int(x) for x in re.split(r"\s+", line.strip())])

spreadsheet = np.array(spreadsheet)

evenly_divisibles = []
for row in spreadsheet:
    for value in row:
        r = row / value
        match = [v for v in r if round(v) == v and v > 1]
        if match:
            evenly_divisibles.append(int(match[0]))
            break

print(sum(evenly_divisibles))
