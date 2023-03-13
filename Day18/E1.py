# 1. What is the most frequent word in the following paragraph?
#     paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
#     [
#     (6, 'love'),
#     (5, 'you'),
#     (3, 'can'),
#     (2, 'what'),
#     (2, 'teaching'),
#     (2, 'not'),
#     (2, 'else'),
#     (2, 'do'),
#     (2, 'I'),
#     (1, 'which'),
#     (1, 'to'),
#     (1, 'the'),
#     (1, 'something'),
#     (1, 'if'),
#     (1, 'give'),
#     (1, 'develop'),
#     (1, 'capabilities'),
#     (1, 'application'),
#     (1, 'an'),
#     (1, 'all'),
#     (1, 'Python'),
#     (1, 'If')
#     ]
import re

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
word_counts = {}
for word in re.split(' ', paragraph.replace('.','')):
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

most_frequent_word = sorted([(count, word) for word, count in word_counts.items()], reverse=True)
print(most_frequent_word)

