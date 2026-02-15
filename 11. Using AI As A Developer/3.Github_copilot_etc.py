'''
Github Copilot, Cursor AI & Llama coder

-> Get introduced to GitHub Copilot, Cursor AI, and Llama Coder—powerful AI tools that assist in coding.

1. GitHub Copilot: Suggests code in real-time as you type, based on context.
2. Cursor AI: An AI-first code editor that helps write, refactor, and understand code.
3. Llama Coder: A large language model optimized for coding tasks.

-> Use them to boost productivity, learn faster, and streamline development.
'''

# Write code for tic tac toe
# 1. Create a 3x3 board
# 2. Allow two players to take turns marking X and O
# 3. Check for a win or a draw after each move
# 4. Display the board after each move 
# 5. End the game when there's a winner or a draw
# 6. Optionally, allow players to play again after a game ends
# 7. Implement input validation to ensure players enter valid moves
# 8. Use functions to organize the code for better readability and maintainability
# 9. Optionally, add a simple AI opponent for single-player mode
# 10. Include comments in the code to explain the logic and flow of the game
# 11. Test the game thoroughly to ensure it works as expected and handles edge cases (e.g., invalid input, winning conditions, etc.) 

import random

def greet():
    """Greet the players and explain the rules."""
    print("Welcome to Tic Tac Toe!")
    print("Players take turns marking X and O on a 3x3 grid.")
    print("The first player to get three in a row wins!")
    print("If all spaces are filled without a winner, it's a draw.")
    print("Let's get started!")

# Initialize the 3x3 board
def create_board():
    """Create an empty 3x3 board."""
    return [' ' for _ in range(9)]

# Display the board to the players
def display_board(board):
    """Display the current state of the board."""
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")
    print("\n")

# Display position numbers for player reference
def display_positions():
    """Display the board position numbers for player reference."""
    print("Position numbers:")
    print(" 0 | 1 | 2 ")
    print("-----------")
    print(" 3 | 4 | 5 ")
    print("-----------")
    print(" 6 | 7 | 8 ")
    print("\n")

# Check if a move is valid
def is_valid_move(board, position):
    """Check if the move is valid (position is empty and within range)."""
    if position < 0 or position > 8:
        return False
    if board[position] != ' ':
        return False
    return True

# Get player input
def get_player_move(board, player):
    """Get a valid move from the player."""
    while True:
        try:
            position = int(input(f"Player {player}, enter your move (0-8): "))
            if is_valid_move(board, position):
                return position
            else:
                print("Invalid move! That position is already taken or out of range.")
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 8.")

# Get AI move (simple minimax algorithm)
def get_ai_move(board, ai_player, human_player):
    """Get AI move using minimax algorithm."""
    best_score = float('-inf')
    best_move = None
    
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai_player
            score = minimax(board, 0, False, ai_player, human_player)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    
    return best_move if best_move is not None else random.choice([i for i in range(9) if board[i] == ' '])

# Minimax algorithm for AI
def minimax(board, depth, is_maximizing, ai_player, human_player):
    """Minimax algorithm to evaluate board positions."""
    result = check_winner(board)
    
    if result == ai_player:
        return 10 - depth
    elif result == human_player:
        return depth - 10
    elif result == 'draw':
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai_player
                score = minimax(board, depth + 1, False, ai_player, human_player)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = human_player
                score = minimax(board, depth + 1, True, ai_player, human_player)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Check for a winner
def check_winner(board):
    """Check if there's a winner or if the board is full (draw)."""
    # Check rows
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] != ' ':
            return board[i*3]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    
    # Check for draw
    if ' ' not in board:
        return 'draw'
    
    return None

# Play a single game
def play_game(game_mode):
    """Play a single game of tic-tac-toe."""
    board = create_board()
    current_player = 'X'
    
    if game_mode == 1:
        # Two-player mode
        print("Starting Two-Player Mode!")
        display_positions()
        
        while True:
            display_board(board)
            move = get_player_move(board, current_player)
            board[move] = current_player
            
            result = check_winner(board)
            if result:
                display_board(board)
                if result == 'draw':
                    print("It's a Draw!")
                else:
                    print(f"Player {result} wins!")
                break
            
            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'
    
    else:
        # Single-player mode (against AI)
        human = 'X'
        ai = 'O'
        print("Starting Single-Player Mode! You are X, AI is O")
        display_positions()
        
        while True:
            display_board(board)
            move = get_player_move(board, human)
            board[move] = human
            
            result = check_winner(board)
            if result:
                display_board(board)
                if result == 'draw':
                    print("It's a Draw!")
                elif result == human:
                    print("Congratulations! You win!")
                else:
                    print("AI wins! Better luck next time.")
                break
            
            # AI move
            print("AI is thinking...")
            ai_move = get_ai_move(board, ai, human)
            board[ai_move] = ai
            
            result = check_winner(board)
            if result:
                display_board(board)
                if result == 'draw':
                    print("It's a Draw!")
                elif result == human:
                    print("Congratulations! You win!")
                else:
                    print("AI wins! Better luck next time.")
                break

# Main game loop
def main():
    """Main function to run the tic-tac-toe game."""
    print("=" * 40)
    print("Welcome to Tic Tac Toe!")
    print("=" * 40)
    
    while True:
        print("\nSelect game mode:")
        print("1. Two-Player Mode")
        print("2. Single-Player Mode (vs AI)")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            
            if choice == 1:
                play_game(1)
            elif choice == 2:
                play_game(2)
            elif choice == 3:
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Invalid choice! Please select 1, 2, or 3.")
                continue
            
            # Ask if players want to play again
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again not in ['yes', 'y']:
                print("Thanks for playing! Goodbye!")
                break
        
        except ValueError:
            print("Invalid input! Please enter a number.")

# Run the game
if __name__ == "__main__":
    main()