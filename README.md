# Fish Time — Estação Meteorológica para Pescadores

Estação meteorológica inteligente desenvolvida para monitorar o clima em tempo real e indicar condições seguras para pesca.

Projeto acadêmico desenvolvido em grupo, por alunos do curso de **Ciência da Computação — UNIP**.

---

## 📖 Sobre o Projeto

Pescadores frequentemente enfrentam a falta de informações meteorológicas locais e em tempo real sobre represas e corpos d'água. Em locais de pesca, mudanças bruscas de pressão e umidade podem gerar tempestades convectivas repentinas (com raios) e neblina espessa, colocando em risco a integridade física de quem está em embarcações ou utilizando varas de pesca.

Além da segurança humana, fatores como a **pressão atmosférica** afetam diretamente a biologia dos peixes (comprimindo ou expandindo a bexiga natatória), determinando se eles estão ativos na superfície ou abrigados no fundo. 

O **Fish Time** une hardware de baixo custo (IoT) e análise de dados para transformar leituras de sensores em tomadas de decisão claras para o pescador.

---

## ⚙️ O que o Sistema Faz

1. **Mede continuamente:**
   * 🌡️ **Temperatura do Ar** (°C)
   * 💧 **Umidade Relativa do Ar** (%)
   * ⏲️ **Pressão Atmosférica Barométrica** (hPa)
2. **Transmite os dados via protocolo MQTT** do microcontrolador para a aplicação.
3. **Classifica a condição de pesca instantaneamente** através de regras lógicas anti-falhas.
4. **Exibe um Dashboard Web interativo** em tempo real com métricas, gráficos temporais e histórico de telemetria.

---

## 🚦 Lógica de Alertas e Regra de Negócio

O sistema avalia os dados recebidos e aciona automaticamente um dos três estados operacionais:

| Status | Condição | Significado e Ação do Pescador |
| :---: | :--- | :--- |
| 🟢 | **Pesca Ideal** | Clima estável, céu limpo, temperatura agradável e pressão favorável. Peixes ativos na superfície; segurança total para navegar. |
| 🟡 | **Pescar com Cautela** | Mudança no clima (pressão caindo, tempo muito seco ou frio/calor). A pesca é produtiva, mas exige atenção contínua ao céu e equipamentos de proteção. |
| 🔴 | **Não Pescar (Perigo)** | Risco iminente de temporais severos, raios, ventania ou neblina densa na represa. Evacuação imediata recomendada. |

### Faixas de Corte do Sistema:
* **🟢 Verde:** Temperatura (17°C a 30°C) **e** Umidade (40% a 75%) **e** Pressão (> 1011 hPa a 1020 hPa).
* **🟡 Amarelo:** Temperatura (12°C a 17°C ou 30°C a 39°C) **ou** Umidade (20% a 40% ou 75% a 85%) **ou** Pressão (1005 hPa a 1011 hPa ou > 1020 hPa).
* **🔴 Vermelho:** Temperatura (< 12°C ou > 39°C) **ou** Umidade (< 20% ou > 85%) **ou** Pressão (< 1005 hPa).

---

## 🛠️ Tecnologias

* **Hardware:** ESP32, Sensor AHT21 (Temperatura/Umidade) e Sensor BMP280 (Pressão).
* **Software:** C++ (ESP32), Python (Streamlit, Pandas e Plotly).

---

## 🚀 Como rodar o código do ESP32:

#### 1. Pré-requisitos na Arduino IDE
* Ter a [Arduino IDE](https://www.arduino.cc/en/software) instalada.
* Ter o pacote de placas do ESP32 configurado:
  * Vá em **Arquivo > Preferências** e adicione a URL da Espressif em *URLs Adicionais do Gerenciador de Placas*:
    ```text
    https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
    ```
  * Vá em **Ferramentas > Placa > Gerenciador de Placas**, pesquise por `esp32` (da Espressif) e instale.

#### 2. Instalar Bibliotecas Necessárias
Vá em **Ferramentas > Gerenciar Bibliotecas...** e instale:
* `PubSubClient` (por Nick O'Leary) — para comunicação MQTT.
* `DHT sensor library` (ou `DHTesp`) — para leitura de temperatura e umidade.
* `Adafruit BMP280 Library` (ou `Adafruit BMP085`) — para pressão atmosférica.

#### 3. Configurar Wi-Fi no Código
No arquivo de código do ESP32 (`.ino`), altere as variáveis para a rede Wi-Fi da sua casa ou do roteador do seu celular (lembrando que o ESP32 opera apenas em redes **2.4 GHz**):
```cpp
const char* ssid = "NOME_DO_SEU_WIFI";
const char* password = "SENHA_DO_SEU_WIFI";
```

---

## 🚀 Como Executar os arquivos PYTHON (Dashboard e Transmissão de Dados)

### 1. Clonar o Repositório
```bash
git clone https://github.com/RicardoRaitaroZS/FISH_TIME.git
cd FISH_TIME
```

### 2. Instalar dependências (Bibliotecas Python)
```bash
pip install -r requirements.txt
```

### 3. Executar a Transmissão de Dados
```bash
python PYTHON/transmissao_dados.py
```

### 4. Executar o Dashboard
```bash
python -m streamlit run PYTHON/FISH_TIME.py
```

---
