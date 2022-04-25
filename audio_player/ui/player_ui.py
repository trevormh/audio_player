from audio_player.audio_player.audio_player import AudioPlayer
from audio_player.audio_player.audio_player_controller import AudioPlayerController
from audio_player.ui.abstract_mediator import AbstractMediator
from audio_player.ui.components.abstract_component import AbstractComponent
from audio_player.ui.components.button import Button
import tkinter as tk

from audio_player.ui.components.label import Label


class PlayerUI(AbstractMediator):

    def __init__(self):
        # self.player = AudioPlayer()
        self.player = AudioPlayerController()
        self.play_button = Button(self, "play")
        self.stop_button = Button(self, "stop")
        self.prev_button = Button(self, "prev")
        self.next_button = Button(self, "next")
        self.now_playing_label = Label(self, "playing_label")
        self.now_playing_text = ''

    def build_gui(self):
        window = tk.Tk()
        window.title("Audio Player")

        main_frame = tk.Frame(master=window, width=500)

        self.play_button.set_widget(
            master=main_frame,
            text="Play",
            command=self.play_button.click
        )
        self.stop_button.set_widget(
            master=main_frame,
            text="Stop",
            command=self.stop_button.click
        )
        self.prev_button.set_widget(
            master=main_frame,
            text="Prev",
            command=self.prev_button.click
        )
        self.next_button.set_widget(
            master=main_frame,
            text="Next",
            command=self.next_button.click
        )
        self.now_playing_label.set_widget(
            master=main_frame,
            text=self.player.get_filename_playing()
        )

        self.play_button.tk_widget.grid(row=0, column=0)
        self.stop_button.tk_widget.grid(row=0, column=1)
        self.prev_button.tk_widget.grid(row=0, column=2)
        self.next_button.tk_widget.grid(row=0, column=3)
        self.now_playing_label.tk_widget.grid(row=1, columnspan=4, sticky="w")

        main_frame.grid(row=0, column=0)
        window.mainloop()

    def notify(self, sender: AbstractComponent, name: str) -> None:
        if name == "play":
            self.player.play()
            self.now_playing_label.set_label(self.player.get_filename_playing())

        if name == "stop":
            self.player.stop()

