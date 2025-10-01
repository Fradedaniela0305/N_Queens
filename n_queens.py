
def n_queens(n) -> list or False :
    board = generate_default_board(n)
    queen_positions = []
    succeeded = solve(board, 0, n, queen_positions)

    if succeeded:
        return transform_positions(queen_positions, n)
    else:
        return False

def generate_default_board(n) -> list:
    board = []
    for i in range(n):
        board.append([' '] * n)
    return board

def solve(board, row, n, queen_positions) -> bool:
    if row == n: # we got to the last row without killing the branch
        return True
    for col in range(n): #  checking column by column in that row
        place_queen(board, (row, col))
        queen_positions.append((row, col))
        if no_attack(board, n, queen_positions):
            if solve(board, row + 1, n, queen_positions): # Recursive call
                return True
        remove_queen(board, (row, col))
        queen_positions.pop()

    return False


def place_queen(board, spot):
    board[spot[0]][spot[1]] = 'Q'

def remove_queen(board, spot):
    board[spot[0]][spot[1]] = ' '

def no_attack(board, n, queen_positions) -> bool:
    for queen_position in queen_positions:
        if not valid_queen_position(board, n, queen_position):
            return False
    return True

def valid_queen_position(board, n, queen_position) -> bool:
    col = get_col(board, n, queen_position)
    left_diagonal = get_left_diagonal(board, n, queen_position) # /
    right_diagonal = get_right_diagonal(board, n, queen_position) # \
    for possible_attack in [col, left_diagonal, right_diagonal]:
        if has_more_queens(possible_attack):
            return False
    return True

def has_more_queens(possible_attack):
    return possible_attack.count("Q") > 1

def get_col(board, n, queen_position):
    col = []
    for row in range(n):
        col.append(board[row][queen_position[1]])
    return col

def get_right_diagonal(board, n, queen_position):
    row, col = queen_position
    right_diagonal = [board[row][col]]
    r, c = row - 1, col + 1
    while r >= 0 and c < n:
        right_diagonal.insert(0, board[r][c])  # add to front
        r -= 1
        c += 1
    r, c = row + 1, col - 1
    while r < n and c >= 0:
        right_diagonal.append(board[r][c])
        r += 1
        c -= 1

    return right_diagonal


def get_left_diagonal(board, n, queen_position):
    row, col = queen_position
    left_diagonal = [board[row][col]]
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        left_diagonal.insert(0, board[r][c])  # add to front
        r -= 1
        c -= 1
    r, c = row + 1, col + 1
    while r < n and c < n:
        left_diagonal.append(board[r][c])
        r += 1
        c += 1
    return left_diagonal



def transform_positions(queen_positions, n) -> list:
    transformed = []
    for position in queen_positions:
        row, col = position
        transformed.append(col + 1 + n*row)
    return transformed

