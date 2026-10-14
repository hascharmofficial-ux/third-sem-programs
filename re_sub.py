import re


pattern = input("Enter a regular expression: ")
replacement = input("Enter the replacement string: ")
text = input("Enter a string: ")

result = re.sub(pattern, replacement, text)
print(result)
