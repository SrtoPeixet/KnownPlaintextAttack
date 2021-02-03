def xor(a,b):
    y = int(a, 2) ^ int(b, 2)
    out = bin(y)[2:].zfill(len(a))
    return out

def hex_to_bin(data):
    return bin(int(data, 16))[2:].zfill(8)

def getArrOfHexBytes(data):
    output = []
    ctr = 0
    for char in data:
        if (ctr == 0):
            tmp = char
        else:
            output.append(tmp+char)
        ctr = 1 - ctr
    return output


c1 = input('Enter the first ciphertext ... Ex. 7a9939d8f6ce')
c2 = input('Enter the second ciphertext ... Ex. 7a9939d8f6ce')
n = input('Enter number of byes that does not corespond to padding ... Ex. For the above case was 6')
m1_hex = input('Enter your known plaintext ... Ex. 6a61636f626f ')


# Get an array of byes for an easier parse

c1_bytes = getArrOfHexBytes(c1)
c2_bytes = getArrOfHexBytes(c2)

print("No padding bytes (HEX) of c1: ",c1_bytes[:6])
print("No padding bytes (HEX) of c2: ",c2_bytes[:6])

# We want to get the first n bytes that does not contain padding

c1_bin = []
c2_bin = []
xored_ciphers = []

for i in range(n): # Convert HEX ciphers to BINARY and XOR both
    c1_bin.append(hex_to_bin(c1_bytes[i]))
    c2_bin.append(hex_to_bin(c2_bytes[i]))
    xored_ciphers.append(xor(c1_bin[i],c2_bin[i]))

print("C1 XOR C2")
print(c1_bin)
print(c2_bin)
print((1 + len(c1_bin))*10*'-')
print(xored_ciphers)

# Assuming that m1 is using his name as username let's get it in BINARY

m1_hex_arr = getArrOfHexBytes(m1_hex)
m1_bin = []
xor_m1_xoredCiphers = []
# We will perform a XOR between username in BINARY and (c1 XOR c2) to get the password
for i in range(n): # Convert m1 to BINARY and XOR with the previous XOR result
    m1_bin.append(hex_to_bin(m1_hex_arr[i]))
    xor_m1_xoredCiphers.append(xor(m1_bin[i],xored_ciphers[i]))

print("(C1 XOR C2) XOR Binary(m1)")
print(m1_bin)
print(xored_ciphers)
print((1 + len(c1_bin))*10*'-')
print(xor_m1_xoredCiphers)

# Finaly convert binary password into a ASCII string

password = ""
for byte in xor_m1_xoredCiphers:
    password += chr(int(byte,2))
print("Password: ",password)
