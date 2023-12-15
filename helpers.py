import torch

def char_to_int_map(start_char, *extra_chars):
    ctoi = {start_char: 0}
    for i in range(26):
        ctoi[chr(i+ord('a'))] = i + 1
    for i, ch in enumerate(extra_chars):
        ctoi[ch] = i + 27
    return ctoi

def int_to_char_map(ctoi):
    return {i:c for c,i in ctoi.items()}

def build_dataset(words, ctoi, block_size=3):
    X, Y = [], []
    for word in words:
        padded_word_list = ['.']*block_size + list(word) + ['.']
        
        for i in range(len(padded_word_list) - block_size):
            chs1 = list(map(lambda ch: ctoi[ch], padded_word_list[i:i+block_size]))
            ch2 = ctoi[padded_word_list[i+block_size]]
            X.append(chs1)
            Y.append(ch2)
    X = torch.tensor(X)
    Y = torch.tensor(Y)
    return X, Y

def split(data, splits):
    assert sum(splits) == 1
    data_size = len(data)
    # split_data =[ [X[:int(splits[0])]]]
    split_data = []
    # curr_sum = splits[0]
    curr_sum = 0
    for s in splits:
        split_data.append(data[int(curr_sum*data_size):int((curr_sum+s)*data_size)])
        curr_sum+=s
        
    return tuple(split_data)
    