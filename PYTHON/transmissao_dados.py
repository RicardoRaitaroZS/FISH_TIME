import paho.mqtt.client as mqtt
import csv
import json
from datetime import datetime

HOST = "mqtt-dashboard.com"
PORT = 1883
TOPIC = "casa/ricardoraitarozubcov/teste/esp32"

DADOS_ESTACAO = "dados_estacao.csv"


# Verifica Conexão MQTT

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Conectado com sucesso!")
        # Entra no tópico 
        client.subscribe(TOPIC)
    else:
        print(f"Falha ao conectar. Código: {reason_code}")

def on_message(client, userdata, msg):
    # CONVERTER PARA TEXTO
    payload = msg.payload.decode('utf-8')
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"[{data}] Novo pacote recebido: {payload}")
    
    temp = ""
    umid = ""
    pres = ""
    status = ""

    try:
        # ARMAZENAR DADOS EM DICIONÁRIO
        dados_json = json.loads(payload)

        temp = dados_json.get("temp", "")
        umid = dados_json.get("umid", "")
        pres = dados_json.get("pres", "")
        status = dados_json.get("status", "")
        
        
        # SALVAR DADOS NO CSV
        with open(DADOS_ESTACAO, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([data, temp, umid, pres, status]) 

# INICIAR MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

# CONEXÃO
print(f"Conectando ao MQTT")
client.connect(HOST, PORT, keepalive=60)

# MANTER TRANSMISSÃO EM TEMPO REAL
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nEncerrando coleta de dados...")
    client.disconnect()        