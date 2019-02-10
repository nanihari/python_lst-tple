### Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a
####given list of strings.
def match_words(words):
    character=0
    
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
          character+=1
    return character
print(match_words(["abc", "hari krishnah", "121", "abbaa", "abracadabra"]))



