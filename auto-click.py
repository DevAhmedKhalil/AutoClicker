import pyautogui 
import time

def auto_click():
    while True:
        # Get current mouse cursor position
        current_x, current_y = pyautogui.position()

        # Perform a left mouse button click at the current position
        pyautogui.click(current_x, current_y)

        # Wait for 30 seconds before clicking again
        time.sleep(30)

if __name__ == "__main__":
    try:
        print("Auto Clicker started. Press Ctrl-C to quit.")
        auto_click()
    except KeyboardInterrupt:
        print("\nAuto Clicker stopped.")
