# developed by strelnikov87

cell = ["[ ]" for i in range(1, 10)]
print('Welcome! This is a tic-tac-toe game. Please, enter a number \
from 1 to 9')
for i in range(0, 3):
    print(''.join(cell[i * 3:i * 3 + 3]))  # drawing grid


def draw_cell(pos:int, xo:str) -> bool:
    if cell[pos - 1] == "[ ]":  # check emptiness cell
        cell[pos - 1] = "[{}]".format(xo)
    else:
        return False  # not empty cell
    for k in range(0, 3):
        print(''.join(cell[k * 3:k * 3 + 3]))  # drawing grid
    return True


def whose_move(player_name:str, xo:str) -> bool:
    while True:
        try:
            number = int(input(f"{player_name}. Enter a number of cell: "))
            if number < 0 or number > 9:
                print('Please, enter a number between 0 and 9')
                continue
            if draw_cell(number, xo):
                break
            else:
                print("This cell is not empty. Choose another cell!")
                continue
        except ValueError:
            print("You entered symbols! Try again!")
    return check_end_game(xo)


def check_end_game(sign:str) -> bool:
    for k in range(0, 3):
        if f"[{sign}]" * 3 == ''.join(cell[k:7 + k:3]):
            return True
        if f"[{sign}]" * 3 == ''.join(cell[k * 3:k * 3 + 3]):
            return True
        if f"[{sign}]" * 3 == ''.join(cell[0::4]) or \
                f"[{sign}]" * 3 == ''.join(cell[2:8:2]):
            return True
    return False


def clean():
    for k, v in enumerate(cell):
        cell[k] = "[ ]"


def restart_game(player_name:str, status:str) -> str:
    print(f"{player_name} {status}!!!")
    return input("Do you wanna restart the game? Y/N").lower()


def check_odd() -> bool:
    if ("".join(cell).find("[ ]")) == -1:
        return True
    return False


while True:
    if whose_move("Player_1", "X"):
        if restart_game("Player_1", "Won") == "y":
            clean()
            continue
        break
    if check_odd():
        if restart_game("", "Odd!") == "y":
            clean()
            continue
        break
    if whose_move("Player_2", "O"):
        if restart_game("Player_2", "Won") == "y":
            clean()
            continue
        break
