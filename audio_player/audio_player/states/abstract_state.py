from abc import abstractmethod

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from audio_player.audio_player.audio_player import AudioPlayer


class AbstractState:

    def __init__(self, player: 'AudioPlayer'):
        self.player = player
        self.component_name = ''

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def previous(self):
        pass
