def char_to_int_map(start_char, *extra_chars):
    ctoi = {start_char: 0}
    for i in range(26):
        ctoi[chr(i+ord('a'))] = i + 1
    for i, ch in enumerate(extra_chars):
        ctoi[ch] = i + 27
    return ctoi

def int_to_char_map(ctoi):
    return {i:c for c,i in ctoi.items()}
