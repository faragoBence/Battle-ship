import sys
import os
import getchfile
import random


def longshipaddy(gameBoard, ship, num, y, x):  # if way is down, we add to y
    count = 1
    while count < num:
        y += 1
        gameBoard[y][x] = "X"
        ship[count].append(x)
        ship[count].append(y)
        count += 1


def longshipminusy(gameBoard, ship, num, y, x):  # if way is up, we substract from y
    count = 1
    while count < num:
        y -= 1
        gameBoard[y][x] = "X"
        ship[count].append(x)
        ship[count].append(y)
        count += 1


def longshipaddx(gameBoard, ship, num, y, x):  # if way is right, we add to x
    count = 1
    while count < num:
        x += 1
        gameBoard[y][x] = "X"
        ship[count].append(x)
        ship[count].append(y)
        count += 1


def longshipminusx(gameBoard, ship, num, y, x):  # if way is left, we substract from x
    count = 1
    while count < num:
        x -= 1
        gameBoard[y][x] = "X"
        ship[count].append(x)
        ship[count].append(y)
        count += 1


def wayinput(gameBoard, ship, num, y, x, computergame):  # checks which way you want your ship to go towards

    while True:
        cpu_way = ["left", "right", "up", "down"]
        checkNumber = 0
        if computergame == False:
            way = input("Choose on option from these:up,down,right,left:")
        else:
            way = random.choice(cpu_way)
        if way == "up"and y >= (num - 1):
            for shipCheck in range(1, num):
                try:
                    if gameBoard[y - shipCheck][x] == "~" and gameBoard[y - shipCheck][x - 1] == "~" and gameBoard[y - shipCheck][x + 1] == "~" and gameBoard[y - num][x] == "~":
                        checkNumber += 1
                except IndexError:
                    checkNumber += 1

            if checkNumber == num - 1:
                gameBoard[y][x] = "X"
                ship[0].append(x)
                ship[0].append(y)
                longshipminusy(gameBoard, ship, num, y, x)
            else:
                print("Invalid coordinates")
                continue
            break

        elif way == "down" and y <= 10 - (num - 1):
            for shipCheck in range(1, num):
                try:
                    if gameBoard[y + shipCheck][x] == "~" and gameBoard[y + shipCheck][x - 1] == "~" and gameBoard[y + shipCheck][x + 1] == "~" and gameBoard[y + num][x] == "~":
                        checkNumber += 1
                except IndexError:
                    checkNumber += 1

            if checkNumber == num - 1:
                gameBoard[y][x] = "X"
                ship[0].append(x)
                ship[0].append(y)
                longshipaddy(gameBoard, ship, num, y, x)
            else:
                print("Invalid coordinates")
                continue
            break

        elif way == "left" and x >= (num - 1):
            for shipCheck in range(1, num):
                try:
                    if gameBoard[y][x - shipCheck] == "~" and gameBoard[y + 1][x - shipCheck] == "~" and gameBoard[y - 1][x - shipCheck] == "~" and gameBoard[y][x - num] == "~":
                        checkNumber += 1
                except IndexError:
                    checkNumber += 1
            if checkNumber == num - 1:
                gameBoard[y][x] = "X"
                ship[0].append(x)
                ship[0].append(y)
                longshipminusx(gameBoard, ship, num, y, x)
            else:
                print("Invalid coordinates")
                continue
            break
        elif way == "right" and x <= 10 - (num - 1):
            for shipCheck in range(1, num):
                try:
                    if gameBoard[y][x + shipCheck] == "~" and gameBoard[y - 1][x + shipCheck] == "~" and gameBoard[y + 1][x + shipCheck] == "~" and gameBoard[y][x + num] == "~":
                        checkNumber += 1
                except IndexError:
                    checkNumber += 1
            if checkNumber == num - 1:
                gameBoard[y][x] = "X"
                ship[0].append(x)
                ship[0].append(y)
                longshipaddx(gameBoard, ship, num, y, x)
            else:
                print("Invalid coordinates")
                continue
            break

        else:
            print("\nInvalid coordinates\n")


