import json

import customtkinter

from states import STATES, Shipment


class RegisterShipment(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.grid_columnconfigure((0, 1), weight=1)

        self.back_button = customtkinter.CTkButton(
            self, text="Volver", command=lambda: controller.show_frame(self._get_home())
        )
        self.back_button.grid(row=0, column=0)

        self.origin_label = customtkinter.CTkLabel(self, text="Origen:")
        self.origin_label.grid(row=1, column=0)

        self.origin_entry = customtkinter.CTkEntry(self)
        self.origin_entry.grid(row=1, column=1)

        self.destination_label = customtkinter.CTkLabel(self, text="Destino:")
        self.destination_label.grid(row=2, column=0)

        self.destination_entry = customtkinter.CTkEntry(self)
        self.destination_entry.grid(row=2, column=1)

        self.weight_label = customtkinter.CTkLabel(self, text="Peso:")
        self.weight_label.grid(row=3, column=0)

        self.weight_entry = customtkinter.CTkEntry(self)
        self.weight_entry.grid(row=3, column=1)

        self.register_button = customtkinter.CTkButton(
            self, text="Registrar", command=self.register_shipment
        )
        self.register_button.grid(row=4, column=1)

    def register_shipment(self):
        origin = self.origin_entry.get()
        destination = self.destination_entry.get()
        weight = float(self.weight_entry.get())
        current_state = STATES[0]

        shipment = Shipment(origin, destination, weight, current_state)
        try:
            with open("shipments.json", "r") as file:
                shipments = json.load(file)
        except FileNotFoundError:
            shipments = []

        shipments.append(shipment.__dict__())

        with open("shipments.json", "w") as file:
            json.dump(shipments, file)

            file.close()

    def _get_home(self):
        from frames.Home import Home

        return Home
