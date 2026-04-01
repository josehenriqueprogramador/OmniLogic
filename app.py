import streamlit as st
import math
import random

# ==============================
# CONFIG
# ==============================
st.set_page_config(
    page_title="OmniLogic v5.0",
    layout="centered",
    page_icon="🧪"
)

st.title("🧪 OmniLogic v5.0")
st.subheader("Sistema de Desafios - Ciência de Dados")

# ==============================
# FUNÇÕES DOS DESAFIOS
# ==============================

def desafio_1():
    n1 = st.number_input("Nota 1", 0.0, 10.0)
    n2 = st.number_input("Nota 2", 0.0, 10.0)
    if st.button("Calcular Média"):
        st.success(f"Média: {(n1+n2)/2:.2f}")

def desafio_2():
    n = st.number_input("Número", step=1)
    if st.button("Verificar"):
        st.success("PAR" if n % 2 == 0 else "ÍMPAR")

def desafio_3():
    c = st.number_input("Celsius")
    if st.button("Converter"):
        st.success(f"{(c*9/5)+32:.2f} °F")

def desafio_4():
    r = st.number_input("Raio", min_value=0.0)
    if st.button("Calcular Área"):
        st.success(f"Área: {math.pi*r**2:.2f}")

def desafio_5():
    ano = st.number_input("Ano", step=1)
    if st.button("Verificar"):
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            st.success("Ano bissexto")
        else:
            st.error("Não é bissexto")

def desafio_6():
    if st.button("Gerar Fibonacci"):
        seq = [0, 1]
        for _ in range(8):
            seq.append(seq[-1] + seq[-2])
        st.write(seq)

def desafio_7():
    n = st.number_input("Número", min_value=0, step=1)
    if st.button("Calcular Fatorial"):
        st.success(f"Fatorial: {math.factorial(int(n))}")

def desafio_8():
    n = st.number_input("Número", step=1)
    if st.button("Verificar Primo"):
        primo = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))
        st.success("Primo" if primo else "Não é primo")

def desafio_9():
    m = st.number_input("Metros")
    if st.button("Converter"):
        st.success(f"{m*100} cm | {m*1000} mm")

def desafio_10():
    n = st.number_input("Número", step=1)
    if st.button("Gerar Tabuada"):
        for i in range(1, 11):
            st.write(f"{n} x {i} = {n*i}")

def desafio_11():
    peso = st.number_input("Peso (kg)")
    altura = st.number_input("Altura (m)")
    if st.button("Calcular IMC"):
        if altura > 0:
            imc = peso / (altura**2)
            st.success(f"IMC: {imc:.2f}")
        else:
            st.error("Altura deve ser maior que zero")

def desafio_12():
    a = st.number_input("Lado A")
    b = st.number_input("Lado B")
    c = st.number_input("Lado C")
    if st.button("Verificar Triângulo"):
        if a == b == c:
            st.success("Equilátero")
        elif a == b or b == c or a == c:
            st.warning("Isósceles")
        else:
            st.info("Escaleno")

def desafio_13():
    a = st.number_input("Cateto A")
    b = st.number_input("Cateto B")
    if st.button("Calcular Hipotenusa"):
        st.success(f"Hipotenusa: {math.sqrt(a**2 + b**2):.2f}")

def desafio_14():
    if st.button("Lançar Dado"):
        st.success(f"Resultado: {random.randint(1,6)}")

def desafio_15():
    texto = st.text_input("Digite uma frase")
    if st.button("Contar Vogais"):
        vogais = sum(1 for c in texto.lower() if c in "aeiou")
        st.success(f"Vogais: {vogais}")

def desafio_16():
    texto = st.text_input("Digite uma palavra")
    if st.button("Inverter"):
        st.success(texto[::-1])

def desafio_17():
    capital = st.number_input("Capital")
    taxa = st.number_input("Taxa (%)")
    tempo = st.number_input("Tempo")
    if st.button("Calcular Juros"):
        juros = capital * (taxa/100) * tempo
        st.success(f"Juros: {juros:.2f}")

