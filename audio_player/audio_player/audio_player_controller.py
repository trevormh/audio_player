from audio_player.audio_player.audio_player import AudioPlayer


# This class acts as a facade for the audioplayer
class AudioPlayerController:

    playing_thread = None

    def __init__(self):
        self.player = AudioPlayer()

    def play(self):
        self.player.get_state().play()

    def pause(self):
        self.player.get_state().pause()

    def stop(self):
        self.player.get_state().stop()

    def next(self):
        self.player.get_state().next()

    def previous(self):
        self.player.get_state().previous()

    def get_filename_playing(self):
        return self.player.get_filename_playing()
