# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
#     a) Read obama_speech.txt file and count number of lines and words
#     b) Read michelle_obama_speech.txt file and count number of lines and words
#     c) Read donald_speech.txt file and count number of lines and words
#     d) Read melina_trump_speech.txt file and count number of lines and words
# 

# a:
filepath = './data/obama_speech.txt'
with open(filepath) as f:
    contents = f.read()
    lines = contents.splitlines()
    words = contents.split()
    print(f"Number of lines = {len(lines)}")
    print(f"Number of words = {len(words)}")

# b:
filepath = './data/michelle_obama_speech.txt'
with open(filepath) as f:
    contents = f.read()
    lines = contents.splitlines()
    words = contents.split()
    print(f"Number of lines = {len(lines)}")
    print(f"Number of words = {len(words)}")

# c:
filepath = './data/donald_speech.txt'
with open(filepath) as f:
    contents = f.read()
    lines = contents.splitlines()
    words = contents.split()
    print(f"Number of lines = {len(lines)}")
    print(f"Number of words = {len(words)}")

# d:
filepath = './data/melina_trump_speech.txt'
with open(filepath) as f:
    contents = f.read()
    lines = contents.splitlines()
    words = contents.split()
    print(f"Number of lines = {len(lines)}")
    print(f"Number of words = {len(words)}")

# Solution 2
def count_line_words(filename):
    filepath = f'./data/{filename}'
    with open(filepath) as f:
        contents = f.read()
        lines = contents.splitlines()
        words = contents.split()
    return len(lines),len(words)

def print_lines_words(name):
    lines, words = count_line_words(f"{name}.txt")
    name_clean = name.replace('_',' ')
    print(f"Lines in {name_clean} = {lines} | Words in {name_clean} = {words}")

names = [
            "obama_speech",
            "michelle_obama_speech",
            "donald_speech",
            "melina_trump_speech"]
for name in names:
    print_lines_words(name)