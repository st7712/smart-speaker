import RPi.GPIO as GPIO
import subprocess
import time

# GPIO pins
BUTTON_MULTIFUNC = 17  # play/pause + skip
BUTTON_VOL_UP = 27
BUTTON_VOL_DOWN = 22
LED_PIN = 5  # One shared LED

DOUBLE_PRESS_TIME = 1.0  # Max time between presses for skip

def blink():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LED_PIN, GPIO.LOW)

def toggle_playback():
    print("Toggling playback")
    subprocess.run(["playerctl", "play-pause"])
    blink()

def skip_track():
    print("Skipping track")
    subprocess.run(["playerctl", "next"])
    blink()

def volume_up():
    print("Volume up")
    subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "+5%"])
    blink()

def volume_down():
    print("Volume down")
    subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "-5%"])
    blink()

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_MULTIFUNC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_VOL_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_VOL_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)

def loop():
    last_press_time = 0
    press_count = 0

    while True:
        # Check volume up
        if GPIO.input(BUTTON_VOL_UP) == GPIO.LOW:
            volume_up()
            time.sleep(0.3)

        # Check volume down
        if GPIO.input(BUTTON_VOL_DOWN) == GPIO.LOW:
            volume_down()
            time.sleep(0.3)

        # Check play/pause/skip button
        if GPIO.input(BUTTON_MULTIFUNC) == GPIO.LOW:
            now = time.time()
            if now - last_press_time < DOUBLE_PRESS_TIME:
                press_count += 1
            else:
                press_count = 1
            last_press_time = now

            # Wait for button release
            while GPIO.input(BUTTON_MULTIFUNC) == GPIO.LOW:
                time.sleep(0.05)

            if press_count == 2:
                skip_track()
                press_count = 0
            else:
                # Wait to see if a second press comes
                time.sleep(DOUBLE_PRESS_TIME)
                if press_count == 1:
                    toggle_playback()
                    press_count = 0

        time.sleep(0.05)

if __name__ == "__main__":
    try:
        setup_gpio()
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
