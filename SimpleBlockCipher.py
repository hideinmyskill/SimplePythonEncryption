import math

def permuted(text,permutation): #does a permutation for characters in string to change its positions based on given value eg.123456 - 241365.
    perm = [] #empty list to store the string based on their index number
    for t, p in zip(text,permutation): #for each text and permutation number...
        perm.append(text[int(p)-1]) #append the text based on the number given in the permutation variable minus 1
    return "".join(perm)  # Convert the list into string

def encrypt(text, key): #encryption starts here
    alphaCollection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'?!@#$%^&*()~ " #ascii collection
    newKey = key #set up a new key variable
    newText = text #to store new added text
    start = 0  #Index number for start range
    end = 6    #Index number for end range
    result = ""  #store the final encrypted characters

    if int(len(newText) % 6) != 0: # if the text is not even for a 48 byte character, it will expand
        maths = 6 - int(len(newText) % 6) #calculate how many bytes to add in the variable. eg. if total length of text is 43 it will add 5 characters to match 48 bytes
        newText += ("~" * maths) #Add "~" until 48 byte is match

    for i in range(math.floor(len(newText)/6)): #run block by block that contains 6 bytes in each block. Total of 8 runs.
        permText = permuted(newText[start:end], permutation)    # it will perform permutation for each block
        newText += permText #add the permutated string in to the newText variable
        start = start + 6 #increment start by 6
        end = end + 6   #increment end by 6

        for alpha, alphaKey in zip(permText, newKey):  # for each character in text and new_key run this
            newLetterindex = (alphaCollection.index(alpha) + alphaCollection.index(alphaKey)) % int(len(alphaCollection)) #key addition #find the index position of the each character in text and newkey, add them together and modulo the lenght of alphaCollection:
            result += alphaCollection[newLetterindex] # add the characters found in alphaCollection based on the number newLetterindex provided.

    return result

def decrypt(text, key):
    alphaCollection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'?!@#$%^&*()~ "
    newKey = key
    newText = ""
    start = 0
    end = 6
    result = ""

    i = 0
    while len(newKey) < len(text):
        newKey = newKey + key[i]
        i = (i + 1) % len(key)

    for alpha, alphaKey in zip(text, newKey):
        newLetterindex = (alphaCollection.index(alpha) - alphaCollection.index(alphaKey)) % int(
            len(alphaCollection))  # key addition
        newText += alphaCollection[newLetterindex]

    for i in range(math.floor(len(newText) / 6)):
        permText = permuted(newText[start:end], inverseperm)
        result += permText
        start = start + 6
        end = end + 6

    return result

permutation = "241365"
inverseperm = "314265"
#cipher_text = "Leave Bob's enveloped in Building 19 at ECU"
#key = "Mycake"

print("Welcome to encrypt or decrypt a message : Block Cipher \n")
message = input("Enter a message: ")
key = input("Enter a key: ")
while True:
    choice = input("Choose from the following: [1] encrypt a message, [2] decrypt a message: ")

    if int(choice) == 1:
        res = encrypt(encrypt((encrypt(message, key)), key), key) #encrypt 3x times
        print(res)
        break
    elif int(choice) == 2:
        res = decrypt(decrypt((decrypt(message, key)), key), key) #decrypt 3x times
        if "~" in res:
            num = res.count("~")
            res = list(res)
            for i in range(num):
                res.pop(len(res) - (5 - i))
        print("".join(res))
        break

    else:
        print("Invalid input please try again.....")

