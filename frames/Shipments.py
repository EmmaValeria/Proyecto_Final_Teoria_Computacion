import json

import customtkinter


class Shipments(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        try:
            with open("shipments.json", "r") as file:
                self.shipments = json.load(file)
                file.close()
        except FileNotFoundError:
            self.shipments = []

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

        self.headers = [
            "Origen",
            "Destino",
            "Peso",
            "Estado",
            "Numero de seguimiento",
            "Acciones",
        ]
        self.back_button = customtkinter.CTkButton(
            self, text="Volver", command=lambda: controller.show_frame(self._get_home())
        )
        self.back_button.grid(row=0, column=0)

        for i, header in enumerate(self.headers):
            label = customtkinter.CTkLabel(
                self,
                text=header,
                fg_color="#1abc9c",
                text_color="white",
                width=150,
                height=40,
            )
            label.grid(row=1, column=i, padx=5, pady=5)

        self.data_frame = customtkinter.CTkFrame(self)
        self.data_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.data_frame.grid(row=2, column=0, columnspan=6, sticky="nsew")
        self.populate_table()

    def populate_table(self):
        for row, shipment in enumerate(self.shipments, start=2):
            origin = customtkinter.CTkLabel(
                self.data_frame,
                text=shipment["origin"],
                width=150,
                height=40,
            )
            origin.grid(row=row, column=0, pady=5)

            destination = customtkinter.CTkLabel(
                self.data_frame,
                text=shipment["destination"],
                width=150,
                height=40,
            )
            destination.grid(row=row, column=1, pady=5)

            weight = customtkinter.CTkLabel(
                self.data_frame,
                text=shipment["weight"],
                width=150,
                height=40,
            )
            weight.grid(row=row, column=2, pady=5)

            current_state = customtkinter.CTkLabel(
                self.data_frame,
                text=shipment["current_state"],
                width=150,
                height=40,
            )
            current_state.grid(row=row, column=3, pady=5)

            tracking_number = customtkinter.CTkLabel(
                self.data_frame,
                text=shipment["tracking_number"],
                width=150,
                height=40,
            )
            tracking_number.grid(row=row, column=4, pady=5)

            actions = customtkinter.CTkButton(
                self.data_frame,
                text="Acciones",
                width=150,
                height=40,
                command=lambda: self.show_actions(shipment),
            )
            actions.grid(row=row, column=5, pady=5)

    def _get_home(self):
        from frames.Home import Home

        return Home

    def _get_shipment_control(self):
        from frames.ShipmentControl import ShipmentControl

        return ShipmentControl

    def refresh_data(self):
        for widget in self.data_frame.winfo_children():
            widget.destroy()

        try:
            with open("shipments.json", "r") as file:
                self.shipments = json.load(file)
                file.close()
        except FileNotFoundError:
            self.shipments = []

        self.populate_table()

    def show_actions(self, shipment):
        self.controller.set_shipment(shipment)

        self.controller.frames[self._get_shipment_control()].display_data()

        self.controller.show_frame(self._get_shipment_control())
