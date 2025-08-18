board = [["-","-","-"],["-","-","-"],["-","-","-"]]
Xrow = {"0":0,"1":0,"2":0}
Orow = {"0":0,"1":0,"2":0}
Xcol = {"0":0,"1":0,"2":0}
Ocol = {"0":0,"1":0,"2":0}
win = False

def checkWin():
    global win
    for key in Xrow:
        if Xrow[key] == 3:
            win = True
    for key in Xcol:
        if Xcol[key] == 3:
            win = True
    for key in Orow:
        if Orow[key] == 3:
            win = True
    for key in Ocol:
        if Ocol[key] == 3:
            win = True
    if board[0][0] == board[1][1] == board[2][2] != "-":
        win = True
    if board[0][2] == board[1][1] == board[2][0] != "-":
        win = True

def place(symbol, row, col):
    if board[row][col] != "-":
        print("Can't place at this spot, try again")
        return False

    if symbol == "1":
        board[row][col] = "X"
        Xrow[str(row)] += 1
        Xcol[str(col)] += 1
    elif symbol == "2":
        board[row][col] = "O"
        Orow[str(row)] += 1
        Ocol[str(col)] += 1

    return True

def displayBoard():
    for row in board:
        print(row)
    print("\n")

# Game loop
displayBoard()
switch = input("Enter 1 for X, 2 for O to start: ")

while any("-" in row for row in board) and not win:
    try:
        row = int(input("Enter Row (1-3): "))
        col = int(input("Enter Column (1-3): "))
    except ValueError:
        print("Invalid input, enter numbers only.")
        continue

    if row > 3 or col > 3 or row < 1 or col < 1:
        print("Invalid input, please try again.")
        continue

    decision = place(switch, row - 1, col - 1)
    if decision:
        displayBoard()
        checkWin()
        if not win:
            switch = "2" if switch == "1" else "1"

if win:
    winner = "X" if switch == "1" else "O"
    print(f"{winner} wins!")
else:
    print("It's a draw!")

print("Uzair 1BM23CS307")
