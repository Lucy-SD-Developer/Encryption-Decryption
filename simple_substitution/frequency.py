# English letter frequency in order from the highest to lowest frequency
_WORDS = [ 'E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H',
'D', 'L', 'U', 'C', 'M', 'F', 'Y', 'W', 'G', 'P', 'B', 'V', 'K',
'X', 'Q', 'J', 'Z']


# English letter frequency corresponding to the predefined array words
# data are from English letter frequency table
_FREQ = [ 12.02,9.10,8.12,7.68,7.31,6.95,6.28,6.02,5.92,4.32,3.98,2.88,2.71,
2.61,2.30,2.11,2.09,2.03,1.82,1.49,1.11,0.69,0.17,0.11,0.10,0.07 ]


# store English letter frequencies
def get_frequency(input):
    input_freq = {}
    char_count = 0
    for char in input:
        if char > 'Z' or char < 'A':
            continue
        input_freq[char] = input_freq.get(char, 0.0) + 1
        char_count = char_count + 1
    '''
    for char in input_freq:
        input_freq[char] = input_freq[char] / char_count * 100
    '''
    return input_freq


# get key
def get_key_by_frequency(input):
    input_freq = get_frequency(input)
    key = {}
    for k, v in input_freq.items():
        for i, f in enumerate(_FREQ):
            left = 100 if i == 0 else _FREQ[i-1]
            right = _FREQ[i]
            if left - v <= right:
                # closer to left
                word = _WORDS[i-1]
            else:
                word = _WORDS[i]
            while word in key and i - 1 >= 0:
                i = i - 1
                word = _WORDS[i]
            while word in key and i + 1 < len(_FREQ):
                i = i + 1
                word = _WORDS[i]
            key[word] = k
            break
    return key
