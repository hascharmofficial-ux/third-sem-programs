import re


pattern = input("Enter a regular expression: ")
text = input("Enter a string: ")

matches = re.findall(pattern, text)
print(matches)
