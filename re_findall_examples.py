import re


print("Find every non-overlapping match of your pattern in the text.")
print(r"Pattern examples: \d+ (numbers), [A-Z] (uppercase letters), or \w+ (words)")
pattern = input("Enter a regular expression: ")
text = input("Enter text to search: ")

matches = re.findall(pattern, text)
print(f"Matches: {matches}")
