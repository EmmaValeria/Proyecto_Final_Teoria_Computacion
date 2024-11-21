import customtkinter


class ShipmentControl(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller
        self.shipment = None

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.back_button = customtkinter.CTkButton(
            self,
            text="Volver",
            command=lambda: controller.show_frame(self._get_shipments()),
        )
        self.back_button.grid(row=0, column=0)

        self.tracking_number_label = customtkinter.CTkLabel(
            self, text=self.shipment["tracking_number"]
        )
        self.tracking_number_label.grid(row=1, column=0)

        self.origin_label = customtkinter.CTkLabel(self, text=self.shipment["origin"])
        self.origin_label.grid(row=2, column=0)

        self.destination_label = customtkinter.CTkLabel(
            self, text=self.shipment["destination"]
        )
        self.destination_label.grid(row=2, column=1)

    def _get_shipments(self):
        from frames.Shipments import Shipments

        return Shipments

    def set_shipment(self, shipment):
        self.shipment = shipment
