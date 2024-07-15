# Auto-Clicker

This is a simple auto-clicker script written in Python using the `pyautogui` module. The script automatically clicks the current mouse cursor position at the first second of each minute and at the 30th second of each minute.

## Features

- Automatically clicks the current mouse cursor position.
- Clicks at the first second of each minute and at the 30th second of each minute.
- Uses Cairo timezone (Africa/Cairo).
- Can be stopped with `Ctrl-C`.

## Requirements

- Python 3.x
- `pyautogui` library
- `pytz` library

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/DevAhmedKhalil/auto-click-pyautogui.git
    cd auto-click-pyautogui
    ```

2. **Create a virtual environment (optional but recommended):**
    ```sh
    # Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
    ```sh
    # Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install the required dependencies:**
    ```sh
    pip install pyautogui pytz
    ```

## Usage

1. **Run the script:**
    ```sh
    python auto_click.py
    ```

2. **The auto-clicker will start clicking the current mouse cursor position at the first second of each minute and at the 30th second of each minute.**

3. **To stop the auto-clicker, press `Ctrl-C` in the terminal.**

## Contributing

Feel free to open issues or submit pull requests if you have any improvements or bug fixes.
