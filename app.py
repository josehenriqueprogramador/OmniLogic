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
    if st.button("Calcular"):
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
    if st.button("Calcular"):
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
    n = st.number_input("Número", step=1, min_value=0)
    if st.button("Calcular"):
        st.success(f"Fatorial: {math.factorial(int(n))}")

def desafio_8():
    n = st.number_input("Número", step=1)
    if st.button("Verificar"):
        primo = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))
        st.success("Primo" if primo else "Não primo")

def desafio_9():
    m = st.number_input("Metros")
    if st.button("Converter"):
        st.write(f"{m*100} cm | {m*1000} mm")

def desafio_10():
    n = st.number_input("Número", step=1)
    if st.button("Tabuada"):
        for i in range(1, 11):
            st.write(f"{n} x {i} = {n*i}")

def desafio_11():
    peso = st.number_input("Peso (kg)")
    altura = st.number_input("Altura (m)")
    if st.button("Calcular IMC"):
        imc = peso / (altura**2)
        st.success(f"IMC: {imc:.2f}")

def desafio_12():
    a = st.number_input("Lado A")
    b = st.number_input("Lado B")
    c = st.number_input("Lado C")
    if st.button("Verificar"):
        if a == b == c:
            st.success("Equilátero")
        elif a == b or b == c or a == c:
            st.warning("Isósceles")
        else:
            st.info("Escaleno")

def desafio_13():
    a = st.number_input("Cateto A")
    b = st.number_input("Cateto B")
    if st.button("Calcular"):
        st.success(f"Hipotenusa: {math.sqrt(a**2+b**2):.2f}")

def desafio_14():
    if st.button("Lançar dado"):
        st.success(f"Resultado: {random.randint(1,6)}")

def desafio_15():
    texto = st.text_input("Digite uma frase")
    if st.button("Contar"):
        vogais = sum(1 for c in texto.lower() if c in "aeiou")
        st.success(f"Vogais: {vogais}")

def desafio_16():
    texto = st.text_input("Digite uma palavra")
    if st.button("Inverter"):
        st.success(texto[::-1])

def desafio_17():
    c = st.number_input("Capital")
    t = st.number_input("Taxa (%)")
    tempo = st.number_input("Tempo")
    if st.button("Calcular"):
        j = c * (t/100) * tempo
        st.success(f"Juros: {j:.2f}")

def desafio_18():
    palavra = st.text_input("Palavra")
    if st.button("Verificar"):
        p = palavra.lower()
        st.success("Palíndromo" if p == p[::-1] else "Não é")

def desafio_19():
    n = st.number_input("Número", step=1)
    if st.button("Somar"):
        st.success(f"Soma: {sum(range(1, int(n)+1))}")

def desafio_20():
    a = st.number_input("A")
    b = st.number_input("B")
    c = st.number_input("C")
    if st.button("Resolver"):
        delta = b**2 - 4*a*c
        if delta < 0:
            st.error("Sem raízes reais")
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            st.success(f"x1={x1:.2f}, x2={x2:.2f}")

# ==============================
# DICIONÁRIO DINÂMICO
# ==============================
desafios = {
    f"Desafio {i}": {
        "descricao": f"Executando desafio {i}",
        "func": globals()[f"desafio_{i}"]
    }
    for i in range(1, 21)
}

# ==============================
# SIDEBAR
# ==============================
st.sidebar.header("Navegação")
desafio = st.sidebar.selectbox("Escolha:", list(desafios.keys()))

# ==============================
# EXECUÇÃO
# ==============================
st.header(desafio)
desafios[desafio]["func"]()

# ==============================
# PRESENÇA
# ==============================
st.markdown("---")
st.header("📋 Registro de Presença")

if "lista" not in st.session_state:
    st.session_state.lista = []

with st.form("form", clear_on_submit=True):
    nome = st.text_input("Nome")
    ok = st.form_submit_button("Registrar")

    if ok:
        if nome.strip():
            st.session_state.lista.append(nome)
            st.toast("Registrado!")
        else:
            st.error("Nome inválido")

if st.session_state.lista:
    for i, n in enumerate(st.session_state.lista, 1):
        st.write(f"{i}. {n}")

    st.download_button(
        "Baixar lista",
        "\n".join(st.session_state.lista),
        "presenca.txt"
    )
