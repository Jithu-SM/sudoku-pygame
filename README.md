# Sudoku Game

A fun and interactive Sudoku game built using Python and Pygame! 🧩🔥

![Sudoku Fun](https://media.giphy.com/media/3orieUe6ejxSFxYCXe/giphy.gif)

## Features

- 🎲 **Random Sudoku Puzzle Generation** – Each game starts with a new, randomly generated puzzle.
- ⏳ **Timer** – Track your progress with a built-in timer displayed in `mm:ss` format.
- 🆘 **Help Button** – Stuck? Reveal a random correct cell from the solution. If the puzzle is unsolvable, the button will display "Not Solvable."
- 🏆 **Win Detection** – Solve the puzzle correctly to see a celebratory "You Win!" message.
- 🔍 **Solvability Check** – Ensures the puzzle is solvable before revealing a hint.
- ❌ **Highlight Unsolvable Cells** – Any cells causing an unsolvable puzzle will be marked in red.
- 🔢 **Bold Initial Cells** – The given numbers are bold and unchangeable to prevent accidental modifications.

## Directory Structure

```
sudoku-game/
├── main.py
├── board.py
├── sudoku_generator.py
├── assets/
│   ├── fonts/
│   └── images/
├── requirements.txt
└── README.md
```

## Requirements

Make sure you have the following installed:

- Python 3.x
- Pygame library

## Installation

To install Pygame, simply run:

```bash
pip install pygame
```

## Running the Game

Launch the game by running the following command in your terminal:

```bash
python main.py
```

## How to Play

1. **Start the Game** – Run `main.py` to generate a new Sudoku puzzle.
2. **Fill the Grid** – Click on a cell to increment the number (cycles from 1 to 9).
3. **Use Help** – Click the "Help" button to reveal a correct number if needed. If unsolvable, it will notify you.
4. **Win the Game** – Complete the puzzle correctly to see the winning message!

Enjoy the challenge of solving Sudoku! 🧠✨

![Winning Animation](https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif)

## Contributing

We welcome contributions! If you have ideas, suggestions, or bug fixes, feel free to contribute.

### Steps to Contribute:

1. **Fork the Repository** – Click the fork button on GitHub.
2. **Create a Branch** – Run:
   ```bash
   git checkout -b feature-branch
   ```
3. **Make Changes** – Modify the code as needed.
4. **Commit Your Changes** – Use descriptive commit messages:
   ```bash
   git commit -m "Add new feature"
   ```
5. **Push to Your Branch** – Upload your changes:
   ```bash
   git push origin feature-branch
   ```
6. **Open a Pull Request** – Submit your changes for review.

### Contribution Guidelines:

- Keep the code clean and follow best practices.
- Ensure changes do not break existing functionality.
- Add comments and documentation where necessary.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

Enjoy playing Sudoku! 🚀🎮

