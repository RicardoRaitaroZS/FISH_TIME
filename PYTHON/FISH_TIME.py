import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# CONFIG STREAMLIT
st.set_page_config(
    page_title="Fish Time Dashboard", layout="wide", initial_sidebar_state="expanded"
)

# TRATAMENTO
df = pd.read_csv("dados_estacao.csv")
df.head()
df.info()
df["Data_Hora"] = pd.to_datetime(df["Data_Hora"], format="%Y-%m-%d %H:%M:%S")
df.info()

# CONDIÇÕES DE PESCA
condicao = df["Condicao_Pesca"].iloc[-1]
texto_condição = ""
imagem_condicao = ""

if condicao == "NÃO PESCAR":
    texto_condição = "As condições climáticas estão totalmente desfavoráveis para a pesca. Não pesque!"
    imagem_condicao = "https://media.canva.com/v2/image-resize/format:PNG/height:447/quality:100/uri:ifs%3A%2F%2FM%2F27d678fa-ab91-4a78-8867-73d094949de3/watermark:F/width:447?csig=AAAAAAAAAAAAAAAAAAAAAFtvemoxv9Y8eJe_OTPaHPYGZG6G5wtlkX3_a39w4AML&exp=1793303889&osig=AAAAAAAAAAAAAAAAAAAAAGGA2eivEMblPS_oMU8FPI-wHrt389OtGaH1PTclqnBa&signer=media-rpc&token=AAIAAU0AJDI3ZDY3OGZhLWFiOTEtNGE3OC04ODY3LTczZDA5NDk0OWRlMwAAAAABoYk9xGgD5KrWt8eV2Sb0Mpt3cFile4HCYFf8h_Q4eWJv3gGXrw&x-canva-quality=screen"
    
elif condicao == "PESCA IDEAL":
    texto_condição = "As condições climáticas estão favoráveis para a pesca. Pesque tranquilamente!"
    imagem_condicao = "https://media.canva.com/v2/image-resize/format:PNG/height:800/quality:100/uri:ifs%3A%2F%2FM%2Fcc24582f-5258-4dff-bb87-f88e36d17eb8/watermark:F/width:800?csig=AAAAAAAAAAAAAAAAAAAAAJhFBhgFXSp4GItbsgg6K1_B2L0oyrt-2ps9bp5F7LMm&exp=1793307740&osig=AAAAAAAAAAAAAAAAAAAAAN6vy3-o-zZgzDWkktGy-n5k5_NthDaE3TzDxak2Rxxt&signer=media-rpc&token=AAIAAU0AJGNjMjQ1ODJmLTUyNTgtNGRmZi1iYjg3LWY4OGUzNmQxN2ViOAAAAAABoYl4h2AHu3jJPk4X9qDl8I0P2oLoB1hNesvZb-NWJZMVHt0T2w&x-canva-quality=screen"

elif condicao == "PESCAR COM CAUTELA":
    texto_condição = "As condições climáticas estão medianas para a pesca. Pesque com atenção!"
    imagem_condicao = "https://media.canva.com/v2/image-resize/format:PNG/height:800/quality:100/uri:ifs%3A%2F%2FM%2F028626fb-8ec2-4877-89e2-4baed9cfe5ab/watermark:F/width:800?csig=AAAAAAAAAAAAAAAAAAAAAID4erPXNYxfVB0VM3sOrOqIb30pEr3Zx1ioFjLI-EGK&exp=1793308933&osig=AAAAAAAAAAAAAAAAAAAAALWT-9ob1oX0OvXZpYL17MjjZ0n6eNhnJduRjtrtEI-L&signer=media-rpc&token=AAIAAU0AJDAyODYyNmZiLThlYzItNDg3Ny04OWUyLTRiYWVkOWNmZTVhYgAAAAABoYmKu4jGWBO--Xntr_WKyNM3flae1qQCKk93PzdziB1OHLcw1Q&x-canva-quality=screen"

