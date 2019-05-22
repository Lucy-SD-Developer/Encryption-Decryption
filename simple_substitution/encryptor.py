# keys for the simple substitution cipher usually consist of 26 letters with random order.
_KEY = [ 'J', 'I', 'C', 'A', 'X', 'S', 'E', 'Y', 'V',
'D', 'K', 'W', 'B', 'Q', 'T', 'Z', 'R', 'H', 'F', 'M', 'P', 'N',
'U', 'L', 'G', 'O']

def encrypt(input):
    output = ""
    for c in input:
        c = c.upper()
        if c < 'A' or c > 'Z':
            output = output + c
            continue
        output = output + _KEY[ord(c) - ord('A')]
    return output