def firstcoordinates(gameBoard, ship, num, computergame):  # put first coordinates to lists
    battleBoard(gameBoard)
    while True:
        while True:

            try:
                if computergame == False:
                    x = int(input("Give your " + str(num) + " unit ship's x coordinate: "))
                else:
                    x = random.randint(1, 10)
                if 0 > x or x > 10:
                    print("\nInvalid coordinate(out of board)\n")
                    continue
            except:
                print("Wrong coordinates")
                continue
            break
        while True:
            try:
                if computergame == False:
                    y = int(input("Give your " + str(num) + " unit ship's y coordinate: "))
                else:
                    y = random.randint(1, 10)
                if 0 > y or y > 10:
                    print("\nInvalid coordinate(out of board)\n")
                    continue
            except:
                print("Wrong coordinates")
                continue
            break

        if x == 10 and y == 10:
            if gameBoard[y][x] != "~" or gameBoard[y][x - 1] == "X" or gameBoard[y - 1][x] == "X":
                print("\nInvalid coordinates\n")
                continue
            else:
                break
        elif x == 10:
            if gameBoard[y][x] != "~" or gameBoard[y][x - 1] == "X" or gameBoard[y + 1][x] == "X" or gameBoard[y - 1][x] == "X":
                print("\nInvalid coordinates\n")
                continue
            else:
                break
        elif y == 10:
            if gameBoard[y][x] != "~" or gameBoard[y][x - 1] == "X" or gameBoard[y][x + 1] == "X" or gameBoard[y - 1][x] == "X":
                print("\nInvalid coordinates\n")
                continue
            else:
                break
        else:
            if gameBoard[y][x] != "~" or gameBoard[y][x - 1] == "X" or gameBoard[y][x + 1] == "X" or gameBoard[y + 1][x] == "X" or gameBoard[y - 1][x] == "X":
                print("\nInvalid coordinates\n")
                continue
            else:
                break
    if num == 1:
        gameBoard[y][x] = "X"
        ship[0].append(x)
        ship[0].append(y)
    elif num > 1:
        wayinput(gameBoard, ship, num, y, x, computergame)


def battleBoard(p):  # printing out the game board

    for i in range(11):
        for j in range(11):
            # SORSZÁMOK KIÍRÁSA A TÁBLA TETEJÉRE
            if i == 0:
                if j == 0:
                    sys.stdout.write(str(j) + '   ')

                if j == 10:
                    sys.stdout.write(str(j) + '\n\n')
                elif j < 9:
                    sys.stdout.write(str(j + 1) + ' ')
            # ---------------------------------------
            # SORSZÁMOK KIÍRÁSA A TÁBLA SZÉLÉRE
            elif j == 0 and i != 10:
                sys.stdout.write(str(i) + '   ')
            elif j == 0:
                sys.stdout.write(str(i) + '  ')
            # ---------------------------------------
            elif j == 10:
                sys.stdout.write(str(p[i][j]) + '\n')
            else:
                sys.stdout.write(str(p[i][j]) + ' ')


def shooting(board, ship, x_coordinate, y_coordinate, computergame):  # this function handles shooting
    global destroyed

    shootArray = []
    shootArray.append(int(x_coordinate))
    shootArray.append(int(y_coordinate))
    for c in range(len(ship)):
        if ship[c] == shootArray:
            ship.pop(c)
            board[y_coordinate][x_coordinate] = "X"

            if computergame == True:
                f = open("cpushot.txt", "w")
                f.write(((str(shootArray).strip("[")).strip("]")).replace(" ", ""))
                f.close()

            if len(ship) == 0:
                destroyed = 1
                if computergame == True:
                    f = open("cpushot.txt", "w")
                    f.write("")
                    f.close()
            break

    if board[y_coordinate][x_coordinate] == "~":
        board[y_coordinate][x_coordinate] = "O"


def winner(shiplist):  # this function helps checking if someone has won
    return len(shiplist)


def menuPrint(list1, list2):
    for k in range(len(list1)):
        print(list1[k] + " " + list2[k])


def scoreBoard():
    f = open("scoreboard.txt", "r")
    score = {}
    for line in f:
        tmp_list = line.split(",")
        score[tmp_list[0]] = int(tmp_list[1].strip("\n"))

    print("name".rjust(9) + "score".rjust(8))
    print("-" * 17)
    for item in sorted(score, key=score.get, reverse=False):
        print(item.rjust(9) + str(score[item]).rjust(6))
    print("-" * 17)


def menu():
    menuList = ["x", " ", " ", " "]
    menuNames = ["Player vs Player", "Player vs AI", "scoreboard", "exit"]
    while True:
        os.system("clear")
        menuPrint(menuList, menuNames)
        x = getchfile.getch()
        try:
            if x == "w":
                for x in range(len(menuList)):
                    if menuList[x] == "x":
                        menuList[x - 1] = "x"
                        menuList[x] = " "
                        break
                menuPrint(menuList, menuNames)
            elif x == "s":
                for x in range(len(menuList)):
                    if menuList[x] == "x":
                        menuList[x + 1] = "x"
                        menuList[x] = " "
                        break
                menuPrint(menuList, menuNames)

            elif ord(x) == 13:
                if menuList[0] == "x":
                    computer_game = False
                    pvp(computer_game)
                    break
                if menuList[1] == "x":
                    computer_game = True
                    pvp(computer_game)
                    break
                if menuList[2] == "x":
                    os.system("clear")
                    scoreBoard()

                    while True:
                        print("Press b to go back to menu")
                        back = getchfile.getch()
                        if back == "b":
                            break

                if menuList[3] == "x":
                    sys.exit()

        except IndexError:
            continue


