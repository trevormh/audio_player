from audio_player.ui.player_ui import PlayerUI


def demo():
    mediator = PlayerUI()
    mediator.build_gui()


if __name__ == "__main__":
    demo()
