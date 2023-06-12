#1/usr/bin/python3
def multiple_returns(sentence):
    tuple_len = len(sentence)
    if tuple_len == 0:
        ch = None
    else:
        ch = sentence[0]
    return ((tuple_len, ch))
