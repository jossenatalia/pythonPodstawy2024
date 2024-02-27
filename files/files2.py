import chardet

file_path = '../test.log'
with open(file_path, "rb") as file:
    raw_data = file.read()

result = chardet.detect(raw_data)
print(result)

encoding = result['encoding']
print(raw_data.decode(encoding=encoding))


