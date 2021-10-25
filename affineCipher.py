def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None 
    else:
        return x % m


def encrypt():
    text = input("Enter the plaintext to be encrypted: ").upper()
    key = list(map(int, input("Enter key as 'a b': ").split()))
    
    if key[0] not in inverse:
        print("'a' does not have inverse in mod 26. Invalid key. Exiting!!")
        exit(0)
        
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)+ ord('A')) for t in text.upper().replace(' ', '') ])


def decrypt():
    cipher = input("Enter the ciphertext to be decrypted: ").upper()
    key = list(map(int, input("Enter key as 'a b': ").split()))
    if key[0] not in inverse:
        print("'a' does not have inverse in mod 26. Invalid key. Exiting!!")
        exit(0)
    
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))% 26) + ord('A')) for c in cipher ])


inverse = [1,  3,  5,  7,  9,  11,  15,  17,  19,  21,  23,  25]

choice = int(input("Select 1 for encryptioin and 2 for decryption: "))
if choice == 1:
    print('Encrypted Text: {}'.format( encrypt() ))
elif choice == 2:
    print('Decrypted Text: {}'.format( decrypt() ))
else:
    print("Invalid choice. Exiting!!")
    exit(0)