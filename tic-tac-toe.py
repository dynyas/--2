import random

# 3x3 보드
board = [[' ' for x in range(3)] for y in range(3)]


def print_board():
    """현재 보드 상태를 출력하는 함수"""
    for r in range(3):
        print(" " + board[r][0] + " | " + board[r][1] + " | " + board[r][2])
        if r != 2:
            print("---|---|---")


def check_winner(symbol):
    """주어진 심볼(X 또는 O)이 승리했는지 확인하는 함수"""
    # 가로
    for i in range(3):
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            return True
    # 세로
    for j in range(3):
        if board[0][j] == symbol and board[1][j] == symbol and board[2][j] == symbol:
            return True
    # 대각선
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    return False


def is_draw():
    """보드가 모두 채워졌는지 (무승부인지) 확인하는 함수"""
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def computer_move():
    """컴퓨터(O)가 빈 칸 중 하나를 무작위로 선택하여 두는 함수"""
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = "O"


print("=== Tic-Tac-Toe ===")
print("당신은 'X', 컴퓨터는 'O' 입니다.")
print("행과 열은 0, 1, 2 중에서 입력하세요.\n")

while True:
    print_board()

    # 사용자(X)의 입력
    try:
        x = int(input("행 번호를 입력하세요 (0-1-2): "))
        y = int(input("열 번호를 입력하세요 (0-1-2): "))
    except ValueError:
        print("숫자만 입력해주세요.\n")
        continue

    if x < 0 or x > 2 or y < 0 or y > 2:
        print("그런 위치는 없습니다.\n")
        continue

    if board[x][y] != ' ':
        print("이미 채워진 칸입니다.\n")
        continue
    else:
        board[x][y] = "X"

    # X 승리
    if check_winner("X"):
        print_board()
        print("\nX가 승리했습니다! 축하합니다!")
        break

    # 무승부
    if is_draw():
        print_board()
        print("\n무승부입니다!")
        break

    # 컴퓨터(O)의 차례
    computer_move()

    # O 승리 확인
    if check_winner("O"):
        print_board()
        print("\nO(컴퓨터)가 승리했습니다!")
        break

    # 무승부 확인
    if is_draw():
        print_board()
        print("\n무승부입니다!")
        break

print("\n게임이 종료되었습니다.")
