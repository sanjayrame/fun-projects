import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

# Define the board as a 2D list of strings
board = [    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"]
]

# Define the piece images
images = {
    "P": "white_pawn.png",
    "N": "white_knight.png",
    "B": "white_bishop.png",
    "R": "white_rook.png",
    "Q": "white_queen.png",
    "K": "white_king.png",
    "p": "black_pawn.png",
    "n": "black_knight.png",
    "b": "black_bishop.png",
    "r": "black_rook.png",
    "q": "black_queen.png",
    "k": "black_king.png"
}

# Create the main window
app = QApplication(sys.argv)
window = QMainWindow()
window.setGeometry(100, 100, 500, 500)
window.setWindowTitle("Chess")

# Add the chess board to the window
for i in range(8):
    for j in range(8):
        piece = board[i][j]
        label = QLabel(window)
        label.setGeometry(50 * j, 50 * i, 50, 50)
        label.setAlignment(Qt.AlignCenter)
        if (i + j) % 2 == 0:
            label.setStyleSheet("background-color: white")
        else:
            label.setStyleSheet("background-color: gray")
        if piece != " ":
            pixmap = QPixmap(images[piece])
            label.setPixmap(pixmap)

# Show the window
window.show()
sys.exit(app.exec_())