import streamlit as st
import math
import random

# ==============================
# CONFIG
# ==============================
st.set_page_config(page_title="OmniLogic v5.0", layout="centered", page_icon="🧪")

st.title("🧪 OmniLogic v5.0")
st.subheader("Sistema de Desafios - Ciência de Dados")

# ==============================
# FUNÇÕES
# ==============================

def desafio_1():
    n1 = st.number_input("Matemática")
    n2 = st.number_input("Português")
    n3 = st.number_input("Ciências")
    if st.button("Calcular Média"):
        st.success(f"Média: {(n1+n2+n3)/3:.2f}")

def desafio_2():
    c = st.number_input("Temperatura em Celsius")
    if st.button("Converter"):
        st.success(f"{(c*9/5)+32:.2f} °F")

def desafio_3():
    r = st.number_input("Raio")
    if st.button("Calcular"):
        st.success(f"Área: {math.pi*r**2:.2f}")

def desafio_4():
    horas = st.number_input("Horas trabalhadas")
    valor = st.number_input("Valor por hora")
    if st.button("Calcular Salário"):
        st.success(f"Salário: R$ {horas*valor:.2f}")

def desafio_5():
    idade = st.number_input("Idade")
    if st.button("Verificar"):
        st.success("Pode votar" if idade >= 18 else "Não pode votar")

def desafio_6():
    nota = st.number_input("Nota")
    if st.button("Classificar"):
        if nota >= 9: c = "A"
        elif nota >= 7: c = "B"
        elif nota >= 5: c = "C"
        elif nota >= 3: c = "D"
        else: c = "E"
        st.success(f"Conceito: {c}")

def desafio_7():
    a = st.number_input("Valor 1")
    b = st.number_input("Valor 2")
    c = st.number_input("Valor 3")
    if st.button("Maior"):
        st.success(f"Maior: {max(a,b,c)}")

def desafio_8():
    a = st.number_input("Lado A")
    b = st.number_input("Lado B")
    c = st.number_input("Lado C")
    if st.button("Verificar"):
        if a+b>c and a+c>b and b+c>a:
            st.success("Forma triângulo")
        else:
            st.error("Não forma triângulo")

def desafio_9():
    n = st.number_input("Número N", step=1)
    if st.button("Somar"):
        st.success(sum(range(1, int(n)+1)))

def desafio_10():
    n = st.number_input("Número", step=1)
    if st.button("Fatorial"):
        st.success(math.factorial(int(n)))

def desafio_11():
    n = st.number_input("Número", step=1)
    if st.button("Tabuada"):
        for i in range(1,11):
            st.write(f"{n} x {i} = {n*i}")

def desafio_12():
    if st.button("Contar pares 1-100"):
        pares = [i for i in range(1,101) if i%2==0]
        st.success(len(pares))

def desafio_13():
    nums = st.text_input("Digite 10 números separados por vírgula")
    if st.button("Mostrar vetor"):
        vetor = list(map(int, nums.split(",")))
        st.write(vetor)

def desafio_14():
    nums = st.text_input("Digite números separados por vírgula")
    if st.button("Somar vetor"):
        vetor = list(map(int, nums.split(",")))
        st.success(sum(vetor))

def desafio_15():
    nums = st.text_input("Digite números separados por vírgula")
    busca = st.number_input("Valor buscado")
    if st.button("Buscar"):
        vetor = list(map(int, nums.split(",")))
        st.success("Encontrado" if busca in vetor else "Não encontrado")

def desafio_16():
    nums = st.text_input("Digite números separados por vírgula")
    busca = st.number_input("Valor")
    if st.button("Contar"):
        vetor = list(map(int, nums.split(",")))
        st.success(vetor.count(busca))

def desafio_17():
    nums = st.text_input("Digite 30 valores")
    if st.button("Média"):
        vetor = list(map(float, nums.split(",")))
        st.success(sum(vetor)/len(vetor))

