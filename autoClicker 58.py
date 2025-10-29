import pyautogui  # type: ignore
import time
from datetime import datetime
import pytz  # type: ignore


def auto_click():
    cairo_tz = pytz.timezone("Africa/Cairo")
    total_click_count = 0
    hourly_click_count = 0

    last_recorded_hour = datetime.now(cairo_tz).hour

    try:
        print("✅ Auto Clicker started. Press Ctrl-C to quit.")
        while True:
            current_time = datetime.now(cairo_tz)
            current_hour = current_time.hour

            if current_hour != last_recorded_hour:
                print(
                    f"🕒 Hour changed from {last_recorded_hour:02d}:00 to {current_hour:02d}:00. "
                    f"🧮 Clicks in the previous hour: {hourly_click_count}"
                )
                last_recorded_hour = current_hour
                hourly_click_count = 0

            if current_time.second == 58: # or current_time.second == 30:
                current_x, current_y = pyautogui.position()
                pyautogui.click(current_x, current_y)

                total_click_count += 1
                hourly_click_count += 1

                print(
                    f"🖱️ Clicked #{total_click_count} "
                    f"(This hour [{current_hour:02d}:00]: {hourly_click_count}) "
                    f"at ({current_x}, {current_y}) ⏰ {current_time.strftime('%H:%M:%S')}"
                )

                time.sleep(1.1)

            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n🛑 Auto Clicker stopped. Total clicks: {total_click_count} 🎯")


if __name__ == "__main__":
    auto_click()
