import chess
from os import system
from time import sleep


board = chess.Board()
while not board.is_checkmate() or not board.is_stalemate():
    system('clear')
    print(board)
    move = input("\nмоля въведете вашия ход: ")
    try:
        board.push_san(move)
    except:
        print(" Г Р Е Ш К А !!!")
        sleep(1)

print("\n К Р А Й  Н А  И Г Р А Т А  !!! ")