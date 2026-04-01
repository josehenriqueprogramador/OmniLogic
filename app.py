import streamlit as st
import math
import random

st.set_page_config(page_title="OmniLogic v5.1", layout="centered")

st.title("🧪 OmniLogic v5.1")

# ==============================
# FUNÇÃO AUXILIAR (SEGURANÇA)
# ==============================
def parse_lista(texto):
    try:
        return [float(x.strip()) for x in texto.split(",") if x.strip()]
    except:
        return None

# ==============================
# DESAFIOS
# ==============================

def desafio_1():
    with st.form("d1"):
        n1 = st.number_input("Matemática")
        n2 = st.number_input("Português")
        n3 = st.number_input("Ciências")
        ok = st.form_submit_button("Calcular")
        if ok:
            st.success(f"Média: {(n1+n2+n3)/3:.2f}")

def desafio_2():
    with st.form("d2"):
        c = st.number_input("Celsius")
        ok = st.form_submit_button("Converter")
        if ok:
            st.success(f"{(c*9/5)+32:.2f} °F")

def desafio_3():
    with st.form("d3"):
        r = st.number_input("Raio")
        ok = st.form_submit_button("Calcular")
        if ok:
            st.success(f"{math.pi*r**2:.2f}")

def desafio_4():
    with st.form("d4"):
        h = st.number_input("Horas")
        v = st.number_input("Valor/hora")
        ok = st.form_submit_button("Calcular")
        if ok:
            st.success(f"R$ {h*v:.2f}")

def desafio_5():
    with st.form("d5"):
        idade = st.number_input("Idade")
        ok = st.form_submit_button("Verificar")
        if ok:
            st.success("Pode votar" if idade >= 18 else "Não pode votar")

def desafio_6():
    with st.form("d6"):
        nota = st.number_input("Nota")
        ok = st.form_submit_button("Classificar")
        if ok:
            if nota >= 9: c="A"
            elif nota >= 7: c="B"
            elif nota >= 5: c="C"
            elif nota >= 3: c="D"
            else: c="E"
            st.success(f"Conceito: {c}")

def desafio_7():
    with st.form("d7"):
        a = st.number_input("A")
        b = st.number_input("B")
        c = st.number_input("C")
        ok = st.form_submit_button("Maior")
        if ok:
            st.success(max(a,b,c))

def desafio_8():
    with st.form("d8"):
        a = st.number_input("A")
        b = st.number_input("B")
        c = st.number_input("C")
        ok = st.form_submit_button("Verificar")
        if ok:
            if a+b>c and a+c>b and b+c>a:
                st.success("Forma triângulo")
            else:
                st.error("Não forma")

def desafio_9():
    with st.form("d9"):
        n = st.number_input("N", step=1)
        ok = st.form_submit_button("Somar")
        if ok:
            st.success(sum(range(1,int(n)+1)))

def desafio_10():
    with st.form("d10"):
        n = st.number_input("Número", step=1)
        ok = st.form_submit_button("Fatorial")
        if ok:
            st.success(math.factorial(int(n)))

def desafio_11():
    with st.form("d11"):
        n = st.number_input("Número", step=1)
        ok = st.form_submit_button("Tabuada")
        if ok:
            for i in range(1,11):
                st.write(f"{n} x {i} = {n*i}")

def desafio_12():
    if st.button("Contar pares", key="d12"):
        st.success(len([i for i in range(1,101) if i%2==0]))

def desafio_13():
    nums = st.text_input("10 números (vírgula)", key="d13")
    if st.button("Mostrar", key="btn13"):
        vetor = parse_lista(nums)
        if vetor:
            st.write(vetor)
        else:
            st.error("Entrada inválida")

def desafio_14():
    nums = st.text_input("Números", key="d14")
    if st.button("Somar", key="btn14"):
        vetor = parse_lista(nums)
        if vetor:
            st.success(sum(vetor))

def desafio_15():
    nums = st.text_input("Números", key="d15")
    busca = st.number_input("Buscar", key="busca15")
    if st.button("Buscar", key="btn15"):
        vetor = parse_lista(nums)
        if vetor:
            st.success("Encontrado" if busca in vetor else "Não encontrado")

def desafio_16():
    nums = st.text_input("Números", key="d16")
    busca = st.number_input("Valor", key="busca16")
    if st.button("Contar", key="btn16"):
        vetor = parse_lista(nums)
        if vetor:
            st.success(vetor.count(busca))

def desafio_17():
    nums = st.text_input("Valores", key="d17")
    if st.button("Média", key="btn17"):
        vetor = parse_lista(nums)
        if vetor:
            st.success(sum(vetor)/len(vetor))

def desafio_18():
    nums = st.text_input("Preços", key="d18")
    if st.button("Filtrar", key="btn18"):
        vetor = parse_lista(nums)
        if vetor:
            st.success(len([x for x in vetor if x > 50]))

def desafio_19():
    nums = st.text_input("Valores", key="d19")
    if st.button("Acima média", key="btn19"):
        vetor = parse_lista(nums)
        if vetor:
            media = sum(vetor)/len(vetor)
            st.success(len([x for x in vetor if x > media]))

def desafio_20():
    nums = st.text_input("Preços", key="d20")
    if st.button("Somar pares", key="btn20"):
        vetor = parse_lista(nums)
        if vetor:
            st.success(sum([int(x) for x in vetor if int(x)%2==0]))

# ==============================
# DICIONÁRIO
# ==============================
desafios = {
    "Desafio 1": {"desc": "Cálculo da média de Pedro", "func": desafio_1},
    "Desafio 2": {"desc": "Conversão de temperatura", "func": desafio_2},
    "Desafio 3": {"desc": "Área do círculo", "func": desafio_3},
    "Desafio 4": {"desc": "Salário da Ana", "func": desafio_4},
    "Desafio 5": {"desc": "Verificação de idade", "func": desafio_5},
    "Desafio 6": {"desc": "Classificação de notas", "func": desafio_6},
    "Desafio 7": {"desc": "Maior número", "func": desafio_7},
    "Desafio 8": {"desc": "Triângulo", "func": desafio_8},
    "Desafio 9": {"desc": "Soma até N", "func": desafio_9},
    "Desafio 10": {"desc": "Fatorial", "func": desafio_10},
    "Desafio 11": {"desc": "Tabuada", "func": desafio_11},
    "Desafio 12": {"desc": "Contar pares", "func": desafio_12},
    "Desafio 13": {"desc": "Vetor", "func": desafio_13},
    "Desafio 14": {"desc": "Soma vetor", "func": desafio_14},
    "Desafio 15": {"desc": "Busca", "func": desafio_15},
    "Desafio 16": {"desc": "Contagem", "func": desafio_16},
    "Desafio 17": {"desc": "Média vetor", "func": desafio_17},
    "Desafio 18": {"desc": "Filtragem", "func": desafio_18},
    "Desafio 19": {"desc": "Acima média", "func": desafio_19},
    "Desafio 20": {"desc": "Soma pares", "func": desafio_20},
}

# ==============================
# UI
# ==============================
desafio = st.sidebar.selectbox("Escolha", list(desafios.keys()))

st.header(desafio)
st.info(desafios[desafio]["desc"])

desafios[desafio]["func"]()
