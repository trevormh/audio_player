from audio_player.audio_player.states.abstract_state import AbstractState


class PausedState(AbstractState):

    def __init__(self, player):
        super().__init__(player)

    def play(self):
        from audio_player.audio_player.states.playing_state import PlayingState
        self.player.change_state(PlayingState(self.player))
        self.player.handle_pause()

    def pause(self):
        pass

    def stop(self):
        self.player.handle_stop()

    def next(self):
        pass

    def previous(self):
        pass
