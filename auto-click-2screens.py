import pyautogui  # type: ignore
import time
from datetime import datetime
import pytz  # type: ignore

def wait_for_click_position(order):
    input(f"\n[+] Move your mouse to the position for screen {order} and press Enter...")
    position = pyautogui.position()
    print(f"[✓] Position for screen {order} recorded at {position}")
    return position

def auto_click():
    cairo_tz = pytz.timezone("Africa/Cairo")

    # سجل موضعي الشاشتين بناءً على إدخال المستخدم
    pos1 = wait_for_click_position("1 (First Screen)")
    time.sleep(0.5)
    pos2 = wait_for_click_position("2 (Second Screen)")
    time.sleep(0.5)

    click_count = 0

    try:
        print("\n[▶] Auto Clicker started. Press Ctrl-C to quit.\n")
        while True:
            current_time = datetime.now(cairo_tz)
            minute = current_time.minute
            second = current_time.second

            if second == 0:
                if minute % 2 == 1:
                    pyautogui.click(pos1)
                    click_count += 1
                    print(f"✅ #{click_count:03} | Clicked on 🖥 Screen 1 at {pos1} | 🕒 {current_time.strftime('%H:%M:%S')}")
                else:
                    pyautogui.click(pos2)
                    click_count += 1
                    print(f"✅ #{click_count:03} | Clicked on 🖥 Screen 2 at {pos2} | 🕒 {current_time.strftime('%H:%M:%S')}")
                print("-" * 60)
                time.sleep(1.1)

            elif second == 30:
                if minute % 2 == 1:
                    pyautogui.click(pos1)
                    print(f"🕧       | (30s) Extra Click on Screen 1 at {pos1} | 🕒 {current_time.strftime('%H:%M:%S')}")
                else:
                    pyautogui.click(pos2)
                    print(f"🕧       | (30s) Extra Click on Screen 2 at {pos2} | 🕒 {current_time.strftime('%H:%M:%S')}")
                print("-" * 60)
                time.sleep(1.1)

            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n[⏹] Auto Clicker stopped. Total counted clicks: {click_count}")

if __name__ == "__main__":
    auto_click()
