import customtkinter
from PIL import Image

from frames.RegisterShipment import RegisterShipment
from frames.Shipments import Shipments
from frames.TrackShipment import TrackShipment


class Home(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.side_bar = customtkinter.CTkFrame(self, fg_color="#333333")
        self.side_bar.grid(row=0, column=0, sticky="nsew")

        self.main_container = customtkinter.CTkFrame(self)
        self.main_container.grid(
            row=0, column=1, columnspan=9, sticky="nsew", rowspan=10
        )
        self.main_container.grid_columnconfigure(0, weight=1)
        self.main_container.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        self.tracking_button = customtkinter.CTkButton(
            self.side_bar,
            text="Rastrea tu envio",
            command=lambda: controller.show_frame(TrackShipment),
            fg_color="transparent",
        )
        self.tracking_button.pack(pady="20", fill="x")

        self.register_button = customtkinter.CTkButton(
            self.side_bar,
            text="Registrar envio",
            command=lambda: controller.show_frame(RegisterShipment),
            fg_color="transparent",
        )
        self.register_button.pack(pady="20", fill="x")

        self.shipments_button = customtkinter.CTkButton(
            self.side_bar,
            text="Envios",
            command=lambda: controller.show_frame(Shipments),
            fg_color="transparent",
        )
        self.shipments_button.pack(pady="20", fill="x")

        self.company_name = customtkinter.CTkLabel(
            self.main_container,
            text="Paqueteria Express",
            font=("Arial", 24),
            text_color="white",
            anchor="w",
        )
        self.company_name.grid(
            column=0,
            row=0,
            pady="20",
            padx="20",
        )

        self.bg_image = customtkinter.CTkImage(
            light_image=Image.open("assets/img/bg_image.png"),
            dark_image=Image.open("assets/img/bg_image.png"),
            size=(300, 300),
        )
        self.about_us = customtkinter.CTkLabel(
            self.main_container,
            text="Somos una empresa de paqueteria con mas de 10 años de experiencia en el mercado",
            font=("Arial", 20),
            wraplength=500,
            text_color="white",
        )
        self.about_us.grid(column=0, row=3, pady="20", padx="20")

        self.bg_label = customtkinter.CTkLabel(
            self.main_container, image=self.bg_image, text=""
        )
        self.bg_label.grid(column=0, row=7, pady="20", padx="20")
