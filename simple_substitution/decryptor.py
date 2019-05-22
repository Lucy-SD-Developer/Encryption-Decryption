def decrypt_from_key(input, key):
    output = ""
    for c in input:
        found = False
        for k, v in key.items():
            if v == c:
                output = output + k
                found = True
                break
        if not found:
            output = output + c
    return output
