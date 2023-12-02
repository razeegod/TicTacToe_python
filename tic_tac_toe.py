def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all([i == player for i in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
            return True
    return False

def get_data():
    while True:
        row = int(input("Введите номер строки(целое число!): "))
        col = int(input("Введите номер столбца(целое число!): "))

        if row in range(1,4) and col in range(1,4):
            row -= 1
            col -= 1
            return row, col
        else:
            print("Неверный ввод! Введите ещё раз:")
            continue

def main_game():
    board = [[" " for i in range(3)] for i in range(3)]
    current_player = "x"
    moves = 0
    while True:
        print_board(board)
        row, col = get_data()
        if board[row][col] == " ":
            board[row][col] = current_player
            moves += 1
        else:
            print("Клетка уже занята. Попробуйте другую клетку!")
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"Победил игрок {current_player}!")
            break

        if moves == 9:
            print_board(board)
            print("Ничья!")
            break

        current_player = "o" if current_player == "x" else "x"

main_game()