import pyautogui # type: ignore
import time
from datetime import datetime
import pytz # type: ignore


def auto_click():
    cairo_tz = pytz.timezone("Africa/Cairo")
    try:
        print("Auto Clicker started. Press Ctrl-C to quit.")
        while True:
            # Get the current time in Cairo timezone
            current_time = datetime.now(cairo_tz)

            # Check if it's the first second of the minute or the 30th second
            if current_time.second == 0 or current_time.second == 30:
                # Get the current mouse cursor position
                current_x, current_y = pyautogui.position()
                # current_x, current_y = 849, 519


                # Perform a left mouse button click at the current position
                pyautogui.click(current_x, current_y)
                print(
                    f"Clicked at ({current_x}, {current_y}) at {current_time.strftime('%H:%M:%S')}"
                )

                # Wait for a bit to avoid multiple clicks within the same second
                time.sleep(1.1)  # Sleep for slightly more than 1 second

            # Sleep for a short period to avoid excessive CPU usage
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nAuto Clicker stopped.")


if __name__ == "__main__":
    auto_click()
