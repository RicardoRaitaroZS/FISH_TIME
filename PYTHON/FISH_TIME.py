import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# CONFIG STREAMLIT
st.set_page_config(
    page_title="Fish Time Dashboard", layout="wide", initial_sidebar_state="expanded"
)

# TRATAMENTO DOS DADOS
df = pd.read_csv("PYTHON/dados_estacao.csv")
df.head()
df.info()
df["Data_Hora"] = pd.to_datetime(df["Data_Hora"], format="%Y-%m-%d %H:%M:%S")
df.info()

# CONDIÇÕES DE PESCA
condicao = df["Condicao_Pesca"].iloc[-1]
texto_condicao = ""
imagem_condicao = ""

if condicao == "NÃO PESCAR":
    texto_condicao = "As condições climáticas estão totalmente desfavoráveis para a pesca. Não pesque!"
    imagem_condicao = "app/static/nao_pescar.png"
    
elif condicao == "PESCA IDEAL":
    texto_condicao = "As condições climáticas estão favoráveis para a pesca. Pesque tranquilamente!"
    imagem_condicao = "app/static/pesca_ideal.png"

elif condicao == "PESCAR COM CAUTELA":
    texto_condicao = "As condições climáticas estão medianas para a pesca. Pesque com atenção!"
    imagem_condicao = "app/static/pescar_cautela.png"

# GRÁFICOS
# GRÁFICO TEMPERATURA
fig_temp = px.line(
    df, x="Data_Hora", y="Temperatura", markers=True
)
fig_temp.update_layout(
    title= {"text":"Variação da Temperatura", "x": 0.02, "y": 0.97 },
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=0, r=0, t=40, b=0),
    xaxis_title = "Data/Hora",
    yaxis_title = "Temperatura (°C)",
)
fig_temp.update_traces(
    line_color="#006ECE", fill="toself", fillcolor="rgba(0, 110, 206, 0.15)"
)

# GRÁFICO UMIDADE
fig_umi = px.line(
    df, x="Data_Hora", y="Umidade", markers=True
)
fig_umi.update_layout(
    title= {"text":"Variação da Umidade", "x": 0.02, "y": 0.97 },
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=0, r=0, t=40, b=0),
    xaxis_title = "Data/Hora",
    yaxis_title = "Umidade (%)",    
)
fig_umi.update_traces(
    line_color="#45B69C", fill="toself", fillcolor="rgba(69, 182, 156, 0.15)"
)

# GRÁFICO PRESSÃO
fig_pressao = px.line(
    df,
    x="Data_Hora",
    y="Pressao",
    markers=True,
)
fig_pressao.update_layout(
    title= {"text": "Variação da pressão atmosférica", "x": 0.02, "y": 0.97 },
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=0, r=0, t=40, b=0),
    xaxis_title = "Data/Hora",
    yaxis_title = "Pressão(hpa)",    
)
fig_pressao.update_traces(
    line_color="#7243B9", fill="toself", fillcolor="rgba(114, 67, 185, 0.15)"
)

# RESOLUÇÃO DO DASHBOARD
resolucao = """
<style>
    .block-container {
        width: 95% !important;
        max-width: 1400px !important;
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        margin: 0 auto !important;
    }
</style>
"""
st.markdown(resolucao, unsafe_allow_html=True)


