import time
import requests
import subprocess
from pathlib import Path
import tempfile
import os as os
import shutil as file
from tkinter.simpledialog import askinteger
fil = 1
testing = False

time_now = time.localtime()
time_hour = time_now.tm_hour
time_min = time_now.tm_min + 1
print(time_hour)

def set_wallpaper(p: Path):

    script = """
    desktops().forEach(d => {
        d.currentConfigGroup = Array("Wallpaper",
                                     "org.kde.image",
                                     "General");
        d.writeConfig("Image", "file://FILEPATH");
        d.reloadConfig();
    });
    """.replace("FILEPATH", str(p))

    cmd = [
        "qdbus6",
        "org.kde.plasmashell",
        "/PlasmaShell",
        "org.kde.PlasmaShell.evaluateScript",
        script,
    ]

    subprocess.check_call(cmd, stdout=subprocess.DEVNULL)


def swap_wallpaper(time_name):
    try:
        fil = fil * -1
    except:
        fil = 1
    print(f"Swapping wallpaper to {time_name}")
    file.copy(
        os.path.expanduser(f"~/wallpapers/mc cherry with bee/{time_name}.png"),
        os.path.expanduser(f"~/wallpapers/cur_wallpaper.png{fil}")
    )
    os.system(f"plasma-apply-wallpaperimage ~/wallpapers/cur_wallpaper{fil}.png")
    set_wallpaper(os.path.expanduser(f"~/wallpapers/cur_wallpaper{fil}.png"))

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
