from tkinter import filedialog


def require_file_window(text="Selecione um arquivo", filetypes=(("Todos os arquivos", "*.*"),), initialdir="C:/"):
    return filedialog.askopenfilename(initialdir=initialdir, title=text, filetypes=filetypes)


def require_video_file_window(text="Selecione um vídeo", filetypes=(("Arquivos de vídeo", "*.mp4; *.avi; *.mov"),),
                              initialdir="C:/"):
    return require_file_window(text, filetypes, initialdir)
