import pyautogui  # type: ignore
import time
from datetime import datetime
import pytz  # type: ignore


def auto_click(click_seconds):
    cairo_tz = pytz.timezone("Africa/Cairo")
    total_click_count = 0
    hourly_click_count = 0

    last_recorded_hour = datetime.now(cairo_tz).hour

    try:
        print("✅ Auto Clicker started. Press Ctrl-C to quit.")
        print(f"⏱️ Will click at seconds: {click_seconds}")

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

            # الكليك في الثواني اللي اختارها المستخدم
            if current_time.second in click_seconds:
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
    # ⬇️ يطلب من المستخدم إدخال الثواني
    user_input = input("⏱️ Enter seconds to click at (e.g. 0,30): ")

    # تحويل الإدخال لقائمة أرقام
    click_seconds = [int(s.strip()) for s in user_input.split(",")]

    auto_click(click_seconds)
