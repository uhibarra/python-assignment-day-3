# Find Palindrome
# Given a string of lowercase letters, write a function to see if the word is a palindrome (the same word spelled forward and backwards).
# Example Input: 'racecar'
# Example Output: True 

word = input("Gimme a word: ")

rev_word = word[::-1]

if rev_word == word:
    print("This is a palindrome!")
else:
    print("This is NOT a palindrome!")