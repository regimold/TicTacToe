win_arr = [["X","X","X"],["X","X","X"],["X","X","X"]]

def play(count):
    game_arr = [["00","01","02"],["10","11","12"],["20","21","22"]]
    game_board(game_arr)
    player = (input("Choose your player (X or O): ")).upper()
    if player != "X" and player != "O":
        print("Invalid player choice. Please choose X or O.")
        return play(count)
    while True:
        make_move(player,game_arr)
        count += 1
        check_for_win(player,count,game_arr)
        if player == "X":
           player = "O"
        else:
            player = "X"

def game_board(game_arr):
    for i in game_arr:
        print(i)

def make_move(player,game_arr):
    choice = input("Enter a position on the board: ")
    if not check_valid_move(choice,game_arr):
        return make_move(player,game_arr)
    place_move(player, choice,game_arr)

def check_valid_move(choice,game_arr):
    pos1 = int(choice[0])
    pos2 = int(choice[1])
    if pos1 < 0 or pos1 > 2 or pos2 < 0 or pos2 > 2:
        print("Invalid move, try again.")
        return False
    if game_arr[pos1][pos2] == "X" or game_arr[pos1][pos2] == "O":
        print("Invalid move, try again.")
        return False
    else:
        return True

def place_move(player, choice,game_arr):
    pos1 = int(choice[0])
    pos2 = int(choice[1])
    print(pos1,pos2)
    game_arr[pos1][pos2] = player
    game_board(game_arr)

def check_for_win(player,count,game_arr):
    for row in range(3):
        for col in range(3):
            win_arr[row][col] = player

    for i in range(3):
        if game_arr[i] == win_arr[i]:
            winner(player,count)
    for j in range(3):
        if game_arr[0][j] == win_arr[0][j] and game_arr[1][j] == win_arr[1][j] and game_arr[2][j] == win_arr[2][j]:
            winner(player,count)
    if game_arr[0][0] == win_arr[0][0] and game_arr[1][1] == win_arr[1][1] and game_arr[2][2] == win_arr[2][2]:
        winner(player)
    if game_arr[0][2] == win_arr[0][2] and game_arr[1][1] == win_arr[1][1] and game_arr[2][0] == win_arr[2][0]:
        winner(player,count)
    if count == 9:
        winner(player,count)

def winner(player,count):
    if count == 9:
        print("It's a tie!")
    else:
        print(f"The winner is {player}!")
    new_game = input("Do you want to play again? (yes/no): ").lower()
    if new_game == "yes":
        count = 0
        play(count)
    else:
        exit()

count = 0
play(count)







