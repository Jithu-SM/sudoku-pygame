import pygame
from board import Board
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Sudoku")
    board = Board()
    start_time = time.time()

    button_font = pygame.font.Font(None, 36)
    help_button_text = button_font.render("Help", True, (255, 255, 255))
    help_button_rect = pygame.Rect(10, 550, 100, 40)
    not_solvable_text = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if help_button_rect.collidepoint(event.pos):
                    board.highlight_unsolvable_cells()
                    if board.is_solvable():
                        board.reveal_random_cell()
                        not_solvable_text = None
                    else:
                        not_solvable_text = button_font.render("Not Solvable", True, (255, 0, 0))
            board.handle_event(event)

        screen.fill((255, 255, 255))
        board.draw(screen)

        elapsed_time = int(time.time() - start_time)
        minutes, seconds = divmod(elapsed_time, 60)
        timer_text = f"Time: {minutes:02}:{seconds:02}"
        font = pygame.font.Font(None, 36)
        timer_surface = font.render(timer_text, True, (0, 0, 0))
        screen.blit(timer_surface, (450, 550))

        pygame.draw.rect(screen, (0, 0, 0), help_button_rect)
        screen.blit(help_button_text, (help_button_rect.x + 10, help_button_rect.y + 5))

        if not_solvable_text:
            screen.blit(not_solvable_text, (120, 550))

        if board.check_win():
            board.draw(screen)
            board.draw_win_animation(screen)
            pygame.display.flip()
            pygame.time.wait(5000)
            running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
