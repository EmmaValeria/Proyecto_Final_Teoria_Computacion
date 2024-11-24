import customtkinter

from frames.Home import Home
from lib.AppController import AppController


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de paqueteria")
        self.geometry("900x700")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.container = customtkinter.CTkFrame(self)
        self.container.grid(column=0, row=0, sticky="nsew")

        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        self.controller = AppController(self.container)
        self.controller.show_frame(Home)


if __name__ == "__main__":
    app = App()
    app.mainloop()
