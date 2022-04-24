import vlc
import os

p = vlc.MediaPlayer(f"{os.getcwd()}/mp3s/affiance_take_on_me.mp3")
p.play()



def stop():
    p.stop()

i = input("Press some keys")
stop()