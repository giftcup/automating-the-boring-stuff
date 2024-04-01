word = input("Enter word to check for palindrome: ")
word_len = len(word)
palindrome = True

for i in range(0, int(word_len/2)):
    if (word[i] != word[word_len-1-i]):
        print(f"{word} is not a palindrome")
        palindrome = False
        break
    
if palindrome:     
    print(f"{word} is a palindrome")