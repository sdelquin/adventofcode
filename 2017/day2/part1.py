import re
import numpy as np

spreadsheet = []
with open("input") as f:
    for line in f:
        spreadsheet.append([int(x) for x in re.split(r"\s+", line.strip())])

spreadsheet = np.array(spreadsheet)
max_values = np.amax(spreadsheet, axis=1)
min_values = np.amin(spreadsheet, axis=1)

print(sum(max_values - min_values))
