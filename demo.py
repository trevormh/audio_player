from audio_player.audio_player.audio_player import AudioPlayer
from time import sleep

# def demo():
#     player = AudioPlayer()
#     print(player.get_state())
#
#     player.start_playback()
#     # sleep(2)
#     input("test")
#     player.stop_playback()
#
#
# if __name__ == "__main__":
#     demo()

from audio_player.ui.player_ui import PlayerUI


def demo():
    mediator = PlayerUI()
    mediator.build_gui()


if __name__ == "__main__":
    demo()
