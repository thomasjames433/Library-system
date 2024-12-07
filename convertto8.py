# Open the file in UTF-16 encoding and read its content
with open('data.json', 'r', encoding='utf-16') as file:
    content = file.read()

# Write the content back in UTF-8 encoding
with open('data_converted.json', 'w', encoding='utf-8') as file:
    file.write(content)

print("File converted to UTF-8 successfully.")
