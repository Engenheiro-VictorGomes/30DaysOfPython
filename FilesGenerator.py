import re

folderToSave = "Day06"
exercises_file = 'List.txt'
pattern = re.compile('^(?P<number>\d+)\.')

filename = None
output = None

with open(exercises_file, 'r') as file:
    for line in file:
        match = pattern.match(line)
        if match:
            if output:
                output.close()
            number = match.group('number')
            filename = f'E{number.upper()}.py'
            print(f"Gerou o arquivo {filename}")
            output = open(f"{folderToSave}/{filename}", 'w')
        lineToWrite = f"# {line}"
        output.write(lineToWrite)
        print(f"Preencheu o arquivo {filename} com a linha: {lineToWrite}")

if output:
    output.close()