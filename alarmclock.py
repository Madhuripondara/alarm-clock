import datetime
import time

def set_alarm():
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up!")
            break
        time.sleep(1)  # Wait for 1 second before checking the time again

set_alarm()
