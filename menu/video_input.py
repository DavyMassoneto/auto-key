import tkinter

import utils


class VideoInput:
    def __init__(self, root):
        self.root = root
        self.video_input = None
        self.select_video_button = None
        self.path = None

    def set_input_text(self, text):
        self.video_input.config(state="normal")
        self.video_input.delete(0, tkinter.END)
        self.video_input.insert(0, text)
        self.video_input.config(state="disabled")

    def create_video_input(self):
        self.video_input = tkinter.Entry(self.root, width=50, borderwidth=2)
        self.video_input.grid(row=0, column=0)
        self.set_input_text("Nenhum vídeo selecionado")
        self.video_input.bind("<Button-1>", lambda event: self.get_video_file_path())

    def create_select_video_button(self):
        self.select_video_button = utils.create_button(self.root, "Selecionar vídeo",
                                                       lambda: self.get_video_file_path(), 0, 1)

    def get_video_file_path(self):
        self.path = utils.require_video_file_window()
        if self.path:
            self.set_input_text(self.path)

    def main(self):
        self.create_video_input()
        self.create_select_video_button()