def pvp(computergame):
    global destroyed
    human = False
    os.system("clear")
    player_one = input("Player one, type in your name: ")
    os.system("clear")
    if computergame == False:
        player_two = input("Player two, type in your name: ")
        os.system("clear")
    else:
        player_two = "CPU"
        os.system("clear")
    num = 1
    count = 0
    # 1st player placing
    print(player_one + " , PLACE YOUR SHIPS\n")
    firstcoordinates(board1placed, p1_s1, num, human)  # 1 unit ship
    num += 1

    os.system("clear")
    print(player_one + " , PLACE YOUR SHIPS\n")
    firstcoordinates(board1placed, p1_s2, num, human)  # 2 unit ship
    num += 1

    os.system("clear")
    print(player_one + " , PLACE YOUR SHIPS\n")
    firstcoordinates(board1placed, p1_s3, num, human)  # 3 unit ship

    os.system("clear")
    print(player_one + " , PLACE YOUR SHIPS\n")
    firstcoordinates(board1placed, p1_s3v2, num, human)  # 3 unit ship

    num += 1

    os.system("clear")
    print(player_one + " , PLACE YOUR SHIPS\n")
    firstcoordinates(board1placed, p1_s4, num, human)  # 4 unit ship
    num += 1

    os.system("clear")
    print("SHIPS PLACED\n")
    battleBoard(board1placed)
    num = 1

    while True:
        player_change = input("Press enter to continue")
        if player_change == "":
            os.system('clear')
            break

    # 2nd player placing
    if computergame == False:
        print(player_two + " , PLACE YOUR SHIPS\n")
    firstcoordinates(board2placed, p2_s1, num, computergame)  # 1 unit ship
    num += 1

    os.system("clear")
    if computergame == False:
        print(player_two + " , PLACE YOUR SHIPS\n")
    firstcoordinates(board2placed, p2_s2, num, computergame)  # 2 unit ship
    num += 1

    os.system("clear")
    if computergame == False:
        print(player_two + " , PLACE YOUR SHIPS\n")
    firstcoordinates(board2placed, p2_s3, num, computergame)  # 3 unit ship

    os.system("clear")
    if computergame == False:
        print(player_two + " , PLACE YOUR SHIPS\n")
    firstcoordinates(board2placed, p2_s3v2, num, computergame)  # 3 unit ship

    num += 1

    os.system("clear")
    if computergame == False:
        print(player_two + " , PLACE YOUR SHIPS\n")
    firstcoordinates(board2placed, p2_s4, num, computergame)  # 4 unit ship
    num += 1

    os.system("clear")
    if computergame == False:
        print("SHIPS PLACED\n")
        battleBoard(board2placed)

    while True:
        start = input("\nPress enter to start")
        if start == "":
            os.system('clear')
            break

    turn_count = 0
    player = 1
    if_winning = 0
    while True:
        while player == 1:
            shooting_phase(player_one, p2_s1, p2_s2, p2_s3, p2_s4, p2_s3v2, board2, human)
            if winning(player_one, p2_s1, p2_s2, p2_s3, p2_s4, p2_s3v2, turn_count):
                if_winning += 1
                break
            player += 1
            turn_count += 1
        while player == 2:
            shooting_phase(player_two, p1_s1, p1_s2, p1_s3, p1_s4, p1_s3v2, board1, computergame)
            if winning(player_two, p1_s1, p1_s2, p1_s3, p1_s4, p1_s3v2, turn_count):
                if_winning += 1
                break
            player -= 1
            turn_count += 1


