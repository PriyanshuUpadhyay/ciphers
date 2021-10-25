def encrypt():
    plainText = input("Enter the plaintext to be encrypted: ").lower()
    key = int(input("Enter the key (1-25) to encrypt plaintext: "))
    ciphertext = ''
    if key not in range(1,26):
        print("Invalid key. Exiting!!")
        exit(0)
    
    for i in plainText:
        if i in mapp:
            ciphertext += unmapp[(mapp[i]+key)%26]
        else:
            ciphertext += i

    print("Ciphertext: ", ciphertext.upper())
    
def decrypt():
    ciphertext = input("Enter the ciphertext to be decrypted: ").lower()
    key = int(input("Enter the key (1-25) to encrypt plaintext: "))
    plainText = ''
    if key not in range(1,26):
        print("Invalid key. Exiting!!")
        exit(0)
    
    for i in ciphertext:
        if i in mapp:
            plainText += unmapp[(mapp[i]-key)%26]
        else:
            plainText += i

    print("Plaintext: ", plainText.upper())

mapp = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7,
    'i' : 8,
    'j' : 9,
    'k' : 10,
    'l' : 11,
    'm' : 12,
    'n' : 13,
    'o' : 14,
    'p' : 15,
    'q' : 16,
    'r' : 17,
    's' : 18,
    't' : 19,
    'u' : 20,
    'v' : 21,
    'w' : 22,
    'x' : 23,
    'y' : 24,
    'z' : 25
}

unmapp = dict([(value, key) for key, value in mapp.items()])

choice = int(input("Select 1 for encryptioin and 2 for decryption: "))

if choice == 1:
    encrypt()
elif choice == 2:
    decrypt()
else:
    print("Invalid choice. Exiting!!")
    exit(0)