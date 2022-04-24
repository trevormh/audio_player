from audio_player.audio_player.states.abstract_state import AbstractState


class PlayingState(AbstractState):

    def __init__(self, player):
        super().__init__(player)

    def play(self):
        self.player.handle_play()

    def pause(self):
        pass

    def stop(self):
        self.player.handle_stop()

    def next(self):
        pass

    def previous(self):
        pass
