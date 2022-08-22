'''
Script to check if the Wi-Fi is current running.
'''

# check the current status of the internet
# check if the internet is on or not
# if it was on but now off, sent one message that it's off and keep checking
# if it was off but now on, send one message and continue checking


# imports
from urllib.request import urlopen
from time import sleep
from datetime import datetime

wifi_on = True
logged = False


def check_status():
    try:
        response = urlopen('http://www.example.com/', timeout=10)
        return True
    except Exception:
        return False


def internet_check(status):
    global wifi_on, logged
    with open("down.txt", "a") as f:
        if status and (wifi_on is False):
            wifi_on = True
            logged = False
            f.write(f"BACK AT: {datetime.now().strftime('%b %d %Y %-I:%M %p')}\n")
        elif status is False and logged is False:
            wifi_on = False
            logged = True
            f.write(f"FAILED AT: {datetime.now().strftime('%b %d %Y %-I:%M %p')}\n")


def main():
    while True:

        # to avoid getting 439 errors
        sleep(10)

        status_val = check_status()

        internet_check(status_val)


if __name__ == "__main__":
    main()
