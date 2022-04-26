import os
from os import path, listdir
from typing import Union
# https://www.olivieraubert.net/vlc/python-ctypes/doc/
import vlc
from audio_player.audio_player.states.abstract_state import AbstractState
from audio_player.audio_player.states.ready_state import ReadyState
import threading
from time import sleep
import glob


class AudioPlayer:

    playing_thread = None

    def __init__(self):
        self.state: Union[AbstractState, None] = ReadyState(self)
        self.playing: bool = False
        self.filename_playing = ''
        self.audio = None
        self.pause = False
        self.files_dir = ''
        self.__set_files_dir()
        self.files = []
        self.__set_file_names()
        self.currently_playing = 0

    def __set_files_dir(self):
        base_path = path.dirname(__file__)
        self.files_dir = path.abspath(path.join(base_path, "..", "..", f"mp3s"))

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
        self.__start_playback()

    def handle_previous(self):
        if self.currently_playing - 1 < 0:
            self.currently_playing = len(self.files) - 1
        else:
            self.currently_playing -= 1
        self.__start_playback()

    def set_current_track_after_stop(self) -> str:
        return "Starting from first track"

    def handle_stop(self):
        self.audio.stop()
        self.currently_playing = 0

    def handle_pause(self):
        self.audio.pause()

    def handle_play(self):
        t = threading.Thread(target=self.__start_playback, daemon=True)
        t.start()

    def __start_playback(self):
        if self.audio is not None:
            self.audio.stop()
        self.audio = vlc.MediaPlayer(self.files[self.currently_playing])
        self.audio.play()
        while self.audio.is_playing() == 1:
            pass
            # if self.pause is True:
            #     self.audio.pause()
