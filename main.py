# task 3: check if a word is a palindrome
def is_palindrome(word):
     word = word.lower()
     return word == ''.join(reversed(word))


word = input("enter a word to check if it is a palindrome or not:")
if is_palindrome(word):
    print(f"'{word}' is a palindrome ")
else:
    print(f"'{word}' is not a palindrome")