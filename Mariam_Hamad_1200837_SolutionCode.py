#MARIAM HAMAD 1200837  & LEENA AFFOURI 1200335
#We certify that this submission is the original work of members of the group and meets
#the Faculty's Expectations of Originality

import time
from random import random
import turtle
# Constants
Width_Size = 800
Height_Size = 850
Square_Size = 75
EMPTY = " "
First_Star = '■'
Second_Star= '□'
#_________________________________________________
#BOREDS PART
# Initialize turtle
Board_Page = turtle.Screen() #create screen of bored that we put size and background and tiHtle.
Board_Page.title("Board Game -  MARYAM: 1200837 & LEENA: 1200335")
Board_Page.setup(Width_Size, Height_Size)
Board_Page.bgcolor("white")

Board_Object = turtle.Turtle() #create individual turtle object that can move and draw on the screen.
Board_Object.speed(0) #fastest speed
Board_Object.hideturtle()

def draw_board():
    # Set up the screen
    Turtle_Page = turtle.Screen()
    Turtle_Page.tracer(0)

    # Set up the turtle pen
    Board_Object = turtle.Turtle()
    Board_Object.color("black")
    Board_Object.pensize(2)
    Board_Object.hideturtle()

    # Draw the board grid
    for i in range(8):
        for j in range(8):
            x = -300 + j * Square_Size
            y = 300 - i * Square_Size

            # Determine the fill color based on the square's position
            if (i + j) % 2 == 0:
                fill_color = "#E6E6FA"
            else:
                fill_color = "white"

            # Draw the square with fill color
            Board_Object.penup()
            Board_Object.goto(x, y)
            Board_Object.pendown()
            Board_Object.fillcolor(fill_color)
            Board_Object.begin_fill()
            for _ in range(4):
                Board_Object.forward(Square_Size)
                Board_Object.right(90)
            Board_Object.end_fill()

    # Draw the alphanumeric labels
    Labell = turtle.Turtle()
    Labell.color("black")
    Labell.penup()
    Labell.hideturtle()

    # Draw letters A to H above and below the chessboard
    label_x = -300 + Square_Size / 2
    label_y_top = 300 + Square_Size / 2 - 15
    label_y_bottom = -300 - Square_Size / 2 - 10
    Labell.color("#660099")
    for letter in "ABCDEFGH":
        # Draw above the chessboard
        Labell.goto(label_x, label_y_top)
        Labell.write(letter, align="center", font=("Arial", 14, "bold"))

        # Draw below the chessboard
        Labell.goto(label_x, label_y_bottom)
        Labell.write(letter, align="center", font=("Arial", 14, "bold"))

        label_x += Square_Size

    # Draw numbers 1 to 8 to the left and right of the chessboard
    label_x_left = -325
    label_x_right = 325
    label_y = 300 - Square_Size / 2
    for number in range(8, 0, -1):
        # Draw to the left of the chessboard
        Labell.goto(label_x_left, label_y)
        Labell.write(str(number), align="center", font=("Arial", 14, "bold"))

        # Draw to the right of the chessboard
        Labell.goto(label_x_right, label_y)
        Labell.write(str(number), align="center", font=("Arial", 14, "bold"))

        label_y -= Square_Size
        # Draw the title
        # Draw the title
    Title = turtle.Turtle()
    Title.color("#3A66B3")
    Title.penup()
    Title.goto(0, 385)  # Adjust the y-coordinate (370) to move the title higher
    Title.write("Welcome to My Magnetic Cave Game", align="center", font=("Open Sans", 18, "bold"))

    # Update the screen
    Turtle_Page.update()
    Turtle_Page.tracer(1)

def draw_piece(row, col, piece):
    # Draw a piece on the board at the given position
    x = -300 + col * Square_Size + Square_Size // 2
    y = 300 - row * Square_Size - Square_Size // 2 - 5

    Board_Object.penup()

    # Adjust the x and y coordinates to center the star
    x += Square_Size // 2 - 65
    y -= Square_Size // 2 - 48

    Board_Object.goto(x, y)

    if piece == First_Star:
        Board_Object.color("#5D4275")
        Board_Object.fillcolor("#5D4275")
    elif piece == Second_Star:
        Board_Object.color("#3A66B3")
        Board_Object.fillcolor("#3A66B3")
    else:
        return

    # Calculate the size for the star
    star_size = 60  # Adjust the star size as desired
    Board_Object.begin_fill()
    for _ in range(5):
        Board_Object.forward(star_size)
        Board_Object.right(144)
    Board_Object.end_fill()



