word = input("Enter a word: ")
key = int(input("enter the shift number: "))
alphabet = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k","l", "m", "n", "o", "p","q", "r", "s", "t", "u","v", "w", "x", "y", "z", " "]
newWord = ""

def caesarCypher(word, key, newWord):

    for x in word:
        position = alphabet.index(x)
        print(f"original position {position}")
        position += key
        print(f"new position {position}")
        #the last letter is shifted back to postion 0
        if position == len(alphabet):
            position -= len(alphabet)
        newWord += alphabet[position]
    return newWord


newWord = caesarCypher(word, key, newWord)
print(f"encrypted word is: {newWord}") 
