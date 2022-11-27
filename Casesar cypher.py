

alphabet = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k","l", "m", "n", "o", "p","q", "r", "s", "t", "u","v", "w", "x", "y", "z", " "]
newWord = ""


def caesarCypher(newWord):
    encode = input("press 1 to encrypt and 2 to decrypt: ")
    if(encode == 1):
        word = input("Enter a word: ")
        key = int(input("enter the shift number: "))
        for x in word:
            position = alphabet.index(x)
            print(f"original position {position}")
            position += key
            print(f"new position {position}")
            if position >= len(alphabet):
                position = (key % len(alphabet))-1
            newWord += alphabet[position]
    
    else:
        word = input("Enter a word: ")
        key = int(input("enter the shift number: "))
        for x in word:
            position = alphabet.index(x)
            print(f"original position {position}")
            position -= key
            print(f"new position {position}")
            if position < 0:
                position += len(alphabet)
            newWord += alphabet[position]
    return newWord


newWord = caesarCypher(newWord)
print(f"encrypted word is: {newWord}")