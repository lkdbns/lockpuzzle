#!/usr/bin/env python3

import re
import sys

hints = []
force = []
reRightPlace0 = '[^{0}][^{1}][^{2}]'
reRightPlace1 = '[{0}][^{1}][^{2}]|[^{0}][{1}][^{2}]|[^{0}][^{1}][{2}]'
reRightPlace2 = '[{0}][{1}][^{2}]|[{0}][^{1}][{2}]|[^{0}][{1}][{2}]'
reRightPlace3 = '[{0}][{1}][{2}]'
reWrongPlace0 = '[^{1}{2}][^{0}{2}][^{0}{1}]'
reWrongPlace1 = '[{1}{2}][^{0}{2}][^{0}{1}]|[^{1}{2}][{0}{2}][^{0}{1}]|[^{1}{2}][^{0}{2}][{0}{1}]'
reWrongPlace2 = '[{1}{2}][{0}{2}][^{0}{1}]|[{1}{2}][^{0}{2}][{0}{1}]|[^{1}{2}][{0}{2}][{0}{1}]'
reWrongPlace3 = '[{1}{2}][{0}{2}][{0}{1}]|[{1}{2}][{0}{2}][{0}{1}]|[{1}{2}][{0}{2}][{0}{1}]'

count = 0

for x in range(0, 1000):
    force.append(1)
    force[x]=str(x).zfill(3)

for i in sys.argv[1:]:
    if re.search(r"^\d{3}-[0-3]-[0-3]$", i):
        hints.append(1)
        hints[count] = re.sub(r"(\d)(\d)(\d)-([0-3])-([0-3])", r"\1-\2-\3-\4-\5", i)
        count += 1
    else:
        print("Invalid argument: ", i)
        sys.exit(1)

print("Trying", end = "")
for i in sys.argv[1:]:
    print(" " + i, end = "")
print("")

for hint in hints:
    code = hint.split("-")
    if code[3] == '0':
        tmpFilter = re.compile(reRightPlace0.format(code[0], code[1], code[2]))
        force = list(filter(tmpFilter.search, force))
    elif code[3] == '1':
        tmpFilter = re.compile(reRightPlace1.format(code[0], code[1], code[2]))
        force = list(filter(tmpFilter.search, force))
    elif code[3] == '2':
        tmpFilter = re.compile(reRightPlace2.format(code[0], code[1], code[2]))
        force = list(filter(tmpFilter.search, force))
    elif code[3] == '3':
        tmpFilter = re.compile(reRightPlace3.format(code[0], code[1], code[2]))
        force = list(filter(tmpFilter.search, force))
    if code[4] == '0':
        tmpFilter = re.compile(reWrongPlace0.format(code[0], code[1], code[2]))
        force = list(filter(tmpFilter.search, force))
    elif code[4] == '1':
        tmpFilter = re.compile(reWrongPlace1.format(code[0], code[1], code[2]))
        force = list(filter(tmpFilter.search, force))
    elif code[4] == '2':
        tmpFilter = re.compile(reWrongPlace2.format(code[0], code[1], code[2]))
        force = list(filter(tmpFilter.search, force))
    elif code[4] == '3':
        tmpFilter = re.compile(reWrongPlace3.format(code[0], code[1], code[2]))
        force = list(filter(tmpFilter.search, force))

if not force:
    print("No Solutions Found")
    sys.exit(1)

for i in force:
    print('*** Solution #{0} is {1}'.format(count, i))
    count += 0