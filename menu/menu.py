import tkinter

from menu.video_input import VideoInput


class Menu:

    def __init__(self):
        self.root = tkinter.Tk()
        self.video_input = None

    def main(self):
        self.root.title("Auto Key")
        self.add_video_input()
        self.root.mainloop()

    def create_frame(self):
        frame = tkinter.Frame(self.root, width=100, height=100)
        frame.grid(padx=20, pady=10)
        return frame

    def add_video_input(self):
        frame = self.create_frame()
        self.video_input = VideoInput(frame)
        self.video_input.main()
