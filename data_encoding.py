import chardet

with open('data.json', 'rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    print(result)
