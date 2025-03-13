import pygame
import random
from sudoku_generator import generate_sudoku

class Board:
    def __init__(self):
        self.grid = generate_sudoku()
        self.solution = [row[:] for row in self.grid]
        self.initial_cells = [(r, c) for r in range(9) for c in range(9) if self.grid[r][c] != 0]
        self.unsolvable_cells = []
        self.solve_board(self.solution)

    def draw(self, screen):
        for row in range(9):
            for col in range(9):
                value = self.grid[row][col]
                if value != 0:
                    if (row, col) in self.initial_cells:
                        font = pygame.font.SysFont(None, 36, bold=True)
                    else:
                        font = pygame.font.SysFont(None, 36)
                    if (row, col) in self.unsolvable_cells:
                        text = font.render(str(value), True, (255, 0, 0))
                    else:
                        text = font.render(str(value), True, (0, 0, 0))
                    screen.blit(text, (col * 60 + 20, row * 60 + 20))

        for i in range(10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(screen, (0, 0, 0), (i * 60, 0), (i * 60, 540), thickness)
            pygame.draw.line(screen, (0, 0, 0), (0, i * 60), (540, i * 60), thickness)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // 60, x // 60
            if 0 <= row < 9 and 0 <= col < 9 and (row, col) not in self.initial_cells:
                self.grid[row][col] = (self.grid[row][col] + 1) % 10

    def check_win(self):
        for row in range(9):
            if len(set(self.grid[row])) != 9:
                return False
        for col in range(9):
            if len(set([self.grid[row][col] for row in range(9)])) != 9:
                return False
        return True

    def draw_win_animation(self, screen):
        font = pygame.font.Font(None, 72)
        text = font.render("You Win!", True, (0, 255, 0))
        screen.blit(text, (150, 250))

    def solve_board(self, board):
        def is_valid(board, row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True

        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.solve_board(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    def reveal_random_cell(self):
        empty_cells = [(r, c) for r in range(9) for c in range(9) if self.grid[r][c] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.grid[row][col] = self.solution[row][col]

    def is_solvable(self):
        temp_grid = [row[:] for row in self.grid]
        return self.solve_board(temp_grid)

    def highlight_unsolvable_cells(self):
        self.unsolvable_cells = []
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] != 0 and self.grid[row][col] != self.solution[row][col]:
                    self.unsolvable_cells.append((row, col))

    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True
