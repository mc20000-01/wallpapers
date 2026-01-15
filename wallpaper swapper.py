import time
import os as os
import shutil as file
from tkinter.simpledialog import askinteger

testing = False

time_now = time.localtime()
time_hour = time_now.tm_hour
time_min = time_now.tm_min + 1
print(time_hour)

def swap_wallpaper(time_name):
    print(f"Swapping wallpaper to {time_name}")
    os.remove(os.path.expanduser("~/wallpapers/cur_wallpaper.png"))
    file.copy(
        os.path.expanduser(f"~/wallpapers/mc cherry with bee/{time_name}.png"),
        os.path.expanduser("~/wallpapers/cur_wallpaper.png")
    )

while True:
    time_now = time.localtime()
    if time_now.tm_min != time_min:
            if testing == True:
                time_hour = askinteger("Hour", "Enter hour (0-23): ")
            else:
                time_hour = int(time_now.tm_hour)
            time_min = time_now.tm_min
            print(time_hour)
            if time_hour >= 5 and time_hour < 12:
                swap_wallpaper("noon1")
            else:
                if time_hour >= 12 and time_hour < 18:
                    swap_wallpaper("day1")
                else:
                    if time_hour >= 18 and time_hour < 21:
                        swap_wallpaper("night1")
                    else:
                        swap_wallpaper("midnight1")