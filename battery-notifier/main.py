from plyer import notification
import psutil
from time import sleep

while True:
    battery = psutil.sensors_battery()

    if battery is None:
        print("No battery information available.")
        break  # Exit the loop if no battery information is available

    life = battery.percent
    charging = battery.power_plugged  # True if the system is plugged in, False otherwise

    if life < 35 and not charging:
        notification.notify(
            title="Battery Low",
            message=f"Battery is at {life}%, Please connect the charger!",
            timeout=10
        )
    elif life > 99 and charging:
        notification.notify(
            title="Battery Full",
            message="Battery is fully charged!",
            timeout=10
        )
    sleep(60)  # Check every minute
