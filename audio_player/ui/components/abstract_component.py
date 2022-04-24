from abc import abstractmethod


class AbstractComponent:

    def __init__(self, player_ui, name, **kwargs):
        self.player_ui = player_ui
        self.name = name
        self.tk_widget = None

    @abstractmethod
    def set_widget(self, **kwargs):
        pass

    def keypress(self):
        self.player_ui.notify(self)