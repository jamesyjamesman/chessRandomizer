import random
import os

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

# Generates a random piece, weighted by the initial piece frequency
def piece_picker():
    if_pawn = input("Would you like to change one pawn into a wildcard?")
    print("Weighted by initial piece frequency.")
    pieces = ["pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "knight", "knight",
                                  "bishop", "bishop", "king", "queen", "rook", "rook"]
    if if_pawn == "yes" or "y":
        pieces[0] = "any piece"
    while True:
        option = input("enter 'exit' to exit. enter anything else to generate a new piece.\n")
        if option == "exit":
            return
        else:
            print(random.choice(pieces))
main()