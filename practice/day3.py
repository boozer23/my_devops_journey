def word_count_dict(text):
    words = text.split()
    count_dict = {}
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1
    return count_dict

print(word_count_dict("привет мир привет"))  # {'привет': 2, 'мир': 1}