def display_board(board):
    # Clear the previous piece
    Board_Object.clear()

    # Draw the current board
    draw_board()

    # Draw the pieces on the board
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != EMPTY:
                draw_piece(row, col, piece)
EMPTY = 0
First_Star = 1  # ■
Second_Star = 2  # □

# Initialize the game board
board = [[EMPTY] * 8 for _ in range(8)]
winning_combinations = [
    # Rows
    [[(row, col + i) for i in range(5)] for row in range(8) for col in range(4)],

    # Columns
    [[(row + i, col) for i in range(5)] for col in range(8) for row in range(4)],

    # Diagonals
    [[(i, i + j) for j in range(5)] for i in range(4) for j in range(4)],
    [[(i, 4 - i + j) for j in range(5)] for i in range(4) for j in range(4)]
]

def create_board():
    return [[EMPTY] * 8 for _ in range(8)]

def display_board(board):
    print("   A B C D E F G H")
    for i in range(8):
        row_str = " ".join(["■" if cell == First_Star else "□" if cell == Second_Star else " " for cell in board[i]])
        print(f"{8 - i} |{row_str}|")
    print("   A B C D E F G H")

#___________________________________________________________________________________________________
#PLAY RULE

def Check_Win_Player(board):
    # Check rows
    for row in range(8):
        for col in range(4):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] == board[row][col + 4] != EMPTY:
                return board[row][col]

    # Check columns
    for col in range(8):
        for row in range(4):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] == board[row + 4][col] != EMPTY:
                return board[row][col]

    # Check diagonal (top left to bottom right)
    for row in range(4):
        for col in range(4):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] == board[row + 4][col + 4] != EMPTY:
                return board[row][col]

    # Check diagonal (top right to bottom left)
    for row in range(4):
        for col in range(4, 8):
            if board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board[row + 3][col - 3] == board[row + 4][col - 4] != EMPTY:
                return board[row][col]

    return EMPTY


def To_Make_MOVE(board, player, move):
    row, col = move
    new_board = [row[:] for row in board]
    new_board[row][col] = player

    # Check diagonals
    if row > 0 and col > 0 and board[row - 1][col - 1] == player:
        new_board[row - 1][col - 1] = player
    if row > 0 and col < len(board[row]) - 1 and board[row - 1][col + 1] == player:
        new_board[row - 1][col + 1] = player
    if row < len(board) - 1 and col > 0 and board[row + 1][col - 1] == player:
        new_board[row + 1][col - 1] = player
    if row < len(board) - 1 and col < len(board[row]) - 1 and board[row + 1][col + 1] == player:
        new_board[row + 1][col + 1] = player

    return new_board


def IS_MOVE_CAN(board, player, position):
    row, col = position

    if col == 0:  # Left wall
        return True
    elif col == 7:  # Right wall
        return True
    else:
        if board[row][col - 1] != EMPTY or board[row][col + 1] != EMPTY:  # Check adjacent columns
            return True
        if board[row][col] != EMPTY:  # Check current position
            return True

    return False


def Score_In_Boarrd(board):
    score = 0
    for comb in winning_combinations:
        for pattern in comb:
            cells = [board[row][col] for row, col in pattern if 0 <= row < 8 and 0 <= col < 8]
            if cells.count(First_Star) == 5:
                score += 100
            elif cells.count(Second_Star) == 5:
                score -= 100
    return score

def Score_In_Boarrd_FAI(board):
    score = 0
    for comb in winning_combinations:
        for pattern in comb:
            cells = [board[row][col] for row, col in pattern if 0 <= row < 8 and 0 <= col < 8]
            if cells.count(Second_Star) == 5:
                score += 100
            elif cells.count(First_Star) == 5:
                score -= 100
    return score

def Min_Max_Algho_fai(board, depth, minmax_player):
    # Minimax algorithm
    Winn = Check_Win_Player(board)
    if depth == 0 or Winn is not None:
        return Score_In_Boarrd_FAI(board)

    if minmax_player:
        Max_value = float("-inf")
        for col in range(8):
            for row in range(8):
                if board[row][col] == EMPTY and IS_MOVE_CAN(board, Second_Star, (row, col)):
                    new_board = To_Make_MOVE(board, Second_Star, (row, col)) #make the move
                    value = Min_Max_Algho_fai(new_board, depth - 1, False)
                    Max_value = max(Max_value, value)  #updat max value
        return Max_value
    else:
        Min_value= float("inf")
        for col in range(8):
            for row in range(8):
                if board[row][col] == EMPTY and IS_MOVE_CAN(board, First_Star, (row, col)):
                    new_board = To_Make_MOVE(board, First_Star, (row, col))   #make the move
                    value = Min_Max_Algho_fai(new_board, depth - 1, True)
                    Min_value= min(Min_value, value)   #updat min value
        return Min_value



