word1 = (input("Enter a word: ")).lower()
word2 = (input("Enter another word to check for anagrams: ")).lower()

def anagram(word1, word2):
    if (len(word1) != len(word2)):
        return False
    elif (word1 == word2):
        return True
    else:
        for letter in word1:
            if (letter not in word2):
                return False
        return True

anagram = anagram(word1, word2)

if anagram:
    print(f"{word1} IS an anagram of {word2}")
else:
    print(f"{word1} IS NOT an anagram of {word2}")