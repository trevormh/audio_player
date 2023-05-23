from os import path
from typing import Union
import vlc
from audio_player.audio_player.states.abstract_state import AbstractState
from audio_player.audio_player.states.ready_state import ReadyState
import threading
import glob


class AudioPlayer:

    def __init__(self):
        self.state: Union[AbstractState, None] = ReadyState(self)
        self.playing: bool = False
        self.filename_playing = ''
        self.vlc_media = None
        self.pause = False
        self.files_dir = ''
        self.__set_files_dir()
        self.files = []
        self.__set_file_names()
        self.currently_playing = 0

    def __set_files_dir(self):
        base_path = path.dirname(__file__)
        self.files_dir = path.abspath(path.join(base_path, "..", "..", f"mp3"))

    def __set_file_names(self):
        self.files = []
        for file in glob.glob(self.files_dir + "/*.mp3"):
            self.files.append(file)

    def get_filename_playing(self):
        file_path = self.files[self.currently_playing]
        file = file_path.rpartition("/")
        return file[2]

    def change_state(self, state: AbstractState) -> None:
        self.state = state

    def get_state(self) -> AbstractState:
        return self.state

    def get_state_name(self) -> str:
        return type(self.state).__name__

    def is_playing(self) -> bool:
        return self.playing

    def handle_next(self):
        if self.currently_playing + 1 > len(self.files) - 1:
            self.currently_playing = 0
        else:
            self.currently_playing += 1
        self.handle_play()

    def handle_previous(self):
        if self.currently_playing - 1 < 0:
            self.currently_playing = len(self.files) - 1
        else:
            self.currently_playing -= 1
        self.handle_play()

    def set_current_track_after_stop(self) -> str:
        return "Starting from first track"

    def handle_stop(self):
        self.vlc_media.stop()
        self.currently_playing = 0

    def handle_pause(self):
        self.vlc_media.pause()

    def handle_play(self):
        t = threading.Thread(target=self.__start_playback, daemon=True)
        t.start()

    def __start_playback(self):
        if self.vlc_media is not None:
            self.vlc_media.stop()
        self.vlc_media = vlc.MediaPlayer(self.files[self.currently_playing])
        self.vlc_media.play()
        while self.vlc_media.is_playing() == 1:
            pass
