"""
Function that decrypts the encrypted file
and prints the original file in terminal
"""
def decryptFile(filename):
    file = open(filename, "r")
    line = file.readline()
    while (line != ""):
        for char in line:
            char_ascii = ord(char)
            des_char = chr(char_ascii - 20)
            print(des_char, end="")

if __name__ == "__main__":
    filename = sys.argv[1]
    decryptFile(filename)