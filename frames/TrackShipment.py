import json

import customtkinter


class TrackShipment(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller
        self.shipment = None

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        self.back_button = customtkinter.CTkButton(
            self,
            text="Volver",
            command=lambda: controller.show_frame(self._get_home()),
        )
        self.back_button.grid(row=0, column=0, pady=10, sticky="w")

        self.tracking_number_label = customtkinter.CTkLabel(
            self, text="Número de seguimiento:", font=("Arial", 18)
        )
        self.tracking_number_label.grid(row=1, column=0, pady=10, columnspan=4)

        self.tracking_number_entry = customtkinter.CTkEntry(self, font=("Arial", 18))
        self.tracking_number_entry.grid(row=1, column=2, pady=10, columnspan=4)

        self.get_shipment_button = customtkinter.CTkButton(
            self,
            text="Buscar",
            command=self.get_shipment,
            font=("Arial", 18),
            height=40,
            width=150,
        )
        self.get_shipment_button.grid(row=2, column=0, columnspan=8, pady=10)

        self.shipment_data_container = customtkinter.CTkFrame(self)
        self.shipment_data_container.grid(row=3, column=0, columnspan=8, sticky="nsew")
        self.shipment_data_container.grid_columnconfigure((0, 1), weight=1)

        self.timeline_container = customtkinter.CTkFrame(self)
        self.timeline_container.grid(row=4, column=0, columnspan=8, sticky="nsew")

    def _get_home(self):
        from frames.Home import Home

        return Home

    def get_shipment(self):
        tracking_number = self.tracking_number_entry.get()

        try:
            with open("shipments.json", "r") as f:
                shipments = json.load(f)
                f.close()
        except FileNotFoundError:
            shipments = []

        for s in shipments:
            if s["tracking_number"] == tracking_number:
                self.shipment = s
                self.display_data()
                break

    def display_timeline(self):
        history_length = len(self.shipment["history"])
        for i in range(history_length * 2):
            self.timeline_container.grid_columnconfigure(i, weight=1)

        for i, state in enumerate(self.shipment["history"]):
            state_label = customtkinter.CTkLabel(self.timeline_container, text=state)
            state_label.grid(row=0, column=i * 2, padx=10, pady=5, sticky="n")

            if i < len(self.shipment["history"]) - 1:
                arrow_label = customtkinter.CTkLabel(self.timeline_container, text="→")
                arrow_label.grid(row=0, column=i * 2 + 1, sticky="n")

    def display_data(self):
        for widget in self.shipment_data_container.winfo_children():
            widget.destroy()

        for widget in self.timeline_container.winfo_children():
            widget.destroy()

        self.origin_label = customtkinter.CTkLabel(
            self.shipment_data_container,
            text=f"Origen: {self.shipment['origin']}",
            font=("Arial", 18),
        )
        self.origin_label.grid(row=3, column=0, columnspan=2)

        self.destination_label = customtkinter.CTkLabel(
            self.shipment_data_container,
            text=f"Destino: {self.shipment['destination']}",
            font=("Arial", 18),
        )
        self.destination_label.grid(row=4, column=0, columnspan=2)

        self.weight_label = customtkinter.CTkLabel(
            self.shipment_data_container,
            text=f"Peso: {self.shipment['weight']} kg",
            font=("Arial", 16),
        )
        self.weight_label.grid(row=5, column=0, columnspan=2)

        self.display_timeline()
