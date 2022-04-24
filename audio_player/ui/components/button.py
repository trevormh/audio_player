import tkinter as tk
from audio_player.ui.abstract_mediator import AbstractMediator
from audio_player.ui.components.abstract_component import AbstractComponent


class Button(AbstractComponent):

    def __init__(self, player_ui: AbstractMediator, name: str):
        super().__init__(player_ui, name)

    def click(self):
        self.player_ui.notify(self, self.name)

    def set_widget(self, **kwargs):
        self.tk_widget = tk.Button(**kwargs)

    def update_widget(self, **kwargs):
        self.tk_widget.configure(**kwargs)
