import json

import customtkinter

from lib.Shipment import Shipment


class RegisterShipment(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        self.back_button = customtkinter.CTkButton(
            self, text="Volver", command=lambda: controller.show_frame(self._get_home())
        )
        self.back_button.grid(row=0, column=0, pady=10)

        self.title_label = customtkinter.CTkLabel(
            self, text="Introduzca los datos del envio", font=("Arial", 24)
        )
        self.title_label.grid(row=1, column=1, columnspan=2, pady=10)

        self.origin_label = customtkinter.CTkLabel(
            self, text="Origen:", font=("Arial", 18)
        )
        self.origin_label.grid(row=2, column=1, pady=10)

        self.origin_entry = customtkinter.CTkEntry(self, font=("Arial", 18))
        self.origin_entry.grid(row=2, column=2, pady=10)

        self.destination_label = customtkinter.CTkLabel(
            self, text="Destino:", font=("Arial", 18)
        )
        self.destination_label.grid(row=3, column=1, pady=10)

        self.destination_entry = customtkinter.CTkEntry(self, font=("Arial", 18))
        self.destination_entry.grid(row=3, column=2, pady=10)

        self.weight_label = customtkinter.CTkLabel(
            self, text="Peso:", font=("Arial", 18)
        )
        self.weight_label.grid(row=4, column=1, pady=10)

        self.weight_entry = customtkinter.CTkEntry(self, font=("Arial", 18))
        self.weight_entry.grid(row=4, column=2, pady=10)

        self.register_button = customtkinter.CTkButton(
            self,
            text="Registrar",
            command=self.register_shipment,
            font=("Arial", 18),
            height=40,
            width=150,
        )
        self.register_button.grid(row=5, column=1, columnspan=2, pady=10)

    def register_shipment(self):
        origin = self.origin_entry.get()
        destination = self.destination_entry.get()
        weight = float(self.weight_entry.get())
        current_state = "Pedido registrado"

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

        self.clean_entries()

        popup = customtkinter.CTkToplevel(self)
        popup.title("Envio registrado")
        popup.geometry("300x100")
        popup.resizable(False, False)

        label = customtkinter.CTkLabel(popup, text="Envio registrado con exito")
        label.pack(pady=10)

        ok_button = customtkinter.CTkButton(
            popup, text="Aceptar", command=popup.destroy
        )
        ok_button.pack(pady=10)

        popup.grab_set()
        self.wait_window(popup)

    def _get_home(self):
        from frames.Home import Home

        return Home

    def clean_entries(self):
        self.origin_entry.delete(0, "end")
        self.destination_entry.delete(0, "end")
        self.weight_entry.delete(0, "end")
