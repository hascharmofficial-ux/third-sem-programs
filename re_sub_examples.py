import re


print("Replace every match of your pattern with replacement text.")
print(r"Pattern examples: \d+ (numbers), \s+ (whitespace), or cat|dog (either word)")
pattern = input("Enter a regular expression: ")
replacement = input("Enter replacement text (leave blank to remove matches): ")
text = input("Enter text to change: ")

result = re.sub(pattern, replacement, text)
print(f"Result: {result}")
