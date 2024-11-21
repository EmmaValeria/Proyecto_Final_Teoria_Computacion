import customtkinter

from frames.Home import Home
from frames.RegisterShipment import RegisterShipment
from frames.ShipmentControl import ShipmentControl
from frames.Shipments import Shipments


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Custom Tkinter")
        self.geometry("900x700")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.container = customtkinter.CTkFrame(self)
        self.container.grid(column=0, row=0, sticky="nsew")

        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        self.frames = {}

        for F in (Home, RegisterShipment, Shipments):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        print(self.frames)
        self.show_frame(Home)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        if hasattr(frame, "refresh_data"):
            frame.refresh_data()
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()