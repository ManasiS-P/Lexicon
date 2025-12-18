import pyautogui
import time

# Give you 5 seconds to focus the VS Code window manually
print("You have 5 seconds to click on the VS Code window...")
time.sleep(5)

# Move to the top of the file
pyautogui.hotkey('ctrl', 'home')
time.sleep(1)

# Configuration
lines_to_move = 30    # Number of lines to scroll (you may adjust this)
pause_between_moves = 0.05  # Time between each line move

direction = 'down'

try:
    while True:
        for _ in range(lines_to_move):
            pyautogui.press('down' if direction == 'down' else 'up')
            time.sleep(pause_between_moves)

        # Switch direction
        direction = 'up' if direction == 'down' else 'down'
        print(f"Switching direction to: {direction}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped by user.")
