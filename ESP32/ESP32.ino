#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include <DHTesp.h>
#include <Adafruit_BMP280.h>

//CONEXÕES WIFI E MQTT
const char* ssid = "RIRI 2G";
const char* password = "riri2521";
const char* mqtt_server = "mqtt-dashboard.com";
const char* mqtt_topic  = "casa/ricardoraitarozubcov/teste/esp32";

//PINOS DHT E BMP280
const int DHT_PIN = 14;
const int SDA_PIN = 21;
const int SCL_PIN = 22;

DHTesp dht;
Adafruit_BMP280 bmp; 
WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  Serial.begin(115200);
  Serial.print("\nConectando: ");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500); Serial.print(".");
  }
  Serial.print("\nWi-Fi Conectado!");
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Tentando conexão MQTT...");
    String clientId = "ESP32-Fish-" + String(random(1000, 9999));
    
    if (client.connect(clientId.c_str())) {
      Serial.println(" MQTT Conectado!");
    } else {
      Serial.print(" Falhou, erro rc="); Serial.print(client.state());
      Serial.println(". Nova tentativa em 5 segundos.");
      delay(5000);
    }
  }
}

void setup() {
  setup_wifi();
  client.setServer(mqtt_server, 1883);

  // Inicializa o DHT11
  dht.setup(DHT_PIN, DHTesp::DHT11);

  // Inicializa o BMP280
  Wire.begin(SDA_PIN, SCL_PIN);

  // Testa o BMP280
  if (!bmp.begin(0x76)) {
    Serial.println("BMP280 nao encontrado!");
    while (true) { delay(100); }
  }
}

void loop() {
  if (!client.connected()) reconnect();
  client.loop();

    // Leitura do DHT11
    TempAndHumidity dados = dht.getTempAndHumidity();
    float temperatura = dados.temperature;
    float umidade = dados.humidity;

    // Leitura do BMP280
    float pressao = bmp.readPressure() / 100.0;

    // Verifica a leitura do DHT11
    if (isnan(temperatura) || isnan(umidade)) {
      Serial.println("Erro no DHT11.");
      return; 
    }

    // Verifica se as condições foram atingidos
    bool T1 = (temperatura > 17.00 && temperatura <= 30.00);
    bool U1 = (umidade >= 40.00 && umidade <= 75.00);
    bool P1 = (pressao > 1011.00 && pressao <= 1020.00);
    bool T2 = ((temperatura >= 12.00 && temperatura <= 17.00) || (temperatura > 30.00 && temperatura <= 39.00)); 
    bool U2 = ((umidade >= 20.00 && umidade < 40.00) || (umidade > 75.00 && umidade <= 85.00)); 
    bool P2 = ((pressao >= 1005.00 && pressao <= 1011.00) || (pressao > 1020.00));
    bool T3 = (temperatura < 12.00 || temperatura > 39.00);
    bool U3 = (umidade < 20.00 || umidade > 85.00);
    bool P3 = pressao < 1005.00;

    String status_pesca = "";
    if (T3 || U3 || P3) status_pesca = "NÃO PESCAR";
    else if (T1 && U1 && P1) status_pesca = "PESCA IDEAL";
    else if (T2 || U2 || P2) status_pesca = "PESCAR COM CAUTELA";
    

    // Formata o pacote JSON para transmissao
    String payload = "{\"temp\":" + String(temperatura, 2) + 
                     ",\"umid\":" + String(umidade, 2) + 
                     ",\"pres\":" + String(pressao, 2) + 
                     ",\"status\":\"" + status_pesca + "\"}";

    // Exibe os resultados do envio
    Serial.print("Enviando dados: "); Serial.println(payload);
    
    if(client.publish(mqtt_topic, payload.c_str())) {
      Serial.println("--> Envio feito com sucesso!");
    } else {
      Serial.println("--> Falha ao enviar.");
    }
  
  delay(6000);
}