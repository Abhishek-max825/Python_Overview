import time
from plyer import notification

print("hello")
while True:
    notification.notify(title="Reminder",message="nigga drink your water ",timeout=10)
    time.sleep(10)


# What Actually Happens if you wont use time module 

# • Non-blocking execution: The timeout=10 parameter only tells your operating system how long the pop-up should stay visible on your screen. It does not pause your Python script.
# • Instant looping: Because notification.notify() finishes running in a fraction of a millisecond, the while True loop immediately repeats.
# • System overload: Within a few seconds, Python will queue thousands of identical alerts. Your Action Center (Windows), Notification Center (macOS), or desktop environment (Linux) will either lag severely, become unresponsive, or start dropping notifications.
# • High CPU usage: The tight loop will spike your CPU usage on a single core to 100% until you force-stop the script.

# from plyer import notification

# notification.notify(
#     title="Task Complete",
#     message="Your Python script has finished running.",
#     app_name="My Python App",
#     timeout=10  # Duration in seconds
# )

