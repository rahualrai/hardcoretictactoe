# Tic Tac Toe Game with Arduino
This is a Tic Tac Toe game that uses an Arduino board to control the game pieces. The game is played on a 10x10 board, and the objective is to get a row, column, or diagonal of X's or O's before your opponent does.

## Requirements
To run this program, you will need:

- Python 3.x
- PySerial
- An Arduino board

## Installation
1. Connect the Arduino board to your computer via USB.
2. Install the PySerial package by running pip install pyserial in your terminal.
3. Download or clone the repository to your local machine.
4. Open the file 10X10.py in your preferred text editor.
5. Modify the makeblock variables in the draw_board function to match the name of the serial port that your Arduino board is connected to. This should be in the format "comX" on Windows.
6. Save your changes and run the program using python 10X10.py.

## How to Play
1. The game starts with an empty board.
2. Player 1 goes first and places an "X" on the board by inputting the x and y coordinates of the cell they want to play in.
3. Player 2 (the CPU) then places an "O" on the board by selecting an available cell.
4. Play continues until one player gets a row, column, or diagonal of three X's or O's, or until the board is full.
5. If a player wins, the game ends and their victory is announced. If the board is full without a winner, the game ends in a draw.

## Credits
This game was created by [rairahual7@gmail.com](rairahual7@gmail.com) as a programming exercise.
