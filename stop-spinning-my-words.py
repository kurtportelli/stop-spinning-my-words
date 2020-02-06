def spin_words(sentence):
    split_words = sentence.split()
    reversed_words = []
    for word in split_words:
        if len(word) < 5:
            reversed_words.append(word)
        else:
            reversed_words.append(word[::-1])
    return ' '.join(reversed_words)
