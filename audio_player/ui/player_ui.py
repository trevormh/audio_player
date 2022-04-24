from audio_player.audio_player.audio_player import AudioPlayer
from audio_player.ui.abstract_mediator import AbstractMediator
from audio_player.ui.components.abstract_component import AbstractComponent
from audio_player.ui.components.button import Button
import tkinter as tk


class PlayerUI(AbstractMediator):

    def __init__(self):
        self.player = AudioPlayer()
        self.play_button = Button(self, "play")
        self.stop_button = Button(self, "stop")
        self.prev_button = Button(self, "prev")
        self.next_button = Button(self, "next")
        self.now_playing_label = Button(self, "playing_label")

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

        self.play_button.tk_widget.grid(row=0, column=0)
        self.stop_button.tk_widget.grid(row=0, column=1)
        self.prev_button.tk_widget.grid(row=0, column=2)
        self.next_button.tk_widget.grid(row=0, column=3)

        main_frame.grid(row=0, column=0)
        window.mainloop()

    def notify(self, sender: AbstractComponent, name: str) -> None:
        print(name)
        if name == "play":
            self.player.start_playback()

        if name == "stop":
            self.player.stop_playback()

