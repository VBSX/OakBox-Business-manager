from datetime import datetime

class HorarioDoSistema:
    def __init__(self):
        
        pass

    def get_horario_sistema(self):
        hora_atual = datetime.strftime(datetime.now(), "%H:%M:%S")
        
        return hora_atual

    def get_data_sistema(self):
        hoje = datetime.now()
        data_atual = hoje.strftime("%d/%m/%y")
        
        return data_atual

h = HorarioDoSistema()
print(h.get_horario_sistema())