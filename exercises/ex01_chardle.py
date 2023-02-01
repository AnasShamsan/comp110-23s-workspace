"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730524701"

word: str = input("Enter a 5-character word: ")
if int(len(word)) != 5:
    print("Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ")
if int(len(single_character)) !=1:
    print("Character must be a single character")
    exit()

found: int = 0

if (word[0] == single_character):
    print(single_character + " is found at index " + str(0))
    found = found + 1
    print(str(found) + " instance of " + single_character + " found")

if (word[1] == single_character):
    print(single_character + " is found at index " + str(1))
    found = found + 1
    print(str(found) + " instance of " + single_character + " found")

if (word[2] == single_character):
    print(single_character + " is found at index " + str(2))
    found = found + 1

if (word[3] == single_character):
    print(single_character + " is found at index " + str(3))
    found = found + 1
    print(str(found) + " instance of " + single_character + " found")

if (word[4] == single_character):
    print(single_character + " is found at index " + str(4))
    found = found + 1
    print(str(found) + " instance of " + single_character + " found")

print()