# GRÁFICOS
# GRÁFICO TEMPERATURA
fig_temp = px.line(
    df, x="Data_Hora", y="Temperatura", markers=True
)
fig_temp.update_layout(
    title= {"text":"Variação da Temperatura", "x": 0.02, "y": 0.97 },
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

# DASHBOARD
# RESOLVER BUG VISUAL
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
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
        min-width: 320px;
        max-width: 320px;
        }
        
        /* Barra de Navegação sempre aberta */
        [data-testid="stSidebarCollapseButton"] {
        display: none !important;}
        
        /* Botões Navegação Lateral */
        [data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
            display: none !important;
        }
        [data-testid="stSidebar"] div[role="radiogroup"] label {
            background-color: transparent;
            padding: 12px 15px ;
            border-radius: 10px; 
            margin-bottom: 8px;
            cursor: pointer;
            transition: all 0.3s ease ;
            display: flex;
            align-items: center;
            width: 100% ;
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
        }

        /* Gráficos */
        [data-testid="stPlotlyChart"]{
            background-color: #FFFDFC;
            border-radius: 15px;
            overflow: hidden;
        }
        
        /* Cards de Temperatura,Umidade e Pressão */
        [data-testid="stMetric"] {
            background-color: #FFFFFC;
            padding: 15px;
            border-radius: 20px;
            box-shadow: 5px 5px 5px 6px rgba(0,0,0,0.1);
        }

        /* Card Condicao Atual */
        .painel-status-pesca {
            background: linear-gradient(to right, #1E4669, #4F77A0);
            color: white;
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 5px 6px 5px 6px rgba(0,0,0,0.1);
        }
        .painel-status-pesca h1, .painel-status-pesca p {
            color: white;
            margin: 0;
        }
        
        /* Cards das condições de pesca (Alerta) */
        .card-alerta {
            padding: 20px;
            border-radius: 15px;
            height: 350px;
            width: 330px;
            display: flex ;
            margin-right: 20px;
            position: relative;
            flex-direction: column;
            border-top: 5px solid;
            background-color: #FFFBFB;
            box-shadow: 5px 8px 8px 5px rgba(0,0,0,0.15);
        }
        /* Borda superior (Card Condições) */
        .condicao-ideal { border-top-color: #28a745; }
        .condicao-cautela { border-top-color: #ffc107; }
        .condicao-nao-pescar { border-top-color: #dc3545; }
        
            
        /* Posição das imagens dos cards */
        .container {
            .card-imagem {
            display: flex;
            align-items: center; 
            }
        }
    </style>
""",
    unsafe_allow_html=True,
)


# BARRA LATERAL
st.sidebar.markdown(
    """
<div class = "card-imagem">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZzOAGfjS6PH-OhKwbUjsoa6qxuM7D3meU_ekCeDHdqg&s=10", width = 60, style = "border-radius: 30px; margin-right:13px" >
                <p style = "margin-left: 70px;margin-top: -52px; font-size:20px"><b>FISH TIME</b></p>
                <p style = "margin-left: 70px;margin-top: -20px; font-size:11px;margin-bottom: 40px">Estação Metereológica para Pescadores</p>
            <div>
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
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="painel-status-pesca">
            <div class = "card-imagem" >
                <span style="background-color: rgb(40,167,69,0.5); padding: 2px 10px; border-radius: 20px; font-size: 12px">● CONDIÇÃO ATUAL</span>
                <h1 style = "margin-top: 20px">{condicao}</h1>
                <p style = "font-size:12px; margin-bottom: 10px; margin-top: -30px">{texto_condição} <img src="{imagem_condicao}", width = 160, style = "border-radius: 200px; margin-left: 355px; margin-top: -100px;"</p>
            </div>
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
    st_autorefresh(interval=4000)
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
            <img src="https://images.vexels.com/media/users/3/340641/isolated/preview/ced6b7b631be3178b1fcbb41c94de64c-design-minimalista-de-marca-de-verificacao-verde.png", width = 45, style = "background: rgba(13, 224, 63, 0.08); border-radius: 10px; padding: 5px">
            <br>
            <h4 style="color: #28a745;font-size: 17px; background: rgba(13, 224, 63, 0.07); border-radius: 12px; padding: 3px; margin-right: 47%; margin-left:3px; margin-top: -10px">🟢 PESCA IDEAL</h4>
            <p style = "font-size: 10px">Condições favoráveis para pesca!</p>
            <br>
            <! TEMPERATURA >
            <div class = "card-imagem">
                <img src="https://static.vecteezy.com/ti/vetor-gratis/p1/79527626-esboco-clima-temperatura-icone-com-sol-e-floco-de-neve-placa-simbolo-vetor.jpg", width = 45, style = "margin-top: -20px">
                <p style = "margin-left: 55px;margin-top: -41px; font-size:11px;margin-bottom: 40px"><b>Temperatura:</b> <br>18°C a 30°C </p>
            <div>
            <! UMIDADE >
            <div class = "card-imagem">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYz6qd9VIcFwnJsETmCQRKMjj268PUZ-f19gHYB6_sFQ&s=10", width = 37, style = "padding: 4px; border: 2px solid black; border-radius: 15px; margin-left: 4px ; margin-top:-40px">
                <p style = "margin-left: 55px;margin-top: -50px; font-size:11px; margin-bottom: 40px"><b>Umidade:</b> <br> 40% a 75% </p>
            <div>
            <! PRESSÃO >
            <div class = "card-imagem">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoYIHDufOiCP5d985ogQc7aFOH-7rv3tNsyy6qLi1FgA&s=10", width = 37, style = "padding: 4px; border: 2px solid black; border-radius: 15px; margin-left: 4px ; margin-top:-37px">
                <p style = "margin-left: 55px;margin-top: -48px; font-size:11px; margin-bottom: 40px"><b>Pressão atmosférica:</b> <br> 1012 a 1020 hpa</p>
            <div>            
        </div>
        """,
        unsafe_allow_html=True,
    )

    cautela_col.markdown(
        """
        <div class="card-alerta condicao-cautela">
            <br>
            <img src="https://icones.pro/wp-content/uploads/2022/02/icone-de-cloche-et-d-alerte-jaune.png", width = 45, style = "background: rgba(254, 217, 5, 0.1); border-radius: 10px; padding: 5px">
            <br>
            <h4 style="color: #ffc107; font-size: 17px; background: rgba(254, 217, 5, 0.1); border-radius: 12px; padding: 3px; margin-right: 22%; margin-left:3px; margin-top: -10px">🟡 PESCAR COM CAUTELA</h4>
            <p style = "font-size: 10px">Condições com algum fator de atenção!</p>
            <br>
            <! TEMPERATURA >
            <div class = "card-imagem">
                <img src="https://static.vecteezy.com/ti/vetor-gratis/p1/79527626-esboco-clima-temperatura-icone-com-sol-e-floco-de-neve-placa-simbolo-vetor.jpg", width = 45, style = "margin-top: -20px">
                <p style = "margin-left: 55px;margin-top: -41px; font-size:11px;margin-bottom: 40px"><b>Temperatura:</b> <br>12-17°C ou 31-39°C</p>
            <div>
            <! UMIDADE >
            <div class = "card-imagem">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYz6qd9VIcFwnJsETmCQRKMjj268PUZ-f19gHYB6_sFQ&s=10", width = 37, style = "padding: 4px; border: 2px solid black; border-radius: 15px; margin-left: 4px ; margin-top:-40px">
                <p style = "margin-left: 55px;margin-top: -50px; font-size:11px; margin-bottom: 40px"><b>Umidade:</b> <br>20-39% ou 76-85%</p>
            <div>
            <! PRESSÃO >
            <div class = "card-imagem">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoYIHDufOiCP5d985ogQc7aFOH-7rv3tNsyy6qLi1FgA&s=10", width = 37, style = "padding: 4px; border: 2px solid black; border-radius: 15px; margin-left: 4px ; margin-top:-37px">
                <p style = "margin-left: 55px;margin-top: -48px; font-size:11px; margin-bottom: 40px"><b>Pressão atmosférica:</b> <br>1005-1011 ou Maior que 1020 hpa</p>
            <div>                        
        </div>
        """,
        unsafe_allow_html=True,
    )

    n_pescar_col.markdown(
        """
        <div class="card-alerta condicao-nao-pescar">
            <br>
            <img src="https://icones.pro/wp-content/uploads/2022/02/icone-de-cloche-et-d-alerte-rouge.png", width = 45, style = "background: rgba(230, 2, 2, 0.08); border-radius: 10px; padding: 5px">
            <br>
            <h4 style="color: #dc3545;font-size: 16px; background: rgba(230, 2, 2, 0.08); border-radius: 12px; padding: 5px; margin-right:48%; margin-left:3px; margin-top: -10px">🔴 NÃO PESCAR</h4>
            <p style = "font-size: 10px">Condições climáticas extremas!</p>
            <br>
            <! TEMPERATURA >
            <div class = "card-imagem">
                <img src="https://static.vecteezy.com/ti/vetor-gratis/p1/79527626-esboco-clima-temperatura-icone-com-sol-e-floco-de-neve-placa-simbolo-vetor.jpg", width = 45, style = "margin-top: -20px">
                <p style = "margin-left: 55px;margin-top: -41px; font-size:11px;margin-bottom: 40px"><b>Temperatura:</b> <br>Menor que 12°C ou Maior que 39°C</p>
            <div>
            <! UMIDADE >
            <div class = "card-imagem">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYz6qd9VIcFwnJsETmCQRKMjj268PUZ-f19gHYB6_sFQ&s=10", width = 37, style = "padding: 4px; border: 2px solid black; border-radius: 15px; margin-left: 4px ; margin-top:-40px">
                <p style = "margin-left: 55px;margin-top: -50px; font-size:11px; margin-bottom: 40px"><b>Umidade:</b> <br> Menor que 20% ou Maior que 85% </p>
            <div>
            <! PRESSÃO >
            <div class = "card-imagem">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoYIHDufOiCP5d985ogQc7aFOH-7rv3tNsyy6qLi1FgA&s=10", width = 37, style = "padding: 4px; border: 2px solid black; border-radius: 15px; margin-left: 4px ; margin-top:-37px">
                <p style = "margin-left: 55px;margin-top: -48px; font-size:11px; margin-bottom: 40px"><b>Pressão atmosférica:</b> <br> Menor que 1005hpa </p>
            <div>                            
        </div>
        """,
        unsafe_allow_html=True,
    )

    # CONDIÇÃO ATUAL
    st.divider()
    st.markdown(
            f"""
            <div class="painel-status-pesca">
                <div class = "card-imagem" >
                    <span style="background-color: rgb(40,167,69,0.5); padding: 2px 10px; border-radius: 20px; font-size: 12px">● CONDIÇÃO ATUAL</span>
                    <h1 style = "margin-top: -10px; font-size: 28px">{condicao}</h1>
                    <p style = "font-size:10px; margin-top: -10px">{texto_condição} <img src="{imagem_condicao}", width = 90, style = "border-radius: 200px; margin-left: 405px; margin-top: -75px;"</p>
                </div>
            </div>""",
            unsafe_allow_html=True,
        )
    st.divider()