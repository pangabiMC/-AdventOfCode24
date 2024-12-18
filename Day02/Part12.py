import numpy as np 

filename = "Day02/input"
reports = []
with open(filename) as file:
    for line in file:
        reports.append(list(map(int, line.strip().split())))

# part 1

def isSafe(report):
    return indexOfFirstBad(report) == -1

def indexOfFirstBad(report):
    diffs = [i - j for i, j in zip(report, report[1:])]
    signs = [i * j for i, j in zip(diffs, diffs[1:])]
    firstDistError = next((i for i, d in enumerate(diffs) if (abs(d) > 3 or abs(d) < 1)), -1)
    firstSignError = next((i for i, d in enumerate(signs) if d < 0), -1)
    return max(firstSignError, firstDistError)

print(sum(isSafe(report) for report in reports))


# part 2

safecount = 0
for report in reports:
    err = indexOfFirstBad(report)
    # the report might become safe if the element at the error is removed, or after, or before (depending the kind of error it has)
    if(err == -1 or isSafe(report[:err + 1] + report[err + 2:]) or isSafe(report[:err] + report[err + 1:]) or isSafe(report[:err + 2] + report[err + 3:])):
        safecount += 1
print(safecount)

