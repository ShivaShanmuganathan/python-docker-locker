from cryptography.fernet import Fernet
import ed25519

#Generate Symmetric Key
symKey = Fernet.generate_key()
#create cipher
cipher = Fernet(symKey)


#Generate Asymmetric Keys
privKey, pubKey = ed25519.create_keypair()

#Get Filename to encrypt
filename = input("Enter filename to encrypt [with extension]:\n")

# Encrypt File
file = open(filename, "rb")
msg = file.read()
encrypted_data = cipher.encrypt(msg)
edata = open('encrypted_' + filename,'wb')
edata.write(encrypted_data)
edata.close()
file.close()

message = msg

# SIGN USING MESSAGE FROM FILE GIVEN
signature = privKey.sign(message, encoding='hex')

print("----------------Please Note Down Signature and both the Keys Generated--------------")
print("Signature (64 bytes):", signature)
print("Public key (32 bytes): ", pubKey.to_ascii(encoding='hex'))
print('Check-----> ' + 'encrypted_'+ filename + ' <------to get the encrypted file')


print('\n')

filename = input("Enter filename to decrypt [with extension]:\n")

# Decrypt File
file = open(filename, "rb")
msg = file.read()
decrypted_file = cipher.decrypt(msg)
file.close()

message=decrypted_file

# VERIFY SIGNATURE
try:
    pubKey.verify(signature, message, encoding='hex')
    print("The signature is valid.")
except:
    print("Invalid signature!")

with open('decrypted_'+filename,'wb') as df:
    df.write(decrypted_file)
print('Check-----> ' + 'decrypted_'+ filename + ' <------to get the decrypted file')