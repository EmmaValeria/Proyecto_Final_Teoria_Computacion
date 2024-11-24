NT = "X"  # No Transition
INTERNATIONAL = "I"
REJECT_STATES = [
    "Cancelado",
    "Devuelto",
    "Problema Envio",
    "Problema Entrega",
    "Problema Aduanas",
    "Intento fallido de entrega",
]
STATES = {
    "Pedido registrado": 0,
    "Pedido Procesado": 1,
    "En preparacion": 2,
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
    "Problema Aduanas": 13,
}

AUTOMATON = [
    [NT, True, NT, NT, NT, NT, NT, NT, NT, False, NT, NT, NT, NT],
    [NT, NT, True, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT],
    [NT, NT, NT, True, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT],
    [NT, NT, NT, NT, True, NT, NT, NT, NT, NT, NT, False, NT, NT],
    [NT, NT, NT, NT, NT, INTERNATIONAL, True, NT, NT, NT, NT, NT, False, NT],
    [NT, NT, NT, NT, NT, NT, True, NT, NT, NT, NT, NT, NT, False],
    [NT, NT, NT, NT, NT, NT, NT, True, False, NT, NT, NT, NT, NT],
    [NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT],
    [NT, NT, NT, NT, NT, NT, True, NT, NT, NT, False, NT, NT, NT],
    [NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT],
    [NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT, NT],
    [NT, NT, NT, True, NT, NT, NT, NT, NT, False, NT, NT, NT, NT],
    [NT, NT, NT, NT, True, NT, NT, NT, NT, False, NT, NT, NT, NT],
    [NT, NT, NT, NT, NT, True, NT, NT, NT, NT, False, NT, NT, NT],
]
