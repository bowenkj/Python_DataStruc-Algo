# Complete the decode function below.
def decode(encoded):
    encoded = encoded[::-1]
    index = 0
    decoded = ""
    while index < len(encoded):
        if encoded[index] == '1':
            decoded += chr(int(encoded[index:index+3]))
            index += 3
        else:
            decoded += chr(int(encoded[index:index+2]))
            index += 2
    return decoded