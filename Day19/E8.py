# 8. Find the 10 most repeated words in the romeo_and_juliet.txt
import re


def find_most_common_words(filename = None, n=10, remove_words = None):
    # Check Parameters
    if n <= 0:
        raise ValueError
    if filename is None:
        raise ValueError
    if remove_words is None:
        remove_words = []

    # Open file and extract words
    with open(filename) as file:
        words = []
        for line in file:
            words.extend(re.findall(r'\b\w+\b', line))
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
print(find_most_common_words(filename='./data/romeo_and_juliet.txt', n=10, remove_words=remove_words))

# Solution 02:
def find_most_common_words_Solution02(filename = None, n=10, remove_words = None):
    # Check Parameters
    if n <= 0 or filename is None:
        raise ValueError
    if remove_words is None:
        remove_words = []

    # Open file and extract words
    with open(filename) as file:
        words = re.findall(r'\b\w+\b', file.read().lower())
    
    # Remove words
    remove_words = set(remove_words) if remove_words else set()
    words = [word for word in words if word not in remove_words and re.match('^[a-z]+$', word)]

    # Get words counting
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    return(sorted([(count, word) for word, count in words_count.items()], reverse=True)[:n])

print(find_most_common_words_Solution02(filename='./data/romeo_and_juliet.txt', n=10, remove_words=remove_words))