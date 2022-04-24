import os
import os.path
from typing import Union
import vlc
from audio_player.audio_player.states.abstract_state import AbstractState
from audio_player.audio_player.states.ready_state import ReadyState
import threading
from time import sleep


class AudioPlayer:

    playing_thread = None

    def __init__(self):
        self.state: Union[AbstractState, None] = ReadyState(self)
        self.playing: bool = False
        self.audio = None

    def change_state(self, state: AbstractState) -> None:
        self.state = state

    def get_state(self) -> AbstractState:
        return self.state

    def get_state_name(self) -> str:
        return type(self.state).__name__

    def is_playing(self) -> bool:
        return self.playing

    def next_track(self) -> str:
        return "Next track playing"

    def start_playback(self):
        self.state.play()

    def stop_playback(self):
        self.state.stop()

    def previous_track(self) -> str:
        return "Previous track"

    def set_current_track_after_stop(self) -> str:
        return "Starting from first track"

    def handle_stop(self):
        self.playing = False
        self.audio.stop()

    def play(self):
        base_path = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(base_path, "..", "..", "mp3s/affiance_take_on_me.mp3"))
        self.audio = vlc.MediaPlayer(filepath)
        self.audio.play()
        while self.playing:
            pass

    def handle_play(self):
        t = threading.Thread(target=self.play, daemon=True)
        t.start()


