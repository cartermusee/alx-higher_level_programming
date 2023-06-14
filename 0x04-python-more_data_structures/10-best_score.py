#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        max = list(a_dictionary.keys())[0]
        for i in a_dictionary:
            if a_dictionary[i] > a_dictionary[max]:
                max = i
        return max
    return None