# LAYOUT E DESIGN GERAL DO DASHBOARD
st.markdown(
    """
    <style>
        /* Cor de Fundo Principal */
        [data-testid="stAppViewContainer"] {
            background-color: #FAF7F2;
        }
        
        /* Cor de Fundo e Texto da barra lateral */
        [data-testid="stSidebar"] {
            background-color: #172443;
        }
        [data-testid="stSidebar"] * {
            color: #FFFFFF !important;
        }

        /* Barra de Naveação */
        [data-testid="stSidebar"] {
            min-width: 280px;
            max-width: 320px;
            width: 100%;
        }
        
        /* Barra de Navegação sempre aberta */
        [data-testid="stSidebarCollapseButton"] {
            display: none !important;
        }
        
        /* Botões Navegação Lateral */
        [data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
            display: none !important;
        }
        [data-testid="stSidebar"] div[role="radiogroup"] label {
            background-color: transparent;
            padding: 12px 15px;
            border-radius: 10px; 
            margin-bottom: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            width: 100%;
            border: none;
        }
        
        /* Efeito de passar o mouse */
        [data-testid="stSidebar"] div[role="radiogroup"] label:hover {
            background-color: rgba(255,255,255,0.05) !important;
        }
        
        /* Quando o botão foi selecionado */
        [data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
            background-color: #2D4067 !important;
        }
        
        /* Texto do botão INATIVO */
        [data-testid="stSidebar"] div[role="radiogroup"] label p {
            color: #A0AEC0 !important;
            font-size: 16px !important;
            font-weight: 500 !important;
            margin: 0 !important;
        }
        
        /* Texto do botão ATIVO */
        [data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {
            color: #FFFFFF !important;
        }
        
        /* Tabela de Histórico */
        [data-testid="stDataFrame"] {
            background-color: #FFFDFC;
            padding: 20px;
            border-radius: 15px;
            overflow: hidden;
            width: 100% !important;
        }

        /* Gráficos */
        [data-testid="stPlotlyChart"] {
            background-color: #FFFDFC;
            border-radius: 15px;
            overflow: hidden;
            width: 100% !important;
        }
        
        /* Cards de Temperatura,Umidade e Pressão */
        [data-testid="stMetric"] {
            background-color: #FFFFFC;
            padding: 15px;
            border-radius: 20px;
            box-shadow: 5px 5px 5px 6px rgba(0,0,0,0.1);
            width: 100%;
        }

        /* Card Condicao Atual */
        .painel-status-pesca {
            background: linear-gradient(to right, #1E4669, #4F77A0);
            color: white;
            padding: 28px 30px;
            border-radius: 15px;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 5px 6px 5px 6px rgba(0,0,0,0.1);
            box-sizing: border-box;
            width: 100%;
        }
        .painel-status-pesca h1 {
            color: white;
            margin: 4px 0 8px 0;
            font-size: 38px;
        }
        .painel-status-pesca p {
            color: white;
            margin: 0;
            font-size: 11px;
        }
        .img-status-pesca {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            object-fit: cover;
            flex-shrink: 0;
            margin-left: 20px;
        }
        
        /* Cards das condições de pesca (Alertas)*/
        .card-alerta {
            padding: 20px;
            border-radius: 15px;
            min-height: 380px;
            width: 100% !important;
            display: flex;
            position: relative;
            flex-direction: column;
            border-top: 5px solid;
            background-color: #FFFBFB;
            box-shadow: 5px 8px 8px 5px rgba(0,0,0,0.15);
            box-sizing: border-box;
        }
        /* Borda superior (Card Condições) */
        .condicao-ideal { border-top-color: #28a745; }
        .condicao-cautela { border-top-color: #ffc107; }
        .condicao-nao-pescar { border-top-color: #dc3545; }
        
        /* Posição das imagens dos cards */
        .card-linha-item {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 20px;
        }
        .card-linha-item img {
            flex-shrink: 0;
        }
        .card-linha-item p {
            margin: 0 !important;
            font-size: 11px;
            line-height: 1.35;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# BARRA LATERAL
st.sidebar.markdown(
    """
    <div style="display: flex; align-items: center; gap: 13px; margin-bottom: 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZzOAGfjS6PH-OhKwbUjsoa6qxuM7D3meU_ekCeDHdqg&s=10" width="60" height="60" style="border-radius: 30px; object-fit: cover; flex-shrink: 0;">
        <div>
            <p style="margin: 0; font-size: 20px; font-weight: bold; line-height: 1.1;">FISH TIME</p>
            <p style="margin: 4px 0 0 0; font-size: 11px; color: #A0AEC0;">Estação Metereológica para Pescadores</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("""<br>""", unsafe_allow_html=True)
st.sidebar.divider()
st.sidebar.markdown("""<br>""", unsafe_allow_html=True)
navegacao = st.sidebar.radio(
    "Navegação", ["Dashboard", "Histórico", "Alertas"], label_visibility="collapsed"
)


# PÁGINA PRINCIPAL
if navegacao == "Dashboard":
    st_autorefresh(interval=6000)
    st.markdown(
        """<h5 style = "font-size: 10px;color: #00A8A8">FISH TIME / MONITORAMENTO</h5>""",
        unsafe_allow_html=True,
    )
    st.subheader("Visão geral")
    st.markdown(
        f"""
        <div class="painel-status-pesca">
            <div>
                <span style="background-color: rgba(40,167,69,0.5); padding: 2px 10px; border-radius: 20px; font-size: 12px">● CONDIÇÃO ATUAL</span>
                <h1>{condicao}</h1>
                <p style = "margin-top: -7%">{texto_condicao}</p>
            </div>
            <img src="{imagem_condicao}" class="img-status-pesca">
        </div>""",
        unsafe_allow_html=True,
    )

    # CARDS
    temperatura = df["Temperatura"].iloc[-1]
    umidade = df["Umidade"].iloc[-1]
    pressao = df["Pressao"].iloc[-1]

    temp_col, umi_col, pressao_col = st.columns(3)
    temp_col.metric("🌡️ Temperatura", f"{temperatura}°C")
    umi_col.metric("💧 Umidade", f"{umidade}%")
    pressao_col.metric("🧭 Pressão atmosférica", f"{pressao} hpa")

    # GRÁFICOS
    st.divider()
    st.plotly_chart(fig_temp, use_container_width=True)
    st.markdown(f"""<br><br>""", unsafe_allow_html=True)
    st.plotly_chart(fig_umi, use_container_width=True)
    st.markdown(f"""<br><br>""", unsafe_allow_html=True)
    st.plotly_chart(fig_pressao, use_container_width=True)
    st.divider()

# HISTÓRICO DA ESTAÇÃO
elif navegacao == "Histórico":
    st_autorefresh(interval=6000)
    st.markdown(
        """<h5 style = "font-size: 10px; color: #00A8A8">FISH TIME / MONITORAMENTO</h5>""",
        unsafe_allow_html=True,
    )
    st.subheader("Histórico dos Dados")
    st.dataframe(df)


# ALERTAS
elif navegacao == "Alertas":
    st_autorefresh(interval=6000)
    st.markdown( """<h5 style = "font-size: 10px; color: #00A8A8">FISH TIME / MONITORAMENTO</h5>""",
        unsafe_allow_html=True,)
    st.subheader("Alertas e Condições")
    st.write("Entenda como os dados meteorológicos determinam a condição para pesca.")
    st.markdown("<br>", unsafe_allow_html=True)

    # CARDS CONDIÇÕES
    ideal_col, cautela_col, n_pescar_col = st.columns(3)
    ideal_col.markdown(
        """
        <div class="card-alerta condicao-ideal">
            <br>
            <img src="https://images.vexels.com/media/users/3/340641/isolated/preview/ced6b7b631be3178b1fcbb41c94de64c-design-minimalista-de-marca-de-verificacao-verde.png" width="45" style="background: rgba(13, 224, 63, 0.08); border-radius: 10px; padding: 5px;">
            <br>
            <h4 style="color: #28a745; font-size: 14px; background: rgba(13, 224, 63, 0.07); border-radius: 12px; padding: 3px 8px; width: fit-content; margin: 0 0 10px 0;">🟢 PESCA IDEAL</h4>
            <p style="font-size: 10px; margin-bottom: 25px;">Condições favoráveis para pesca!</p>
            <!-- TEMPERATURA -->
            <div class="card-linha-item">
                <img src="https://static.vecteezy.com/ti/vetor-gratis/p1/79527626-esboco-clima-temperatura-icone-com-sol-e-floco-de-neve-placa-simbolo-vetor.jpg" width="45">
                <p><b>Temperatura:</b> <br>18°C a 30°C </p>
            </div>
            <!-- UMIDADE -->
            <div class="card-linha-item">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYz6qd9VIcFwnJsETmCQRKMjj268PUZ-f19gHYB6_sFQ&s=10" width="37" style="padding: 4px; border: 2px solid black; border-radius: 15px;">
                <p><b>Umidade:</b> <br> 40% a 75% </p>
            </div>
            <!-- PRESSÃO -->
            <div class="card-linha-item">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoYIHDufOiCP5d985ogQc7aFOH-7rv3tNsyy6qLi1FgA&s=10" width="37" style="padding: 4px; border: 2px solid black; border-radius: 15px;">
                <p><b>Pressão atmosférica:</b> <br> 1012 a 1020 hpa</p>
            </div>            
        </div>
        """,
        unsafe_allow_html=True,
    )

    cautela_col.markdown(
        """
        <div class="card-alerta condicao-cautela">
            <br>
            <img src="https://icones.pro/wp-content/uploads/2022/02/icone-de-cloche-et-d-alerte-jaune.png" width="45" style="background: rgba(254, 217, 5, 0.1); border-radius: 10px; padding: 5px;">
            <br>
            <h4 style="color: #ffc107; font-size: 14px; background: rgba(254, 217, 5, 0.1); border-radius: 12px; padding: 3px 8px; width: fit-content; margin: 0 0 10px 0;">🟡 PESCAR COM CAUTELA</h4>
            <p style="font-size: 10px; margin-bottom: 25px;">Condições com algum fator de atenção!</p>
            <!-- TEMPERATURA -->
            <div class="card-linha-item">
                <img src="https://static.vecteezy.com/ti/vetor-gratis/p1/79527626-esboco-clima-temperatura-icone-com-sol-e-floco-de-neve-placa-simbolo-vetor.jpg" width="45">
                <p><b>Temperatura:</b> <br>12-17°C ou 31-39°C</p>
            </div>
            <!-- UMIDADE -->
            <div class="card-linha-item">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYz6qd9VIcFwnJsETmCQRKMjj268PUZ-f19gHYB6_sFQ&s=10" width="37" style="padding: 4px; border: 2px solid black; border-radius: 15px;">
                <p><b>Umidade:</b> <br>20-39% ou 76-85%</p>
            </div>
            <!-- PRESSÃO -->
            <div class="card-linha-item">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoYIHDufOiCP5d985ogQc7aFOH-7rv3tNsyy6qLi1FgA&s=10" width="37" style="padding: 4px; border: 2px solid black; border-radius: 15px;">
                <p><b>Pressão atmosférica:</b> <br>1005-1011 ou Maior que 1020 hpa</p>
            </div>                        
        </div>
        """,
        unsafe_allow_html=True,
    )

    n_pescar_col.markdown(
        """
        <div class="card-alerta condicao-nao-pescar">
            <br>
            <img src="https://icones.pro/wp-content/uploads/2022/02/icone-de-cloche-et-d-alerte-rouge.png" width="45" style="background: rgba(230, 2, 2, 0.08); border-radius: 10px; padding: 5px;">
            <br>
            <h4 style="color: #dc3545; font-size: 14px; background: rgba(230, 2, 2, 0.08); border-radius: 12px; padding: 4px 8px; width: fit-content; margin: 0 0 10px 0;">🔴 NÃO PESCAR</h4>
            <p style="font-size: 10px; margin-bottom: 25px;">Condições climáticas extremas!</p>
            <!-- TEMPERATURA -->
            <div class="card-linha-item">
                <img src="https://static.vecteezy.com/ti/vetor-gratis/p1/79527626-esboco-clima-temperatura-icone-com-sol-e-floco-de-neve-placa-simbolo-vetor.jpg" width="45">
                <p><b>Temperatura:</b> <br>Menor que 12°C ou Maior que 39°C</p>
            </div>
            <!-- UMIDADE -->
            <div class="card-linha-item">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYz6qd9VIcFwnJsETmCQRKMjj268PUZ-f19gHYB6_sFQ&s=10" width="37" style="padding: 4px; border: 2px solid black; border-radius: 15px;">
                <p><b>Umidade:</b> <br> Menor que 20% ou Maior que 85% </p>
            </div>
            <!-- PRESSÃO -->
            <div class="card-linha-item">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoYIHDufOiCP5d985ogQc7aFOH-7rv3tNsyy6qLi1FgA&s=10" width="37" style="padding: 4px; border: 2px solid black; border-radius: 15px;">
                <p><b>Pressão atmosférica:</b> <br> Menor que 1005hpa </p>
            </div>                            
        </div>
        """,
        unsafe_allow_html=True,
    )

    # CONDIÇÃO ATUAL
    st.divider()
    st.markdown(
        f"""
        <div class="painel-status-pesca">
            <div>
                <span style="background-color: rgba(40,167,69,0.5); padding: 2px 10px; border-radius: 20px; font-size: 12px">● CONDIÇÃO ATUAL</span>
                <h1>{condicao}</h1>
                <p style = "margin-top: -7%">{texto_condicao}</p>
            </div>
            <img src="{imagem_condicao}" class="img-status-pesca">
        </div>""",
        unsafe_allow_html=True,
    )
    st.divider()