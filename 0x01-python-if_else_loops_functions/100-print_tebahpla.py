#!/usr/bin/python3
for i in range(25, -1, -1):
    n = i + ord('A')
    if i % 2 == 1:
        n += 32
    print("{:c}".format(n), end="")
