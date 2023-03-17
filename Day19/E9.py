# 9. Read the hacker news csv file and find out:
#     a) Count the number of lines containing python or Python
#     b) Count the number lines containing JavaScript, javascript or Javascript
#     c) Count the number lines containing C and not JavaScript
import re


counter_python = 0
counter_javascript = 0
counter_java = 0

with open("./data/hacker_news.csv") as file:
    for line in file:
        if re.search(r'\bpython\b|\bPython\b',line):
            counter_python+=1
        if re.search(r'\bJavaScript\b|\bjavascript\b|\bJavascript\b',line):
            counter_javascript+=1
        if re.search(r'\bJava\b|\bjava\b',line):
            counter_java+=1

print(f"Python = {counter_python}")
print(f"Javascript = {counter_javascript}")
print(f"Java = {counter_java}")
