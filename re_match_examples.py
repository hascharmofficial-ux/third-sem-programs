import re


print("Check whether a pattern matches at the start of your text.")
print(r"Pattern examples: ^Hello, \d{4}, or [A-Z]\w+")
pattern = input("Enter a regular expression: ")
text = input("Enter text to check: ")

result = re.match(pattern, text)
if result:
    print(f"Match found at the start: {result.group()}")
else:
    print("No match at the start of the text.")
