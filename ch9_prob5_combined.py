# Chapter 9, Problem 5 — Combined Keyword + Path Cipher
# Combines Problem 3's keyword column ordering with Problem 4's zigzag path idea:
# columns are visited in the order given by the keyword, and each column is read
# top-to-bottom or bottom-to-top depending on its position in that order.

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

def buildPath(order, numRows, numCols):
    path = []
    colNum = 1
    while colNum <= numCols:
        col = 0
        while col < numCols:
            if order[col] == colNum:
                if colNum % 2 == 1:
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
        colNum = colNum + 1
    return path

def encipher(message, keyword):
    message = message.upper()
    keyword = keyword.upper()
    numCols = len(keyword)
    numRows = (len(message) + numCols - 1) // numCols
    totalLength = numRows * numCols
    message = padMessage(message, totalLength)
    grid = buildGrid(message, numRows, numCols)
    order = getColumnOrder(keyword)
    path = buildPath(order, numRows, numCols)

    ciphertext = ""
    i = 0
    while i < len(path):
        row, col = path[i]
        ciphertext = ciphertext + grid[row][col]
        i = i + 1
    return ciphertext

def decipher(ciphertext, keyword, numRows):
    keyword = keyword.upper()
    numCols = len(keyword)
    order = getColumnOrder(keyword)
    path = buildPath(order, numRows, numCols)

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

    i = 0
    while i < len(path):
        row, col = path[i]
        grid[row][col] = ciphertext[i]
        i = i + 1

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
