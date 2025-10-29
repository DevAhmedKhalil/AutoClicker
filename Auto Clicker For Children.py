import pyautogui  # type: ignore
import time
from datetime import datetime
import pytz  # type: ignore
import winsound  # لإصدار صوت في ويندوز


def auto_click():
    cairo_tz = pytz.timezone("Africa/Cairo")
    total_click_count = 0
    hourly_click_count = 0

    last_recorded_hour = datetime.now(cairo_tz).hour
    last_click_time = None  # حفظ وقت الكليك الأساسي

    try:
        print("✅ Auto Clicker started. Press Ctrl-C to quit.")
        while True:
            current_time = datetime.now(cairo_tz)
            current_hour = current_time.hour

            # عند تغير الساعة
            if current_hour != last_recorded_hour:
                print(
                    f"🕒 Hour changed from {last_recorded_hour:02d}:00 to {current_hour:02d}:00. "
                    f"🧮 Clicks in the previous hour: {hourly_click_count}"
                )
                last_recorded_hour = current_hour
                hourly_click_count = 0

            # 🔵 الكليك الأساسي (مع الصوت) - بداية الدقيقة
            if current_time.second == 00 and current_time.minute % 5 == 0:
                current_x, current_y = pyautogui.position()
                pyautogui.click(current_x, current_y)

                # صوت تنبيه
                winsound.Beep(1000, 500)

                total_click_count += 1
                hourly_click_count += 1

                # سجل وقت الكليك الأساسي
                last_click_time = current_time

                print(
                    f"🖱️ [Main] Clicked #{total_click_count} "
                    f"(Hour {current_hour:02d}: {hourly_click_count}) "
                    f"⏰ {current_time.strftime('%H:%M:%S')}"
                )

                time.sleep(1.2)

            # 🟡 الكليك الثاني بعد دقيقتين ونصف (بدون صوت)
            if last_click_time:
                elapsed = (current_time - last_click_time).seconds
                if elapsed == 150:  # 150 ثانية = 2.5 دقيقة
                    current_x, current_y = pyautogui.position()
                    pyautogui.click(current_x, current_y)

                    total_click_count += 1
                    hourly_click_count += 1

                    print(
                        f"🖱️ [Extra] Second Click #{total_click_count} "
                        f"(Hour {current_hour:02d}: {hourly_click_count}) "
                        f"⏰ {current_time.strftime('%H:%M:%S')} (2.5 min later)"
                    )

                    last_click_time = None  # منع التكرار
                    time.sleep(1.2)

            time.sleep(0.1)

    except KeyboardInterrupt:
        print(f"\n🛑 Auto Clicker stopped. Total clicks: {total_click_count} 🎯")


if __name__ == "__main__":
    auto_click()
