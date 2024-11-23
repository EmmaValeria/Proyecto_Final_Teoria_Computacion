import json

import customtkinter

from states import AUTOMATON, REJECT_STATES, STATES


class ShipmentControl(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.shipments = []
        self.controller = controller
        self.shipment = None

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.back_button = customtkinter.CTkButton(
            self,
            text="Volver",
            command=lambda: controller.show_frame(self._get_shipments()),
        )
        self.back_button.grid(row=0, column=0)

        self.data_container = customtkinter.CTkFrame(self)
        self.data_container.grid(row=1, column=0, columnspan=6, sticky="nsew")

        self.state_container = customtkinter.CTkFrame(self)
        self.state_container.grid(row=2, column=0, columnspan=6, sticky="nsew")
        self.state_container.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.actions_container = customtkinter.CTkFrame(self)
        self.actions_container.grid(row=3, column=0, columnspan=6, sticky="nsew")
        self.actions_container.grid_columnconfigure((0, 1, 2), weight=1)

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
            print("Cambios guardados")
        except FileNotFoundError:
            pass

    def set_new_state(self, state):
        self.shipment["current_state"] = state
        self.save_changes()
        self.display_data()

    def display_actions(self):
        state = self.shipment["current_state"]
        state_index = STATES[state]
        actions = AUTOMATON[state_index]
        column_counter = 0

        for widget in self.actions_container.winfo_children():
            widget.destroy()

        for i, action in enumerate(actions):
            if action != "X":
                action_state = next((k for k, v in STATES.items() if v == i), None)
                button = customtkinter.CTkButton(
                    self.actions_container,
                    text=action_state,
                    command=lambda s=action_state: self.set_new_state(s),
                )
                if action_state in REJECT_STATES:
                    button.configure(fg_color="red", hover_color="red")
                button.grid(row=0, column=column_counter)
                column_counter += 1

    def display_data(self):
        self.set_shipment(self.controller.get_shipment())
        if not self.shipment:
            return

        for widget in self.data_container.winfo_children():
            widget.destroy()

        for widget in self.state_container.winfo_children():
            widget.destroy()

        self.tracking_number_label = customtkinter.CTkLabel(
            self.data_container, text=self.shipment["tracking_number"]
        )
        self.tracking_number_label.grid(row=1, column=0)

        self.origin_label = customtkinter.CTkLabel(
            self.data_container, text=self.shipment["origin"]
        )
        self.origin_label.grid(row=2, column=0)

        self.destination_label = customtkinter.CTkLabel(
            self.data_container, text=self.shipment["destination"]
        )
        self.destination_label.grid(row=2, column=1)

        self.current_state_label = customtkinter.CTkLabel(
            self.state_container, text=self.shipment["current_state"]
        )
        self.current_state_label.grid(row=0, column=0, columnspan=6)

        self.display_actions()
