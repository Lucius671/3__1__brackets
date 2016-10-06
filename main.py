import re

def process_text( str ):
    b1 = 0 #brackets '(', ')'
    b2 = 0 #brackets '[', ']'
    b3 = 0 #brackets '{', '}'
    for i, a in enumerate(str):
        if a == '(':
            b1 += 1
        elif a == ')':
            if b1 <= 0:
                return i
            else:
                b1 -= 1
        elif a == '[':
            b2 += 1
        elif a == ']':
            if b2 <= 0:
                return i
            else:
                b2 -= 1
        elif a == '{':
            b3 += 1
        elif a == '}':
            if b3 <= 0:
                return i
            else:
                b3 -= 1
    if b1 > 0 or b2 > 0 or b3 > 0:
        return -1
    else:
        return 'yes'

print process_text(raw_input())
