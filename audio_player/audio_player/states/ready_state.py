from audio_player.audio_player.states.abstract_state import AbstractState
from audio_player.audio_player.states.playing_state import PlayingState


class ReadyState(AbstractState):

    def __init__(self, player):
        super().__init__(player)

    def play(self):
        self.player.change_state(PlayingState(self.player))
        self.player.handle_play()

    def pause(self):
        from audio_player.audio_player.states.paused_state import PausedState
        self.player.change_state(PausedState(self.player))

    def stop(self):
        self.player.handle_stop()

    def next(self):
        pass

    def previous(self):
        pass
