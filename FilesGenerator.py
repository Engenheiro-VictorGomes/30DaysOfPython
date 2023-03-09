import re

exercises_file = 'ExercicesLvl1.txt'

with open(exercises_file, 'r') as file:
    lines = file.readlines()

pattern = re.compile('^(?P<number>\d+)\.')

filename = None

for line in lines:
    match = pattern.match(line)
    if match:
        if filename is not None:
            with open(filename, 'w') as output:
                output.write(lineToWrite)
        number = match.group('number')
        filename = f'E{number.upper()}.py'        
        print(f"Gerou o arquivo {filename}")
        lineToWrite = f"# {line}"
        print(f" Preencheu o arquivo {filename} com a linha: {lineToWrite}")
    else:
        lineToWrite += f"# {line}"
        print(f" Preencheu o arquivo {filename} com a linha: {lineToWrite}")
