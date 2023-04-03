# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
import requests
import re


def find_most_common_words(filename = None, url=None, n=10, remove_words = None):
    # Check Parameters
    if n <= 0:
        raise ValueError
    if filename is None and url is None:
        raise ValueError
    if remove_words is None:
        remove_words = []

    # Open file and extract words
    if filename is not None:
        with open(filename) as file:
            words = []
            for line in file:
                words.extend(re.findall(r'\b\w+\b', line))
        words = list(map(lambda x: x.lower(), words))

    # Open url and extract words
    if url is not None:
        response = requests.get(url)
        words = []
        words.extend(re.findall(r'\b\w+\b', response.text))
        words = list(map(lambda x: x.lower(), words))
    
    # Remove words
    for remove_word in remove_words:
        words = list(filter(lambda x: x != remove_word, words))

    # Get words counting
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    return(sorted([(count, word) for word, count in words_count.items()], reverse=True)[:n])

remove_words = ['the', 'and', 'to', 'of', 'a', 'an', 'in', 'with', 'that', 'this', 's', 'd']
print(find_most_common_words(url = 'http://www.gutenberg.org/files/1112/1112.txt', remove_words=remove_words))
