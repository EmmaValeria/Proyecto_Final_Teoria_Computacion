import customtkinter

from frames.RegisterShipment import RegisterShipment
from frames.Shipments import Shipments


class Home(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.tracking_button = customtkinter.CTkButton(self, text="Rastrea tu envio")
        self.tracking_button.grid(row=0, column=0)

        self.register_button = customtkinter.CTkButton(
            self,
            text="Registrar envio",
            command=lambda: controller.show_frame(RegisterShipment),
        )
        self.register_button.grid(row=0, column=1)

        self.shipments_button = customtkinter.CTkButton(
            self, text="Envios", command=lambda: controller.show_frame(Shipments)
        )
        self.shipments_button.grid(row=1, column=0)
