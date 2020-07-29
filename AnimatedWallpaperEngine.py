# Windows
import glob
import ctypes
import os
# Image Manager
from PIL import Image, ImageDraw, ImageFont
# Other
import time

is_gif = True
frame_index = 0


class animated_wallpaper:
    def frames(self):
        home_folder_path = os.path.dirname(os.path.abspath("untitled\\"))
        wallpapers_folder_path = home_folder_path + "\\wallpapers\\"
        gif_paths = glob.glob(f"{wallpapers_folder_path}*.gif")
        for gif_path in gif_paths:
            frame_index = 0
            tries = 0
            gif_name = gif_path.replace(wallpapers_folder_path, "")
            gif_frames_folder_dir = f"{home_folder_path}\\wallpaper frames\\{gif_name}_frames\\"
            try:
                os.mkdir(gif_frames_folder_dir)
            except:
                print("Error: Dir already exists")
                os.remove(gif_path)
            while is_gif is True:
                try:
                    im = Image.open(gif_path)
                    im.seek(frame_index)
                    im.save(f"{gif_frames_folder_dir}\\{gif_name}frame{frame_index}.gif")
                    frame_index += 1
                except:
                    os.remove(gif_path)
                    pass
            tries += 1

    def animate(self):
        TimeBetweenFrames = 1/float((open("Fps.txt", "r").read())[:-3])
        gif_path = (glob.glob(f'{os.path.abspath("wallpaper frames")}\\*\\'))[0]
        gif_frames = (glob.glob(f'{gif_path}\\*.gif'))[0]
        frame_index = 0
        path, dirs, files = next(os.walk(gif_path))
        file_count = len(files)
        while True:
            while frame_index != file_count:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{gif_frames[:-5]}{frame_index}.gif", 0)
                time.sleep(TimeBetweenFrames)
                frame_index += 1
            else:
                frame_index = 0

    def run(self):
        self.frames()
        self.animate()

animated_wallpaper().run()
