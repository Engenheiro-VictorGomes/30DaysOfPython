# 5.Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters -
#   a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order.
#   Check the output
#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 10))
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and'),
#     (4, 'a'),
#     (4, 'in'),
#     (3, 'that'),
#     (2, 'have'),
#     (2, 'I')]
# 
#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 5))
# 
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and')]

def find_most_common_words(filename = None, text = None, n=10):
    if n <= 0:
        raise ValueError
    if filename is None and text is None:
        raise ValueError
    elif filename is not None:
        filepath = filename
        with open(filepath) as file:
            text = file.read().splitlines()
    elif text is not None:
        text = [text]
    words = []
    for line in text:
        words.extend(line.split())
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    return(sorted([(count, word) for word, count in words_count.items()], reverse=True)[:n])

print(find_most_common_words(filename='./data/obama_speech.txt', n=10))
print(find_most_common_words(filename='./data/romeo_and_juliet.txt', n=3))
print(find_most_common_words(text='Just a generic text to test the function repeat repeat test repeat', n=3))