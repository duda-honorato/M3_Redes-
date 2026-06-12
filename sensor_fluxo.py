import socket
import time
import random
from datetime import datetime
from shared.config import UDP_HOST_GATEWAY, UDP_PORT_GATEWAY

class SensorFluxo:
    def __init__(self, id_sensor="F01"):
        self.id_sensor = id_sensor
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.gateway_addr = (UDP_HOST_GATEWAY, UDP_PORT_GATEWAY)
        
    def gerar_leitura_fluxo(self):
        # Simula quantidade de veículos no período
        qtde_veiculos = random.randint(5, 50)
        periodo_seg = 30  # período fixo de 30 segundos
        return qtde_veiculos, periodo_seg
    
    def enviar_leitura(self):
        qtde, periodo = self.gerar_leitura_fluxo()
        timestamp = datetime.now().isoformat()
        # Formato: FLUXO;<id_sensor>;<qtde_veiculos>;<periodo_seg>;<timestamp>
        mensagem = f"FLUXO;{self.id_sensor};{qtde};{periodo};{timestamp}"
        
        self.sock.sendto(mensagem.encode(), self.gateway_addr)
        print(f"[FLUXO {self.id_sensor}] Enviado: {qtde} veículos em {periodo}s")
        
    def executar(self, intervalo=30):
        print(f"🟢 Sensor Fluxo {self.id_sensor} iniciado (UDP cliente)")
        try:
            while True:
                self.enviar_leitura()
                time.sleep(intervalo)
        except KeyboardInterrupt:
            print(f"\n🔴 Sensor Fluxo {self.id_sensor} encerrado")
            self.sock.close()
if __name__ == "__main__":
    fluxo = SensorFluxo("F01")
    fluxo.executar()