def Min_Max_Algho(board, depth, minmax_player):
    # Minimax algorithm
    Winn = Check_Win_Player(board)
    if depth == 0 or Winn is not None:
        return Score_In_Boarrd(board)

    if minmax_player:
        Max_value = float("-inf")
        for col in range(8):
            for row in range(8):
                if board[row][col] == EMPTY and IS_MOVE_CAN(board, First_Star, (row, col)):
                    new_board = To_Make_MOVE(board, First_Star, (row, col)) #make the move
                    value = Min_Max_Algho(new_board, depth - 1, False)
                    Max_value = max(Max_value, value)  #updat max value
        return Max_value
    else:
        Min_value= float("inf")
        for col in range(8):
            for row in range(8):
                if board[row][col] == EMPTY and IS_MOVE_CAN(board, Second_Star, (row, col)):
                    new_board = To_Make_MOVE(board, Second_Star, (row, col))   #make the move
                    value = Min_Max_Algho(new_board, depth - 1, True)
                    Min_value= min(Min_value, value)   #updat min value
        return Min_value


def get_best_move_Fai(board):
    # prevent manual player to win
    for col in range(8):
        for row in range(8):
            if board[row][col] == EMPTY and IS_MOVE_CAN(board, Second_Star, (row, col)):
                new_board = To_Make_MOVE(board, Second_Star, (row, col))
                if Check_Win_Player(new_board) ==Second_Star:
                    return row, col

    # If the manual in original cannot win, use the original minmax
    depth = 1
    best_move = None
    start_time = time.time()
    while time.time() - start_time < 2:  #limit on auto player time to play
        Best_Scoree = float("-inf")
        for col in range(8):
            for row in range(8):
                if board[row][col] == EMPTY and IS_MOVE_CAN(board, First_Star, (row, col)): #if can move
                    new_board = To_Make_MOVE(board, First_Star, (row, col))  #move
                    score = Min_Max_Algho_fai(new_board, depth, False)  #get score to determine best move
                    if score > Best_Scoree:
                        Best_Scoree = score  #if score larger get it the best score to make best move
                        best_move = (row, col)
        depth += 1
    if best_move is None:  #if cannot find the best move
        Valid_MOV = []
        for col in range(8):
            for row in range(8):
                if board[row][col] == EMPTY and IS_MOVE_CAN(board, First_Star, (row, col)):
                    Valid_MOV.append((row, col))  #put all valid move for auto to choose one move from it as randomly
        if Valid_MOV:
            best_move = random.choice(Valid_MOV)
    return best_move


def get_best_move(board):
    # prevent manual player to win
    for col in range(8):
        for row in range(8):
            if board[row][col] == EMPTY and IS_MOVE_CAN(board, First_Star, (row, col)):
                new_board = To_Make_MOVE(board, First_Star, (row, col))
                if Check_Win_Player(new_board) == First_Star:
                    return row, col

    # If the manual in original cannot win, use the original minmax
    depth = 1
    best_move = None
    start_time = time.time()
    while time.time() - start_time < 2:  #limit on auto player time to play
        Best_Scoree = float("-inf")
        for col in range(8):
            for row in range(8):
                if board[row][col] == EMPTY and IS_MOVE_CAN(board, Second_Star, (row, col)): #if can move
                    new_board = To_Make_MOVE(board, Second_Star, (row, col))  #move
                    score = Min_Max_Algho(new_board, depth, False)  #get score to determine best move
                    if score > Best_Scoree:
                        Best_Scoree = score  #if score larger get it the best score to make best move
                        best_move = (row, col)
        depth += 1
    if best_move is None:  #if cannot find the best move
        Valid_MOV = []
        for col in range(8):
            for row in range(8):
                if board[row][col] == EMPTY and IS_MOVE_CAN(board, Second_Star, (row, col)):
                    Valid_MOV.append((row, col))  #put all valid move for auto to choose one move from it as randomly
        if Valid_MOV:
            best_move = random.choice(Valid_MOV)
    return best_move



