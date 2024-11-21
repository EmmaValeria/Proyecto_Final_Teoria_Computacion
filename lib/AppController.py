from frames.Home import Home
from frames.RegisterShipment import RegisterShipment
from frames.ShipmentControl import ShipmentControl
from frames.Shipments import Shipments


class AppController:
    def __init__(self, container) -> None:
        self.shipment = None
        self.container = container
        self.frames = {}

        for F in (Home, RegisterShipment, Shipments, ShipmentControl):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def set_shipment(self, shipment):
        self.shipment = shipment

    def get_shipment(self):
        return self.shipment

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        if hasattr(frame, "refresh_data"):
            frame.refresh_data()
        frame.tkraise()
