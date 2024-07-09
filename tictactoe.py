import pyxel
from dataclasses import dataclass
from enum import Enum, auto
from random import choice

WIDTH = 240
HEIGHT = 240
TITLE = "TicTacToe"

class State(Enum):
    menu = auto()
    settings = auto()
    pvp = auto()
    pvc = auto()
    game_over = auto()

@dataclass
class Ai:
    def make_move(self, board):
        empty_cells = [(y, x) for y in range(3) for x in range(3) if board[y][x] is None]
        if empty_cells:
            return choice(empty_cells)
        return None

@dataclass
class Board:
    x: int = 5
    y: int = 5
    square: int = 14
    padding: int = 3
    color: int = pyxel.COLOR_NAVY
    hl_color: int = pyxel.COLOR_YELLOW

class Game:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title=TITLE)
        pyxel.mouse(True)
        self.reset_game()
        self.state = State.menu
        self.ai = Ai()
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None
        self.move_count = 0

    def update(self):
        match self.state:
            case State.menu:
                self.update_menu()
            case State.pvp:
                self.update_pvp()
            case State.pvc:
                self.update_pvc()
            case State.game_over:
                self.update_game_over()

    def update_menu(self):
        mx, my = pyxel.mouse_x, pyxel.mouse_y
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 20 < mx < 80 and 10 < my < 20:
                self.state = State.pvp
            elif 20 < mx < 80 and 25 < my < 35:
                self.state = State.pvc
            elif 20 < mx < 80 and 25 < my < 35:
                self.state = State.lobby
            elif 20 < mx < 80 and 40 < my < 50:
                self.state = State.settings
            elif 20 < mx < 80 and 55 < my < 65:
                pyxel.quit()


    def update_pvp(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            x = pyxel.mouse_x // 80
            y = pyxel.mouse_y // 80
            if x < 3 and y < 3 and self.board[y][x] is None and self.winner is None:
                self.board[y][x] = self.current_player
                self.move_count += 1
                if self.check_winner():
                    self.winner = self.current_player
                    self.state = State.game_over
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"
                if self.move_count == 9 and self.winner is None:
                    self.winner = "Draw"
                    self.state = State.game_over
        
    def update_pvc(self):
        if self.current_player == "X":
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                x = pyxel.mouse_x // 80
                y = pyxel.mouse_y // 80
                if x < 3 and y < 3 and self.board[y][x] is None and self.winner is None:
                    self.board[y][x] = self.current_player
                    self.move_count += 1
                    if self.check_winner():
                        self.winner = self.current_player
                        self.state = State.game_over
                    else:
                        self.current_player = "O"
                    if self.move_count == 9 and self.winner is None:
                        self.winner = "Draw"
                        self.state = State.game_over
        else:
            ai_move = self.ai.make_move(self.board)
            if ai_move:
                y, x = ai_move
                self.board[y][x] = self.current_player
                self.move_count += 1
                if self.check_winner():
                    self.winner = self.current_player
                    self.state = State.game_over
                else:
                    self.current_player = "X"
                if self.move_count == 9 and self.winner is None:
                    self.winner = "Draw"
                    self.state = State.game_over

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] is not None:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] is not None:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] is not None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] is not None:
            return True
        return False

    def draw(self):
        pyxel.cls(0)
        match self.state:
            case State.menu:
                self.draw_menu()
            case State.pvp:
                self.draw_pvp()
            case State.pvc:
                self.draw_pvp()
            case State.game_over:
                self.draw_game_over()

    def draw_menu(self):
        mx, my = pyxel.mouse_x, pyxel.mouse_y
        c = 20
        r = 10
        w = 80
        h = 10
        for i, opt in enumerate(["Player vs Player", "Player vs Computer","Settings", "Quit"]):
            hover = c < mx < c + w and r + i * 15 < my < r + i * 15 + h
            col = pyxel.COLOR_ORANGE if hover else pyxel.COLOR_BLACK
            pyxel.rect(c, r + i * 15, w, h, col)
            pyxel.text(c + 2, r + 2 + i * 15, opt, pyxel.COLOR_CYAN)

    def draw_pvp(self):
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == "X":
                    pyxel.text(x * 80 + 40, y * 80 + 40, "X", pyxel.COLOR_RED)
                elif self.board[y][x] == "O":
                    pyxel.text(x * 80 + 40, y * 80 + 40, "O", pyxel.COLOR_DARK_BLUE)
        for i in range(4):
            pyxel.line(i * 80, 0, i * 80, 240, pyxel.COLOR_WHITE)
            pyxel.line(0, i * 80, 240, i * 80, pyxel.COLOR_WHITE)
        if self.winner:
            pyxel.text(10, 225, f"Winner: {self.winner}", pyxel.COLOR_YELLOW)
        else:
            pyxel.text(10, 225, f"Player: {self.current_player}", pyxel.COLOR_YELLOW)
    
    def update_game_over(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.reset_game()
            self.state = State.menu

    def draw_game_over(self):
        pyxel.text(100, 110, "GAME OVER", pyxel.COLOR_YELLOW)
        pyxel.text(10, 130, f"Winner: {self.winner}", pyxel.COLOR_YELLOW)
        pyxel.text(10, 150, "Click to return to menu", pyxel.COLOR_YELLOW)

if __name__ == "__main__":
    Game()