def desafio_18():
    palavra = st.text_input("Digite uma palavra")
    if st.button("Verificar Palíndromo"):
        p = palavra.lower()
        st.success("Palíndromo" if p == p[::-1] else "Não é palíndromo")

def desafio_19():
    n = st.number_input("Número", step=1)
    if st.button("Calcular Soma"):
        st.success(f"Soma: {sum(range(1, int(n)+1))}")

def desafio_20():
    a = st.number_input("A")
    b = st.number_input("B")
    c = st.number_input("C")
    if st.button("Resolver Bhaskara"):
        if a == 0:
            st.error("A não pode ser zero")
        else:
            delta = b**2 - 4*a*c
            if delta < 0:
                st.error("Sem raízes reais")
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                st.success(f"x1 = {x1:.2f}, x2 = {x2:.2f}")

# ==============================
# DESAFIOS + ENUNCIADOS
# ==============================
desafios = {
    "Desafio 1": {"descricao": "Calcule a média aritmética de duas notas.", "func": desafio_1},
    "Desafio 2": {"descricao": "Verifique se um número é par ou ímpar.", "func": desafio_2},
    "Desafio 3": {"descricao": "Converta Celsius para Fahrenheit.", "func": desafio_3},
    "Desafio 4": {"descricao": "Calcule a área de um círculo.", "func": desafio_4},
    "Desafio 5": {"descricao": "Verifique se um ano é bissexto.", "func": desafio_5},
    "Desafio 6": {"descricao": "Exiba os 10 primeiros números de Fibonacci.", "func": desafio_6},
    "Desafio 7": {"descricao": "Calcule o fatorial de um número.", "func": desafio_7},
    "Desafio 8": {"descricao": "Verifique se um número é primo.", "func": desafio_8},
    "Desafio 9": {"descricao": "Converta metros para cm e mm.", "func": desafio_9},
    "Desafio 10": {"descricao": "Exiba a tabuada de um número.", "func": desafio_10},
    "Desafio 11": {"descricao": "Calcule o IMC.", "func": desafio_11},
    "Desafio 12": {"descricao": "Classifique um triângulo.", "func": desafio_12},
    "Desafio 13": {"descricao": "Calcule a hipotenusa.", "func": desafio_13},
    "Desafio 14": {"descricao": "Simule um dado.", "func": desafio_14},
    "Desafio 15": {"descricao": "Conte vogais em uma frase.", "func": desafio_15},
    "Desafio 16": {"descricao": "Inverta uma string.", "func": desafio_16},
    "Desafio 17": {"descricao": "Calcule juros simples.", "func": desafio_17},
    "Desafio 18": {"descricao": "Verifique palíndromo.", "func": desafio_18},
    "Desafio 19": {"descricao": "Some de 1 até N.", "func": desafio_19},
    "Desafio 20": {"descricao": "Resolva Bhaskara.", "func": desafio_20},
}

# ==============================
# SIDEBAR
# ==============================
st.sidebar.header("📌 Navegação")
desafio = st.sidebar.selectbox("Escolha o desafio:", list(desafios.keys()))

# ==============================
# EXIBIÇÃO
# ==============================
st.header(f"📍 {desafio}")
st.markdown("### 📝 Enunciado")
st.info(desafios[desafio]["descricao"])

st.markdown("### 💻 Resolução")
desafios[desafio]["func"]()

# ==============================
# PRESENÇA
# ==============================
st.markdown("---")
st.header("📋 Registro de Presença")

if "lista" not in st.session_state:
    st.session_state.lista = []

with st.form("form_presenca", clear_on_submit=True):
    nome = st.text_input("Nome do aluno")
    btn = st.form_submit_button("Registrar")

    if btn:
        if nome.strip():
            st.session_state.lista.append(nome.strip())
            st.toast(f"{nome} registrado!")
        else:
            st.error("Nome inválido")

if st.session_state.lista:
    st.write("### Lista Atual")
    for i, aluno in enumerate(st.session_state.lista, 1):
        st.write(f"{i}. ✅ {aluno}")

    st.download_button(
        "📥 Baixar lista",
        "\n".join(st.session_state.lista),
        "lista_presenca.txt"
    )
