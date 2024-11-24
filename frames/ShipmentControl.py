import json

import customtkinter

from lib.constants import AUTOMATON, REJECT_STATES, STATES


class ShipmentControl(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.shipments = []
        self.controller = controller
        self.shipment = None

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        self.back_button = customtkinter.CTkButton(
            self,
            text="Volver",
            command=lambda: controller.show_frame(self._get_shipments()),
        )
        self.back_button.grid(row=0, column=0, pady=10)

        self.data_container = customtkinter.CTkFrame(self)
        self.data_container.grid(row=1, column=0, columnspan=8, sticky="nsew")
        self.data_container.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        self.state_container = customtkinter.CTkFrame(self)
        self.state_container.grid(row=2, column=0, columnspan=8, sticky="nsew")
        self.state_container.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.actions_container = customtkinter.CTkFrame(self)
        self.actions_container.grid(row=3, column=0, columnspan=8, sticky="nsew")

    def _get_shipments(self):
        from frames.Shipments import Shipments

        return Shipments

    def set_shipment(self, shipment):

        try:
            with open("shipments.json", "r") as f:
                self.shipments = json.load(f)
                f.close()
        except FileNotFoundError:
            self.shipments = []

        for s in self.shipments:
            if s == shipment:
                self.shipment = s
                break

    def save_changes(self):
        try:
            with open("shipments.json", "w") as f:
                json.dump(self.shipments, f)
                f.close()
        except FileNotFoundError:
            pass

    def set_new_state(self, state):
        for i, s in enumerate(self.shipments):
            if s == self.shipment:
                self.shipment["current_state"] = state
                self.shipment["history"].append(state)
                self.shipments[i] = self.shipment
                break

        self.save_changes()
        self.display_data()

    def display_actions(self):
        state = self.shipment["current_state"]
        state_index = STATES[state]
        actions = AUTOMATON[state_index]

        for widget in self.actions_container.winfo_children():
            widget.destroy()

        for i, action in enumerate(actions):
            if action != "X":
                action_state = next((k for k, v in STATES.items() if v == i), None)
                button = customtkinter.CTkButton(
                    self.actions_container,
                    text=action_state,
                    command=lambda s=action_state: self.set_new_state(s),
                    width=150,
                    height=40,
                    font=("Arial", 18),
                )
                if action_state in REJECT_STATES:
                    button.configure(fg_color="red", hover_color="red")
                button.pack(pady=10, padx=10, anchor="center")

    def display_data(self):
        self.set_shipment(self.controller.get_shipment())
        if not self.shipment:
            return

        for widget in self.data_container.winfo_children():
            widget.destroy()

        for widget in self.state_container.winfo_children():
            widget.destroy()

        self.tracking_number_label = customtkinter.CTkLabel(
            self.data_container,
            text=f"Numero de rastreo: {self.shipment['tracking_number']}",
            font=("Arial", 18),
        )
        self.tracking_number_label.grid(row=1, column=0, pady=10, padx=10)

        self.origin_label = customtkinter.CTkLabel(
            self.data_container,
            text=f"Origen: {self.shipment['origin']}",
            font=("Arial", 16),
        )
        self.origin_label.grid(row=2, column=0, pady=5, padx=5, columnspan=4)

        self.destination_label = customtkinter.CTkLabel(
            self.data_container,
            text=f"Destino: {self.shipment['destination']}",
            font=("Arial", 16),
        )
        self.destination_label.grid(row=2, column=4, pady=5, padx=5, columnspan=4)

        self.current_state_label = customtkinter.CTkLabel(
            self.state_container,
            text=f"Estado Actual: {self.shipment['current_state']}",
            font=("Arial", 20),
        )
        self.current_state_label.grid(row=0, column=0, columnspan=6)

        self.display_actions()
