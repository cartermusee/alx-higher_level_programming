#!/usr/bin/python3
if __name__ == "__main__":

    """moreon calc"""
    import sys
    from calculator_1 import add, sub, mul, div

    total_len = len(sys.argv) - 1
    if total_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = sys.argv[1]
    b = sys.argv[3]
    operator = sys.argv[2]

    if operator == '+':
        print("{:d} - {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

