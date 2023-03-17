# 6. Use the function, find_most_frequent_words to find:
#     a) The ten most frequent words used in Obama's speech
#     b) The ten most frequent words used in Michelle's speech
#     c) The ten most frequent words used in Trump's speech
#     d) The ten most frequent words used in Melina's speech
# 

def find_most_common_words(filename = None, n=10):
    if n <= 0:
        raise ValueError
    if filename is None:
        raise ValueError
    filepath = filename
    with open(filepath) as file:
        words = file.read().split()
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    return(sorted([(count, word) for word, count in words_count.items()], reverse=True)[:n])

print(find_most_common_words(filename='./data/obama_speech.txt', n=10))
print(find_most_common_words(filename='./data/michelle_obama_speech.txt', n=10))
print(find_most_common_words(filename='./data/donald_speech.txt', n=10))
print(find_most_common_words(filename='./data/melina_trump_speech.txt', n=10))