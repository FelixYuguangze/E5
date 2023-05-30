import time
import winsound

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Time left: {seconds // 60} minute(s) {seconds % 60} second(s)")
        time.sleep(1)
        seconds -= 1

    # Play sound after the countdown ends
    frequency = 2500  # Set frequency to 2500 Hz
    duration = 1000  # Set duration to 1000 ms (1 second)
    winsound.Beep(frequency, duration)

if __name__ == "__main__":
    minutes = int(input("Enter number of minutes for focus timer: "))
    focus_timer(minutes)
