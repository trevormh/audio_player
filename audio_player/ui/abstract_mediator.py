from abc import abstractmethod
from audio_player.ui.components.abstract_component import AbstractComponent


class AbstractMediator:

    @abstractmethod
    def notify(self, sender: AbstractComponent, name: str) -> None:
        pass
