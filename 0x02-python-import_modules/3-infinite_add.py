#!/usr/bin/python3
if __name__ == "__main__":
    """addition of numbers all."""
    import sys
    sum_all = 0
    for i in range(len(sys.argv) - 1):
        sum_all += int(sys.argv[i + 1])
    print(sum_all)
