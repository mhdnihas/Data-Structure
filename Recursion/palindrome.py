def ispalindrom(word):
    if len(word)<=1:
        return True
    return word[0]==word[-1] and ispalindrom(word[1:-1])

word1="malayalam"
word2="hai"
print(f"is {word1} palindrom?{ispalindrom(word1)}")
print(f"is {word2} palindrom?{ispalindrom(word2)}")

