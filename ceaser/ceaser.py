# Using the Python,
# have the function CaesarCipher(str, num) take the str parameter and perform a Caesar Cipher num on it using the num parameter as the numing number.
# A Caesar Cipher works by numing all letters in the string N places down in the alphabetical order (in this case N will be num).
# Punctuation, spaces, and capitalization should remain intact.

# For example if the string is "Caesar Cipher" and num is 2 the output should be "Ecguct Ekrjgt".

# more on cipher visit http://practicalcryptography.com/ciphers/caesar-cipher/
# happy coding :-)


# create a key for encrypting && decrypting
key = 'abcdefghijklmnopqrstuvwxyz'


# create a cipher using the set key
def CaesarCipher(string, n):
    result = ''
    # make sure that all letters are in lower case
    for letter in string.lower():
        try:
            temp = (key.index(letter)+n) % 26
            result += key[temp]
        except ValueError:
            result += letter

    return result.lower()


print CaesarCipher("Hello world", 2)

print "Cipertext:", CaesarCipher("A Crazy fool Z", 1)
