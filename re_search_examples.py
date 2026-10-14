import re


print("Find the first occurrence of your pattern anywhere in the text.")
print(r"Pattern examples: \d+ (numbers), cat|dog (either word), or (\w+) (captured word)")
pattern = input("Enter a regular expression: ")
text = input("Enter text to search: ")

result = re.search(pattern, text)
if result:
    print(f"First match: {result.group()}")
    if result.groups():
        print(f"Captured groups: {result.groups()}")
else:
    print("No match found.")
