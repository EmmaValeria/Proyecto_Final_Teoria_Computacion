NT = "X"  # No Transition
INTERNATIONAL = "I"
REJECT_STATES = ["Cancelado", "Devuelto", "Problema Envio", "Problema Entrega"]
STATES = {
    "Pedido registrado": 0,
    "Pedido Procesado": 1,
    "En preparación": 2,
    "Enviado": 3,
    "En transito": 4,
    "En aduana": 5,
    "En reparto": 6,
    "Entregado": 7,
    "Intento fallido de entrega": 8,
    "Cancelado": 9,
    "Devuelto": 10,
    "Problema Envio": 11,
    "Problema Entrega": 12,
}

AUTOMATON = [
    [NT, True, NT, NT, NT, NT, NT, NT, NT, False, NT, NT, NT],
    [NT, NT, True, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT],
    [NT, NT, NT, True, NT, NT, NT, NT, NT, NT, NT, NT, NT],
    [NT, NT, NT, NT, True, NT, NT, NT, NT, NT, NT, False, NT],
    [NT, NT, NT, NT, NT, INTERNATIONAL, True, NT, NT, NT, NT, NT, False],
    [NT, NT, NT, NT, NT, NT, True, NT, NT, NT, NT, NT, NT],
    [NT, NT, NT, NT, NT, NT, NT, True, False, NT, NT, NT, NT],
    [NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT],
    [NT, NT, NT, NT, NT, NT, True, NT, NT, NT, False, NT, NT],
    [NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT],
    [NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT],
    [NT, NT, NT, True, NT, NT, NT, NT, NT, False, NT, NT, NT],
    [NT, NT, NT, NT, True, NT, NT, NT, NT, False, NT, NT, NT],
]


class Shipment:
    def __init__(self, origin: str, destination: str, weight: float, current_state):
        self._origin = origin
        self._destination = destination
        self._weight = weight
        self._current_state = current_state
        self._tracking_number = "0000001"

    def get_origin(self) -> str:
        return self._origin

    def get_destination(self) -> str:
        return self._destination

    def get_weight(self) -> float:
        return self._weight

    def get_current_state(self) -> str:
        return self._current_state

    def get_tracking_number(self) -> str:
        return self._tracking_number

    def set_current_state(self, state: str):
        self._current_state = state

    def __str__(self):
        return f"Origin: {self._origin}, Destination: {self._destination}, Weight: {self._weight}, Current State: {self._current_state}, Tracking Number: {self._tracking_number}"

    def __dict__(self):
        return {
            "origin": self._origin,
            "destination": self._destination,
            "weight": self._weight,
            "current_state": self._current_state,
            "tracking_number": self._tracking_number,
        }