def play_game():
    First_Player = input("Select mode for Player 1 - purple star (manual/auto): ")
    Second_Player = input("Select mode for Player 2 - blue star(manual/auto): ")
    board = create_board()
    draw_board()  # Initial drawing of the board
    display_board(board)
    while True:
        # Fisrt player turn
        if First_Player == "manual":
            while True:

                Input_Column = input("Enter column (A-H) to place ■ or 'Q' to quit: ")
                if Input_Column.lower() == 'q':
                    return
                if Input_Column.upper() not in 'ABCDEFGH':
                    print("Invalid input. Please enter a valid column (A-H) or 'Q' to quit.")
                    continue
                col = ord(Input_Column.upper()) - ord('A')

                Input_Row = input("Enter row (1-8) to place ■: ")
                if not Input_Row.isdigit() or int(Input_Row) not in range(1, 9):
                    print("Invalid input. Please enter a valid row (1-8).")
                    continue
                row = 8 - int(Input_Row)

                if board[row][col] != EMPTY:
                    print("Invalid move. The position is already occupied. Please choose another position.")
                    continue

                if IS_MOVE_CAN(board, First_Star, (row, col)):
                    board = To_Make_MOVE(board, First_Star, (row, col))
                    break
                else:
                    print("Invalid move. Must be attracted with the wall. Please choose another position")
                # Auto turn
        else:

                Auto_Move = get_best_move_Fai(board)
                row, col = Auto_Move
                board = To_Make_MOVE(board, First_Star, Auto_Move)

                display_board(board)
                draw_piece(row, col, First_Star)  # Draw the AI's piece on the interface

                Winn = Check_Win_Player(board)
                if Winn == First_Star:
                    print("Congratulations the first player (purple) won")
                    return
                elif Winn == First_Star:
                    print("Congratulations the second player (blue) won!")
                    return
                elif all(cell != EMPTY for row in board for cell in row):
                    print("It's a tie!")
                    return
        display_board(board)
        draw_piece(row, col, First_Star)  # Draw the player's piece on the interface

        Winn = Check_Win_Player(board)
        if Winn == First_Star:
            print("Congratulations the first player (purple) won")
            return
        elif Winn == Second_Star:
            print("Congratulations the second player (blue) won!")
            return
        elif all(cell != EMPTY for row in board for cell in row):
            print("It's a tie!")
            return

        #__________________________________________
        #Second player turn

        if Second_Player == "manual":
            while True:

                Input_Column = input("Enter column (A-H) to place ■ or 'Q' to quit: ")
                if Input_Column.lower() == 'q':
                    return
                if Input_Column.upper() not in 'ABCDEFGH':
                    print("Invalid input. Please enter a valid column (A-H) or 'Q' to quit.")
                    continue
                col = ord(Input_Column.upper()) - ord('A')

                Input_Row = input("Enter row (1-8) to place ■: ")
                if not Input_Row.isdigit() or int(Input_Row) not in range(1, 9):
                    print("Invalid input. Please enter a valid row (1-8).")
                    continue
                row = 8 - int(Input_Row)

                if board[row][col] != EMPTY:
                    print("Invalid move. The position is already occupied. Please choose another position.")
                    continue

                if IS_MOVE_CAN(board, Second_Star, (row, col)):
                    board = To_Make_MOVE(board, Second_Star, (row, col))
                    break
                else:
                    print("Invalid move. Must be attracted with the wall. Please choose another position")
                # Auto player turn
        else:
                Auto_Move = get_best_move(board)
                row, col = Auto_Move
                board = To_Make_MOVE(board, Second_Star, Auto_Move)

                display_board(board)
                draw_piece(row, col, Second_Star)  # Draw the AI's piece on the interface

                Winn = Check_Win_Player(board)
                if Winn == First_Star:
                    print("Congratulations the first player (purple) won")
                    return
                elif Winn == Second_Star:
                    print("Congratulations the second player (blue) won!")
                    return
                elif all(cell != EMPTY for row in board for cell in row):
                    print("It's a tie!")
                    return
        display_board(board)
        draw_piece(row, col, Second_Star)  # Draw the player's piece on the interface

        Winn = Check_Win_Player(board)
        if Winn == First_Star:
            print("Congratulations the first player (purple) won!")
            return
        elif Winn == Second_Star:
            print("Congratulations the second player (blue) won!")
            return
        elif all(cell != EMPTY for row in board for cell in row):
            print("It's a tie!")
            return



if __name__ == "__main__":
    play_game()

    # Keep the turtle window open until it is closed by the user
    turtle.done()
