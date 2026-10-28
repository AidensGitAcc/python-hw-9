# Chapter 9, Problem 3 — Key Word Columnar Transposition Cipher
# The message is written into a grid, and the keyword determines the order
# in which columns are read off to produce the ciphertext.

import random

def getColumnOrder(keyword):
    keyword = keyword.upper()
    n = len(keyword)
    order = [0] * n
    sortedLetters = sorted(keyword)

    rank = 1
    i = 0
    while i < n:
        letter = sortedLetters[i]
        j = 0
        placed = False
        while j < n and not placed:
            if keyword[j] == letter and order[j] == 0:
                order[j] = rank
                placed = True
            j = j + 1
        rank = rank + 1
        i = i + 1
    return order

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

def encipher(message, keyword):
    message = message.upper()
    keyword = keyword.upper()
    numCols = len(keyword)
    numRows = (len(message) + numCols - 1) // numCols
    totalLength = numRows * numCols
    message = padMessage(message, totalLength)
    grid = buildGrid(message, numRows, numCols)
    order = getColumnOrder(keyword)

    ciphertext = ""
    colNum = 1
    while colNum <= numCols:
        col = 0
        while col < numCols:
            if order[col] == colNum:
                row = 0
                while row < numRows:
                    ciphertext = ciphertext + grid[row][col]
                    row = row + 1
            col = col + 1
        colNum = colNum + 1
    return ciphertext

def decipher(ciphertext, keyword, numRows):
    keyword = keyword.upper()
    numCols = len(keyword)
    order = getColumnOrder(keyword)

    grid = []
    row = 0
    while row < numRows:
        newRow = []
        col = 0
        while col < numCols:
            newRow.append("")
            col = col + 1
        grid.append(newRow)
        row = row + 1

    index = 0
    colNum = 1
    while colNum <= numCols:
        col = 0
        while col < numCols:
            if order[col] == colNum:
                row = 0
                while row < numRows:
                    grid[row][col] = ciphertext[index]
                    index = index + 1
                    row = row + 1
            col = col + 1
        colNum = colNum + 1

    plaintext = ""
    row = 0
    while row < numRows:
        col = 0
        while col < numCols:
            plaintext = plaintext + grid[row][col]
            col = col + 1
        row = row + 1
    return plaintext

def main():
    message = input("Enter a message to encipher (no spaces): ")
    keyword = input("Enter a keyword: ")

    cipher = encipher(message, keyword)
    print()
    print("Enciphered message:", cipher)

    numCols = len(keyword)
    numRows = len(cipher) // numCols
    plain = decipher(cipher, keyword, numRows)
    print("Deciphered message (includes random padding):", plain)

main()
