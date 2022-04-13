import random

def randomKey(): #random key generator
    alphaCollection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'?!@#$%^&*()~" #ascii collection
    a = random.randint(1,9) #random multiplier
    c = random.randint(1,9) #random counter
    s = 1
    m = int(len(alphaCollection)) #modulo the lenght of alphaCollection 
    result = "" #store the new key

    #LCG pseudo random number algorithm
    for i in range(s, 9):
        randomNum = (s*a+c) % m
        s = randomNum
        result += alphaCollection[s]
    return result

def encrypt(text, key):
    alphaCollection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'?!@#$%^&*()~ " #ascii collection
    new_key = key #add the new key lenght depending on how many characters are in the message. EG. hellohellohellohellohell
    i = 0 # Pointer counter 
    result = "" # Store the encrypted message
    while len(new_key) < len(text): # if the length of the key is not equal to the message lenght: run this until it matches the same length
        new_key = new_key + key[i] #add the characters based on the index number provided in i variable
        i = (i + 1) % len(key)  # increment i variable by 1 and modulo the lenght of the key to reset the number to 0 if reached the last character. Avoiding index error
    for alpha, alphaKey in zip(text, new_key): # for each character in text and new_key run this
        newLetterindex = (alphaCollection.index(alpha) + alphaCollection.index(alphaKey)) % int(len(alphaCollection)) #find the index position of the each character in text and newkey, add them together and modulo the lenght of alphaCollection:
        result += alphaCollection[newLetterindex] # add the characters found in alphaCollection based on the number newLetterindex provided.  
    return result


def decrypt(text, key):
    alphaCollection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'?!@#$%^&*()~ "
    new_key = key
    i = 0
    result = ""
    while len(new_key) < len(text):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    for alpha, alphaKey in zip(text, new_key):
        newLetterindex = (alphaCollection.index(alpha) - alphaCollection.index(alphaKey)) % int(len(alphaCollection))
        result += alphaCollection[newLetterindex]
    return result

print("Welcome to encrypt or decrypt a message \n")

while True:
    choice = input("Choose from the following: [1] encrypt a message, [2] decrypt a message: ")
    message = input("Enter a message: ")
    if int(choice) == 1:
        newKey = randomKey()
        print("Your new key is: ", newKey)
        for i in range(2):
            encryption = encrypt(message, newKey)
            res = encrypt(encryption, newKey)
        print(res)
        break
    elif int(choice) == 2 :
        key = input("Enter a key: ")
        for i in range(2):
            decryption = decrypt(message, key)
            res2 = decrypt(decryption, key)
        print(res2)
        break
    else:
        print("Invalid input please try again.....")

# cipher_text = "Leave Bob's enveloped in Building 19 at ECU"
