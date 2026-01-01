import time
import os as os
import shutil as file

time_now = time.localtime()
time_hour = time_now.tm_hour
time_min = time_now.tm_min + 1
print(time_hour)

def swap_wallpaper(time_name):
    os.remove(os.path.expanduser("~/wallpapers/cur_wallpaper.png"))
    file.copy(
        os.path.expanduser(f"~/wallpapers/mc cherry with bee/{time_name}.png"),
        os.path.expanduser("~/wallpapers/cur_wallpaper.png")
    )

while True:
    time_now = time.localtime()
    if time_now.tm_min != time_min:
            time_hour = int(time_now.tm_hour)
            time_min = time_now.tm_min
            print(time_hour)
            if time_hour >= 5 and time_hour < 12:
                swap_wallpaper("noon")
            else:
                if time_hour >= 12 and time_hour < 18:
                    swap_wallpaper("day")
                else:
                    if time_hour >= 18 and time_hour < 21:
                        swap_wallpaper("night")
                    else:
                        swap_wallpaper("midnight")
        