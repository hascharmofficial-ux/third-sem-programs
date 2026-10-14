import re


pattern = input("Enter a regular expression: ")
text = input("Enter a string: ")

parts = re.split(pattern, text)
print(parts)
