from audio_player.audio_player.states.abstract_state import AbstractState


class PlayingState(AbstractState):

    def __init__(self, player):
        super().__init__(player)

    def play(self):
        pass

    def pause(self):
        self.player.handle_pause()
        from audio_player.audio_player.states.paused_state import PausedState
        self.player.change_state(PausedState(self.player))

    def stop(self):
        self.player.handle_stop()

    def next(self):
        self.player.handle_next()

    def previous(self):
        self.player.handle_previous()
