import subprocess
import time

import requests
import os
from moviepy.editor import VideoFileClip
import pygame

def download_video(url, destination):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(destination, 'wb') as f:
                f.write(response.content)
            return True
        else:
            print("Fehler beim Herunterladen des Videos. Statuscode:", response.status_code)
            return False
    except Exception as e:
        print("Fehler beim Herunterladen des Videos:", str(e))
        return False

def play_video(video_path):
    pygame.init()
    pygame.display.set_caption("Video")
    clock = pygame.time.Clock()

    clip = VideoFileClip(video_path)
    clip.preview()

    pygame.quit()

if __name__ == "__main__":
    video_url = "http://cdn.ghost143.de/jumpscare.mp4"  # URL zum Video
    video_filename = "jumpscare.mp4"

    if not os.path.exists(video_filename):
        print("Lade das Video herunter...")
        if download_video(video_url, video_filename):
            print("Video erfolgreich heruntergeladen.")
        else:
            print("Fehler beim Herunterladen des Videos. Beende das Skript.")
            exit()

    # Abspielen des Videos
    play_video(video_filename)
    time.sleep(300)
    play_video(video_filename)
    time.sleep(300)
    play_video(video_filename)
    time.sleep(300)
    play_video(video_filename)
    time.sleep(300)
    play_video(video_filename)
    time.sleep(300)
    play_video(video_filename)
    time.sleep(300)
    play_video(video_filename)
    time.sleep(300)
    play_video(video_filename)
    time.sleep(300)
    play_video(video_filename)
    time.sleep(300)
    play_video(video_filename)
