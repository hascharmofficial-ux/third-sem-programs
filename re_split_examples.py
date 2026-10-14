import re


print("Split your text wherever your regular expression matches.")
print(r"Pattern examples: \s+ (whitespace), [,;] (comma or semicolon), or - (hyphen)")
pattern = input("Enter a regular expression to split on: ")
text = input("Enter text to split: ")

parts = re.split(pattern, text)
print(f"Parts: {parts}")
