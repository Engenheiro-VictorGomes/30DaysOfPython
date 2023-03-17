# 7. Write a python application that checks similarity between two texts.
#     It takes a file or a string as a parameter and it will evaluate the similarity of the two texts.
#     For instance check the similarity between the transcripts of Michelle's and Melina's speech.
#     You may need a couple of functions, function to clean the text(clean_text),
#     function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
#     List of stop words are in the data directory

import re


def get_words_from_file(filepath):
    with open(filepath) as file:
        words = []
        for line in file:
            words.extend(re.findall(r'\b\w+\b', line))
    return words

def remove_words(words_to_read, words_to_remove):
    words_result = words_to_read
    for word_to_remove in words_to_remove:
        words_result = list(filter(lambda x: x != word_to_remove, words_result))
    return words_result

def similarity(text1_words, text2_words):
    similarity = set(text1_words) & set(text2_words)
    similarity_percent = (len(similarity) / len(set(text1_words + text2_words))) * 100
    return similarity_percent

def check_Similarity(file1, file2, words_to_remove, decimal = 2):
    text1_words = get_words_from_file(file1)
    text1_words = remove_words(text1_words, words_to_remove)
    text2_words = get_words_from_file(file2)
    text2_words = remove_words(text2_words, words_to_remove)
    percent = similarity(text1_words, text2_words)
    return round(percent, decimal)

# Inputs
words_to_remove = ['the', 'and', 'of', 'to', 'that', '-', 'for', 'a', 'an', 'in']
filepath1='./data/michelle_obama_speech.txt'
filepath2='./data/melina_trump_speech.txt'

# Process
percent = check_Similarity(filepath1, filepath2, words_to_remove, decimal=2)

# Outputs
print(f"Comparing text: {filepath1}")
print(f"     with text: {filepath2}")
print(f"Ignoring the words: {words_to_remove}")
print(f"Similarity = {percent}%")
