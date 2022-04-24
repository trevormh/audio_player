import tkinter as tk
from audio_player.ui.abstract_mediator import AbstractMediator
from audio_player.ui.components.abstract_component import AbstractComponent


class Label(AbstractComponent):

    def __init__(self, player_ui: AbstractMediator, name):
        super().__init__(player_ui, name)

    def set_label(self, value: str):
        return self.tk_widget.configure(text=value)

    def set_widget(self, **kwargs):
        self.tk_widget = tk.Label(**kwargs)
