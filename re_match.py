import re


pattern = input("Enter a regular expression: ")
text = input("Enter a string: ")

result = re.match(pattern, text)
print(result)
