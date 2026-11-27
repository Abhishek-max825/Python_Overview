# This file looks for new folders inside user uploads and converts them to reel if they are not already converted
import os
import time
from text_to_audio import text_to_Speech

def text_to_audio_fun(folder):
    print("Text to audio : " , folder)
    desc_path = os.path.join(os.path.dirname(__file__), "user_upload", folder, "desc.text")
    with open(desc_path,"r+")as f:
       text = f.read()
       text_to_Speech(text,folder)
    print(text,folder)   

def create_reel(folder):
    print("Text to reel " ,folder)


if __name__ == "__main__":
  while True:  
    print("Processing queue...")
    with open(os.path.join(os.path.dirname(__file__),"done.txt"),"r")as f:
      done_folders = f.readlines()
      
    done_folders = [f.strip() for f in done_folders]
    folders = os.listdir(os.path.join(os.path.dirname(__file__),"user_upload"))
    
    for folder in folders:
      if folder not in done_folders:
        text_to_audio_fun(folder) # generate the audio from desc.txt
        create_reel(folder) # convert the images and audio.mp3 inside the folder to a reel

        with open(os.path.join(os.path.dirname(__file__),"done.txt"),"a") as f:
           f.write(folder + "\n")
    time.sleep(4)      