def desafio_18():
    nums = st.text_input("Preços separados por vírgula")
    if st.button("Filtrar > 50"):
        vetor = list(map(float, nums.split(",")))
        st.success(len([x for x in vetor if x > 50]))

def desafio_19():
    nums = st.text_input("Valores separados por vírgula")
    if st.button("Acima da média"):
        vetor = list(map(float, nums.split(",")))
        media = sum(vetor)/len(vetor)
        st.success(len([x for x in vetor if x > media]))

def desafio_20():
    nums = st.text_input("Preços separados por vírgula")
    if st.button("Somar pares"):
        vetor = list(map(int, nums.split(",")))
        st.success(sum([x for x in vetor if x % 2 == 0]))

# ==============================
# ENUNCIADOS COMPLETOS
# ==============================
desafios = {
    "Desafio 1": {"desc": """Imagine que estamos ajudando um estudante chamado Pedro... calcular a média das três provas.""", "func": desafio_1},
    "Desafio 2": {"desc": """Maria quer converter temperatura de Celsius para Fahrenheit.""", "func": desafio_2},
    "Desafio 3": {"desc": """João quer calcular a área de um círculo.""", "func": desafio_3},
    "Desafio 4": {"desc": """Ana quer calcular seu salário bruto baseado em horas trabalhadas.""", "func": desafio_4},
    "Desafio 5": {"desc": """Verificar se Joaquim pode votar (18 anos).""", "func": desafio_5},
    "Desafio 6": {"desc": """Classificar nota de acordo com conceitos A-E.""", "func": desafio_6},
    "Desafio 7": {"desc": """Encontrar o maior entre três valores.""", "func": desafio_7},
    "Desafio 8": {"desc": """Verificar se três lados formam triângulo.""", "func": desafio_8},
    "Desafio 9": {"desc": """Somar números de 1 até N.""", "func": desafio_9},
    "Desafio 10": {"desc": """Calcular fatorial.""", "func": desafio_10},
    "Desafio 11": {"desc": """Gerar tabuada.""", "func": desafio_11},
    "Desafio 12": {"desc": """Contar pares de 1 a 100.""", "func": desafio_12},
    "Desafio 13": {"desc": """Preencher vetor com 10 números.""", "func": desafio_13},
    "Desafio 14": {"desc": """Somar vetor.""", "func": desafio_14},
    "Desafio 15": {"desc": """Buscar valor no vetor.""", "func": desafio_15},
    "Desafio 16": {"desc": """Contar ocorrências no vetor.""", "func": desafio_16},
    "Desafio 17": {"desc": """Calcular média de valores.""", "func": desafio_17},
    "Desafio 18": {"desc": """Filtrar valores maiores que 50.""", "func": desafio_18},
    "Desafio 19": {"desc": """Valores acima da média.""", "func": desafio_19},
    "Desafio 20": {"desc": """Somar valores pares.""", "func": desafio_20},
}

# ==============================
# SIDEBAR
# ==============================
st.sidebar.header("📌 Navegação")
desafio = st.sidebar.selectbox("Escolha o desafio", list(desafios.keys()))

# ==============================
# EXIBIÇÃO
# ==============================
st.header(f"📍 {desafio}")

st.markdown("### 📝 Enunciado")
st.info(desafios[desafio]["desc"])

st.markdown("### 💻 Resolução")
desafios[desafio]["func"]()

# ==============================
# PRESENÇA
# ==============================
st.markdown("---")
st.header("📋 Registro de Presença")

if "lista" not in st.session_state:
    st.session_state.lista = []

with st.form("form"):
    nome = st.text_input("Nome")
    if st.form_submit_button("Registrar"):
        if nome:
            st.session_state.lista.append(nome)
            st.toast("Registrado!")

if st.session_state.lista:
    for i, n in enumerate(st.session_state.lista,1):
        st.write(f"{i}. {n}")

    st.download_button("Baixar", "\n".join(st.session_state.lista))
