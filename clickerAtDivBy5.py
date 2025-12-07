import pyautogui  # type: ignore
import time
from datetime import datetime, timedelta
import pytz  # type: ignore
import winsound


# ───────────────────────────────────────────────
# Display a banner showing when the next click will happen
# ───────────────────────────────────────────────
def print_next_click_banner(next_click_time):
    print(r"""
      ╔════════ CLOCK ════════╗
      ║        🕒              ║
      ║   • Scheduled Click •  ║
      ╚════════════════════════╝
    """)
    print(f"🖱️ NEXT CLICK → {next_click_time.strftime('%H:%M:%S')}")
    print("-" * 35)


# ───────────────────────────────────────────────
# Main Auto Clicker Logic (loop every 0.1 sec)
# ───────────────────────────────────────────────
def auto_click():
    # Cairo timezone (for exact time syncing)
    cairo_tz = pytz.timezone("Africa/Cairo")

    # Second of each minute when click happens
    click_second = int(input("♦️ Enter the second to click (0-59): "))

    total_click_count = 0
    hourly_click_count = 0

    last_recorded_hour = datetime.now(cairo_tz).hour
    last_click_time = None

    # ───────────────────────────────────────────────
    # Calculate next click time:
    #   - Main click: 1 minute before any 5-minute mark (00, 05, 10, 15...)
    # ───────────────────────────────────────────────
    def schedule_next_click(now):
        minute = now.minute

        # Next minute divisible by 5
        divisible_minute = (minute + (5 - (minute % 5))) % 60

        # Click happens 1 minute earlier
        click_minute = (divisible_minute - 1) % 60

        hour = now.hour

        # Handle hour rollover cases
        if divisible_minute == 0 and minute > 55:
            hour = (hour + 1) % 24
        elif click_minute == 59 and minute < 55:
            hour = (hour + 1) % 24

        next_click = now.replace(hour=hour, minute=click_minute, second=click_second)

        # Ensure next click is always in the future
        if next_click <= now:
            next_click += timedelta(minutes=5)

        print_next_click_banner(next_click)
        return next_click

    # First scheduled click
    next_click_at = schedule_next_click(datetime.now(cairo_tz))

    try:
        print(f"Auto Clicker started. Clicking at second {click_second:02d}.")

        # ───────────────────────────────────────────────
        #  Main loop (checks time 10 times per second)
        # ───────────────────────────────────────────────
        while True:
            current_time = datetime.now(cairo_tz)
            current_hour = current_time.hour

            # Reset hourly counter when hour changes
            if current_hour != last_recorded_hour:
                print(
                    f"Hour changed {last_recorded_hour:02d}:00 → {current_hour:02d}:00 | "
                    f"Clicks last hour: {hourly_click_count}"
                )
                last_recorded_hour = current_hour
                hourly_click_count = 0

            # ───────────────────────────────────────────────
            # MAIN CLICK: 1 minute before a 5-minute mark
            # Example: minute = 04, 09, 14, 19...
            # ───────────────────────────────────────────────
            if (
                current_time.second == click_second
                and (current_time.minute + 1) % 5 == 0
            ):
                x, y = pyautogui.position()
                pyautogui.click(x, y)

                winsound.Beep(1000, 500)

                total_click_count += 1
                hourly_click_count += 1
                last_click_time = current_time

                print(
                    f"[Main] Click #{total_click_count} "
                    f"(Hour {current_hour:02d}:{hourly_click_count}) "
                    f"{current_time.strftime('%H:%M:%S')}"
                )

                # Schedule next click
                next_click_at = schedule_next_click(current_time)

                time.sleep(1.2)

            # ───────────────────────────────────────────────
            # EXTRA CLICK exactly 2.5 minutes after main click
            # (150 seconds)
            # ───────────────────────────────────────────────
            if last_click_time:
                if (current_time - last_click_time).seconds == 150:
                    x, y = pyautogui.position()
                    pyautogui.click(x, y)

                    total_click_count += 1
                    hourly_click_count += 1

                    print(
                        f"[Extra] Second Click #{total_click_count} "
                        f"(Hour {current_hour:02d}:{hourly_click_count}) "
                        f"{current_time.strftime('%H:%M:%S')} (2.5 min later)"
                    )

                    last_click_time = None
                    time.sleep(1.2)

            time.sleep(0.1)

    except KeyboardInterrupt:
        print(f"Stopped. Total clicks: {total_click_count}")


if __name__ == "__main__":
    auto_click()
