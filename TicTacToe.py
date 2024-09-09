
ls = list( range(1, 10) )

def show_board():
    i = 0 
    while i <= 8:
        print(ls[i], "|", end=" ")
        if (i + 1) % 3 == 0:
            print()
        i = i + 1

def swap():
    # swap_num = ls.index(box_num)
    ls.pop(swap_num)
    ls.insert(swap_num, curr_sign)    

flag = 1

def check_winner():
    if player_row1 == [1,2,3] or player_row1 == [4,5,6] or player_row1 == [7,8,9] or player_row1 == [1, 4, 7] or player_row1 == [2,5,8] or player_row1 == [3,6,9] or player_row1 == [1,5,9] or player_row1 == [3,5,7]:
        print("Player 1 Wins....")
        return 2
    elif player_row2 == [1,2,3] or player_row2 == [4,5,6] or player_row2 == [7,8,9] or player_row2 == [1, 4, 7] or player_row2 == [2,5,8] or player_row2 == [3,6,9] or player_row2 == [1,5,9] or player_row2 == [3,5,7]:
        print("Player 2 Wins....")
        return 2
        


curr_player = 1
curr_sign = 'X'
player_row1 = []
player_row2 = []
move = 0

while move <= 9:
    show_board()
    if curr_player == 1:
        box_num1 = int(input("Player " + str(curr_player) + ", Enter box number: "))

        swap_num = ls.index(box_num1)
        player_row1.append(box_num1)
        flag = check_winner()
        if flag == 2:
            break
        swap()
        curr_player = 2
        curr_sign = 'O'
    else:
        box_num2 = int(input("Player " + str(curr_player) + ", Enter box number: "))

        swap_num = ls.index(box_num2)
        player_row2.append(box_num2)
        flag = check_winner()
        if flag == 2:
            break
        swap()
        curr_player = 1
        curr_sign = 'X'

    print()
    move = move + 1
