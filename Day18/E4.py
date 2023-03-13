# 4. Clean the following text. After cleaning, count three most frequent words in the string.
# 
#     sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
# 
#     print(clean_text(sentence));
#     I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
#     print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]

import re

def most_frequent_words(paragraph):
    word_counts = {}
    for word in re.split(' ', paragraph.replace('.','')):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return sorted([(count, word) for word, count in word_counts.items()], reverse=True)

def clean_text(paragraph):
    return re.sub(r'[^\w\s,.!?]','',paragraph) #Allow letter, numbers, ',', '.', '!', '?'

sentence = "%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"
cleaned_text = clean_text(sentence)
print(sentence)
print(cleaned_text)
print(most_frequent_words(re.sub(r'[^\w\s]','',cleaned_text.lower())))


