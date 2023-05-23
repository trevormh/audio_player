from audio_player.audio_player.audio_player_controller import AudioPlayerController
from audio_player.ui.abstract_mediator import AbstractMediator
from audio_player.ui.components.abstract_component import AbstractComponent
from audio_player.ui.components.button import Button
import tkinter as tk

from audio_player.ui.components.label import Label


class PlayerUI(AbstractMediator):

    def __init__(self):
        self.player = AudioPlayerController()
        self.play_button = Button(self, "play")
        self.pause_button = Button(self, "pause")
        self.stop_button = Button(self, "stop")
        self.prev_button = Button(self, "previous")
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
        self.pause_button.set_widget(
            master=main_frame,
            text="Pause",
            command=self.pause_button.click
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
        self.pause_button.tk_widget.grid(row=0, column=1)
        self.stop_button.tk_widget.grid(row=0, column=2)
        self.prev_button.tk_widget.grid(row=0, column=3)
        self.next_button.tk_widget.grid(row=0, column=4)
        self.now_playing_label.tk_widget.grid(row=1, columnspan=5, sticky="w")

        main_frame.grid(row=0, column=0)
        window.mainloop()

    def notify(self, sender: AbstractComponent, name: str) -> None:
        if name == "play":
            self.player.play()
            self.now_playing_label.set_label(self.player.get_filename_playing())
        if name == "pause":
            self.player.pause()
            self.now_playing_label.set_label(f"Paused - {self.player.get_filename_playing()}")
        if name == "stop":
            self.player.stop()
            self.now_playing_label.set_label("")
        if name == "next":
            self.player.next()
            self.now_playing_label.set_label(f"{self.player.get_filename_playing()}")
        if name == "previous":
            self.player.previous()
            self.now_playing_label.set_label(f"{self.player.get_filename_playing()}")

