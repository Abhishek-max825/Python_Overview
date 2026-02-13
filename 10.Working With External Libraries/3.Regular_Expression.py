'''
Regular Expressions in Python :-

Regular expressions (regex) are powerful tools for pattern matching in strings. Python's re module provides support for regex.
'''
import re

text = "The quick brown fox jumps over the lazy dog."

# Search for a pattern
# -> it returns the first occurence of the pattern from the text
match = re.search("brown", text)
if match:
    print("Match found!")
    print("Start index:", match.start())
    print("End index:", match.end())

'''
Output :-
Match found!
Start index: 10
End index: 15
'''    

# Find all occurrences of a pattern
# -> it finds all the occurence of the pattern in the text
matches = re.findall("the", text, re.IGNORECASE)  # Case-insensitive search
print("Matches:", matches)
# Output :- Matches: ['The', 'the']

# Replace all occurrences of a pattern
# -> it replaces all the occurences of the pattern with replacement text
new_text = re.sub("fox", "cat", text)
print("New text:", new_text)
# Output :-  New text: The quick brown cat jumps over the lazy dog.

# Compile a regex for efficiency (if used multiple times)
pattern = re.compile(r"\b\w+\b")  # Matches whole words
words = pattern.findall(text)
print("Words:", words)
# Output :- Words: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

'''
Part	Meaning
\b	Word boundary (ensures we match full words, not parts of words)
\w+	One or more word characters (letters, digits, underscores)
\b	Word boundary (ensures we match entire words)
'''