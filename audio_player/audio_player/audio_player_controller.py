from audio_player.audio_player.audio_player import AudioPlayer


# This class acts as a facade for the audioplayer
class AudioPlayerController:

    playing_thread = None

    def __init__(self):
        self.player = AudioPlayer()
        self.state = self.player.get_state()

    def play(self):
        self.state.play()

    def stop(self):
        self.state.stop()

    def get_filename_playing(self):
        return self.player.get_filename_playing()
