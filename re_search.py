import re


pattern = input("Enter a regular expression: ")
text = input("Enter a string: ")

result = re.search(pattern, text)
print(result)
