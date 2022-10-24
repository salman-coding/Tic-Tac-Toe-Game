def input_value():
    return int(input("Please enter value: "))
  
#----Check For Winnig Positions------#

def check_win(x_positions, z_positions):
    win_conditins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in win_conditins:
        x_win = int(x_positions[win[0]]) + int(x_positions[win[1]]) + int(x_positions[win[2]])
        z_win = int(z_positions[win[0]]) + int(z_positions[win[1]]) + int(z_positions[win[2]])
        if x_win == 3:
            print("X Wins")
            return 1
        elif z_win == 3:
            print("Z win")
            return 0
    return False

  #-------------------Game Board-----------------#
def gameboard(x_positiins, z_positions):
    zero = 'X' if x_positiins[0] else '0' if z_positions[0] else '0'
    one = 'X' if x_positiins[1] else '0' if z_positions[1] else '1'
    two = 'X' if x_positiins[2] else '0' if z_positions[2] else '2'
    three = 'X' if x_positiins[3] else '0' if z_positions[3] else '3'
    four = 'X' if x_positiins[4] else '0' if z_positions[4] else '4'
    five = 'X' if x_positiins[5] else '0' if z_positions[5] else '5'
    six = 'X' if x_positiins[6] else '0' if z_positions[6] else '6'
    seven = 'X' if x_positiins[7] else '0' if z_positions[7] else '7'
    eight = 'X' if x_positiins[8] else '0' if z_positions[8] else '8'
    print(f"| {zero} | {one} | {two} | ")
    print("-------------")
    print(f"| {three} | {four} | {five} | ")
    print("-------------")
    print(f"| {six} | {seven} | {eight} | ")


x_positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
z_positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1
game_on = True
print("Welcome to Tic Tac Toe Game")
while game_on:
    gameboard(x_positions, z_positions)
    if turn == 1:
        print(" X Turn")
        value = input_value()
        if x_positions[value] == 1 or z_positions[value] == 1:
            while True:
                print("value already exist. Please put another value")
                value = input_value()
                if x_positions[value] == 0 or z_positions[value] == 0:
                    x_positions[value] = 1
                    break
        else:
            x_positions[value] = 1
    else:
        print(" Z Turn")
        value = input_value()
        if x_positions[value] == 1 or z_positions[value] == 1:
            while True:
                print("value already exist. Please put another value")
                value = input_value()
                if x_positions[value] == 0 or z_positions[value] == 0:
                    z_positions[value] = 1
                    break
        else:
            z_positions[value] = 1
    is_win = check_win(x_positions, z_positions)
    if is_win == False:
        turn = 1 - turn
    else:
        print("Game is Over")
        game_on = False

