import random

def main():
    while True:
        try:
            choice = int(input("0: exit, 1: randomize board, 2: piece picker\n"))
        except:
            print("Please enter an integer!")
            continue
        if choice == 0:
            exit()
        elif choice == 1:
            randomize_board()
        elif choice == 2:
            piece_picker()
        else:
            print("Invalid option!")

def randomize_board():

    used_squares = []
    remaining_white_pieces = ["pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "knight", "knight",
                              "bishop", "bishop", "king", "queen", "rook", "rook"]
    remaining_black_pieces = ["pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "knight", "knight",
                              "bishop", "bishop", "king", "queen", "rook", "rook"]
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    n = 0
    while n < 32:
        first = random.choice(letters)
        second = random.choice(numbers)
        move = first + str(second)
        if move in used_squares:
            continue
        used_squares.append(move)
        if n % 2 == 0:
            color = "white"
            piece = random.choice(remaining_white_pieces)
            remaining_white_pieces.remove(piece)
        else:
            color = "black"
            piece = random.choice(remaining_black_pieces)
            remaining_black_pieces.remove(piece)
        print(f'{color} {piece} to {move}')
        n += 1
    return

def piece_picker():
    print("Weighted by initial piece frequency.")
    while True:
        pieces = ["pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "knight", "knight",
                                  "bishop", "bishop", "king", "queen", "rook", "rook"]
        option = input("enter 'exit' to exit. enter anything else to generate a new piece.")
        if option == "exit":
            return
        else:
            print(random.choice(pieces))

main()