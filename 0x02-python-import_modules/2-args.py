#!/usr/bin/python3
if __name__ == "__main__":
    """ numbers of a list."""
    import sys

    count_len = len(sys.argv) - 1
    if count_len ==0:
        print('0 arguments.')
    elif count_len == 1:
        print('1 argument:')
    else:
        print('{} arguments:'.format(count_len))
    for i in range(count_len):
        print('{}: {}'.format(i + 1, sys.argv[i + 1))