def shooting_phase(player_name, ship1, ship2, ship3, ship4, ship5, board, computergame):
    print("\n" + player_name + ", SHOOT!")
    print("""
            X   =  Hit
            O   =  Missed
            ~   =  Sea
                """)

    battleBoard(board)
    global destroyed
    while True:
        if computergame == False:
            try:
                x_coordinate = int(input("\nChoose an x coordinate to shoot at:"))
                y_coordinate = int(input("Choose a y coordinate to shoot at:"))
                if board[y_coordinate][x_coordinate] == "X" or board[y_coordinate][x_coordinate] == "O":
                    print("You have already shot here")
                    continue
            except ValueError:
                print("Wrong input")
                continue
        else:
            f = open("cpushot.txt", "r")
            k = f.read()
            f.close()

            if len(k) == 0:
                x_coordinate = random.randint(1, 10)
                y_coordinate = random.randint(1, 10)
            else:
                prev_c_shot = k.split(",")
                x_coordinate = int(prev_c_shot[0])
                y_coordinate = int(prev_c_shot[1])

                if board[x_coordinate] != 10:
                    if board[y_coordinate][x_coordinate - 1] == "X":
                        x_coordinate += 1
                if board[x_coordinate] != 0:
                    if board[y_coordinate][x_coordinate + 1] == "X":
                        x_coordinate -= 1
                if board[y_coordinate] != 10:
                    if board[y_coordinate - 1][x_coordinate] == "X":
                        y_coordinate += 1
                if board[x_coordinate] != 0:
                    if board[y_coordinate + 1][x_coordinate] == "X":
                        y_coordinate -= 1

                if board[x_coordinate] != 0:
                    if board[y_coordinate][x_coordinate - 1] != "X" and board[y_coordinate][x_coordinate - 1] != "O":
                        x_coordinate -= 1
                if board[x_coordinate] != 10:
                    if board[y_coordinate][x_coordinate + 1] != "X" and board[y_coordinate][x_coordinate + 1] != "O":
                        x_coordinate += 1
                if board[y_coordinate] != 0:
                    if board[y_coordinate - 1][x_coordinate] != "X" and board[y_coordinate - 1][x_coordinate] != "O":
                        y_coordinate -= 1
                if board[y_coordinate] != 10:
                    if board[y_coordinate + 1][x_coordinate] != "X" and board[y_coordinate + 1][x_coordinate] != "O":
                        y_coordinate += 1

            # if board[y_coordinate][x_coordinate] == "X" or board[y_coordinate][x_coordinate] == "O":
            #    continue

        if (x_coordinate > 10 or x_coordinate < 0) or (y_coordinate < 0 or y_coordinate > 10):
            print("Wrong input")
            continue
        break
    shooting(board, ship1, x_coordinate, y_coordinate, computergame)
    shooting(board, ship2, x_coordinate, y_coordinate, computergame)
    shooting(board, ship3, x_coordinate, y_coordinate, computergame)
    shooting(board, ship4, x_coordinate, y_coordinate, computergame)
    shooting(board, ship5, x_coordinate, y_coordinate, computergame)
    os.system('clear')
    battleBoard(board)
    if destroyed == 1:
        print("\nShip destroyed\n")
        if computergame == True:
            f = open("cpushot.txt", "w")
            f.write("")
            f.close()
        destroyed = 0
    if computergame == True:
        print("\nCPU's shot at "+str(x_coordinate)+","+str(y_coordinate))
    passTurn = input("\nPress enter to pass turn")
    if passTurn == "":
        os.system('clear')


def winning(player_name, ship1, ship2, ship3, ship4, ship5, turn_counter):

    if winner(ship1) == 0 and winner(ship2) == 0 and winner(ship3) == 0 and winner(ship4) == 0 and winner(ship5) == 0:
        os.system("clear")
        print("\n" + player_name + " WINS\n")

        print("""
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `'''''''`
        """)
        while True:
            print("\n\npress enter to continue")
            g = getchfile.getch()
            if ord(g) == 13:
                break

        f = open("scoreboard.txt", "a")
        f.write(player_name + "," + str(int(turn_counter / 2)) + "\n")
        f.close
        return True


while True:

    f = open("cpushot.txt", "w")
    f.write("")
    f.close()

    board1 = []
    board1placed = []
    board2 = []
    board2placed = []
    for i in range(11):
        board1.append([])
        board2.append([])
        board1placed.append([])
        board2placed.append([])
        for x in range(11):
            board1[i].append("~")
            board2[i].append("~")
            board1placed[i].append("~")
            # to up from here is the gameboard creating
            board2placed[i].append("~")

    p1_s1 = [[]]  # ----------------------------------------------------------
    p1_s2 = [[], []]  # Coordinates of the first player's ships
    p1_s3 = [[], [], []]
    p1_s3v2 = [[], [], []]         #
    # ----------------------------------------------------------
    p1_s4 = [[], [], [], []]

    p2_s1 = [[]]  # ----------------------------------------------------------
    p2_s2 = [[], []]  # Coordinates of the second player's ships
    p2_s3 = [[], [], []]
    p2_s3v2 = [[], [], []]
    # ----------------------------------------------------------
    p2_s4 = [[], [], [], []]

    destroyed = 0
    player = 1  # This helps to change turns

    menu()
