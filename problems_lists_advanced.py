import random
lightbright = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
board = []
for x in range(10):
    board.append(lightbright.copy())


for row in board:
    for dot in row:
        print(dot, end=' ')
    print()
secret_y, secret_x = random.randint(0, 9), random.randint(0, 9)
print((secret_x, secret_y))
turns = 10
while turns > 0:
    answer = input('enter a row and column(example: 1 2)')
    y, x =map(int, answer.split())
    turns = turns - 1
    print(y)
    print(x)
    if x == secret_x and y == secret_y:
        print("You Won!")
        board[y][x] = 'X'
        turns = 0
    else:
        board[y][x] = 'O'
    for row in board:
        for dot in row:
            print(dot, end=' ')
        print()


