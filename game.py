
def show():
    print("    | 0 | 1 | 2 | ")
    print("___________________")
    for i in range(3):
        row_info = " | ".join(field[i])
        print(f"{i} | {row_info} | ")
        print("___________________")


def ask():
    while True:
        cords = input("       Your input: ").split()

        if len(cords) != 2:
            print(" You should input two coordinates! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Input integer numbers! ")

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Out of coordinate axes ")
            continue

        if field[x][y] != " ":
            print(" Cell is not empty! ")
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Won X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Won 0!!!")
            return True
    return False

field = [[" "] * 3 for i in range(3)]
num = 0
while True:
    num += 1

    show()

    if num % 2 == 1:
        print(" X's turn ")
    else:
        print(" 0's turn ")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if num == 9:
        print("Draw")
        break



