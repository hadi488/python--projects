import random 
import string

st = " " + string.punctuation + string.digits + string.ascii_letters
print(st)
chars = list(st)
key = chars.copy()
random.shuffle(key)
print(key)
print(chars)
plain_text = ""

def Encrypt():
    enc_text = ''
    plain_text = input("enter your message to encrypt")
    for letter in plain_text:
        indx = chars.index(letter)
        # print(indx)
        enc_text += key[indx]
        # print(key[indx])
    
    print(f'encrypted text is {enc_text}')

def Decrypt():
    dec_text = ''
    en_text = input("enter your encrypted message to decrypt")
    for letter in en_text:
        indx = key.index(letter)
        # print(indx)
        dec_text += chars[indx]
        # print(key[indx])
    
    print(f'decrypted text is {dec_text}')
    
def main():
    Encrypt()
    Decrypt()

if __name__== "__main__":
    main()
    
