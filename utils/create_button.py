import tkinter


def create_button(root, text, command, row, column, padx=5, pady=5):
    button = tkinter.Button(root, text=text, command=command)
    button.grid(row=row, column=column, padx=padx, pady=pady)
    return button
