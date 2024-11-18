from transitions import Machine

class CitasMedicas():
    def __init__(self):
        self.states = ['cita_solicitada', 'cita_confirmada', 'recordatorio_enviado', 'cita_realizada', 'cita_cancelada']
        self.machine = Machine(model=self, states=self.states, initial='cita_solicitada')
        
        self.machine.add_transition(trigger='confirmar_cita', source='cita_solicitada', dest='cita_confirmada')
        self.machine.add_transition(trigger='enviar_recordatorio', source='cita_confirmada', dest='recordatorio_enviado')
        self.machine.add_transition(trigger='realizar_cita', source='recordatorio_enviado', dest='cita_realizada')
        self.machine.add_transition(trigger='cancelar_cita', source='cita_solicitada', dest='cita_cancelada')

sistema = CitasMedicas()
print(sistema.state) # cita_solicitada
sistema.confirmar_cita()
print(sistema.state) # cita_confirmada
sistema.enviar_recordatorio()
print(sistema.state) # recordatorio_enviado
sistema.realizar_cita()
print(sistema.state) # cita_realizada
