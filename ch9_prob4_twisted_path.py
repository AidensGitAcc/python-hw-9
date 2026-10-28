# Chapter 9, Problem 4 — Twisted Path Cipher
# The message fills a fixed-size grid row by row, then is read back out by
# following a path (a list of (row, col) tuples) that zigzags down and up each column.

import random

GRID_ROWS = 5
GRID_COLS = 6

def buildPath(numRows, numCols):
    path = []
    col = 0
    while col < numCols:
        if col % 2 == 0:
            row = 0
            while row < numRows:
                path.append((row, col))
                row = row + 1
        else:
            row = numRows - 1
            while row >= 0:
                path.append((row, col))
                row = row - 1
        col = col + 1
    return path

def padMessage(message, totalLength):
    while len(message) < totalLength:
        message = message + chr(random.randint(65, 90))
    return message

def buildGrid(message, numRows, numCols):
    grid = []
    index = 0
    row = 0
    while row < numRows:
        newRow = []
        col = 0
        while col < numCols:
            newRow.append(message[index])
            index = index + 1
            col = col + 1
        grid.append(newRow)
        row = row + 1
    return grid

def encipher(message):
    message = message.upper()
    totalLength = GRID_ROWS * GRID_COLS
    message = padMessage(message, totalLength)
    grid = buildGrid(message, GRID_ROWS, GRID_COLS)
    path = buildPath(GRID_ROWS, GRID_COLS)

    ciphertext = ""
    i = 0
    while i < len(path):
        row, col = path[i]
        ciphertext = ciphertext + grid[row][col]
        i = i + 1
    return ciphertext

def decipher(ciphertext):
    path = buildPath(GRID_ROWS, GRID_COLS)

    grid = []
    row = 0
    while row < GRID_ROWS:
        newRow = []
        col = 0
        while col < GRID_COLS:
            newRow.append("")
            col = col + 1
        grid.append(newRow)
        row = row + 1

    i = 0
    while i < len(path):
        row, col = path[i]
        grid[row][col] = ciphertext[i]
        i = i + 1

    plaintext = ""
    row = 0
    while row < GRID_ROWS:
        col = 0
        while col < GRID_COLS:
            plaintext = plaintext + grid[row][col]
            col = col + 1
        row = row + 1
    return plaintext

def main():
    maxLength = GRID_ROWS * GRID_COLS
    print("This cipher uses a fixed", GRID_ROWS, "by", GRID_COLS, "grid, so your message can be at most", maxLength, "letters.")
    message = input("Enter a message to encipher (no spaces): ")

    cipher = encipher(message)
    print()
    print("Enciphered message:", cipher)

    plain = decipher(cipher)
    print("Deciphered message (includes random padding):", plain)

main()
