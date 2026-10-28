# Chapter 9, Problem 2 — Polybius Checkerboard (list of lists + tuples, based on Ch 8 Problem 5)
# The checkerboard is now a list of lists, and locateLetter returns a tuple (row, col).

def locateLetter(grid, letter):
    row = 0
    while row < len(grid):
        col = 0
        while col < len(grid[row]):
            if grid[row][col] == letter:
                return (row, col)
            col = col + 1
        row = row + 1
    return (-1, -1)

def encrypt(grid, message):
    message = message.upper()
    codes = []
    i = 0
    while i < len(message):
        ch = message[i]
        if ch == "Z":
            ch = "Y"
        if ch.isalpha():
            location = locateLetter(grid, ch)
            codes.append(location)
        i = i + 1
    return codes

def decrypt(grid, codes):
    plaintext = ""
    i = 0
    while i < len(codes):
        row, col = codes[i]
        plaintext = plaintext + grid[row][col]
        i = i + 1
    return plaintext

def main():
    grid = [
        ["A", "B", "C", "D", "E"],
        ["F", "G", "H", "I", "J"],
        ["K", "L", "M", "N", "O"],
        ["P", "Q", "R", "S", "T"],
        ["U", "V", "W", "X", "Y"],
    ]

    message = input("Enter a message to encrypt (letters only, no spaces): ")
    codes = encrypt(grid, message)
    print()
    print("Encrypted message (row, col) pairs:", codes)

    plaintext = decrypt(grid, codes)
    print("Decrypted message:", plaintext)

main()
