def check_palindrome(word):
    return True if word.lower() == word[::-1].lower() else False

 
print(check_palindrome("anna"))

# word = "Hannah"
# # print(word == word[::-1])
# print(word.lower())
# print(word[::-1].lower())