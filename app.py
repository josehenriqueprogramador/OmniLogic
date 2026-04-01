import streamlit as st
import math

# Configuração da página
st.set_page_config(page_title="OmniLogic v6.0", layout="centered")

st.title("🧪 OmniLogic v6.0")
st.subheader("Sistema de Desafios - Ciência de Dados")

# ==============================
# FUNÇÃO AUXILIAR PARA VETORES
# ==============================
def parse_lista(texto):
    try:
        # Aceita números separados por vírgula ou espaço
        separador = "," if "," in texto else " "
        return [float(x.strip()) for x in texto.split(separador) if x.strip()]
    except:
        return None

# ==============================
# DEFINIÇÃO DAS FUNÇÕES DE RESOLUÇÃO
# ==============================

def res_d1():
    n1 = st.number_input("Nota de Matemática", key="d1_n1", min_value=0.0, max_value=10.0)
    n2 = st.number_input("Nota de Português", key="d1_n2", min_value=0.0, max_value=10.0)
    n3 = st.number_input("Nota de Ciências", key="d1_n3", min_value=0.0, max_value=10.0)
    if st.button("Calcular Média Final"):
        media = (n1 + n2 + n3) / 3
        st.success(f"A média final do Pedro é: {media:.2f}")

def res_d2():
    c = st.number_input("Temperatura em Celsius (°C)", key="d2")
    if st.button("Converter para Fahrenheit"):
        f = (c * 9/5) + 32
        st.success(f"{c}°C equivalem a {f:.2f}°F")

def res_d3():
    r = st.number_input("Medida do Raio", key="d3", min_value=0.0)
    if st.button("Calcular Área"):
        area = math.pi * r**2
        st.success(f"A área do círculo no quintal do João é: {area:.2f}")

def res_d4():
    h = st.number_input("Horas Trabalhadas", key="d4_h", min_value=0.0)
    v = st.number_input("Valor da Taxa Horária (R$)", key="d4_v", min_value=0.0)
    if st.button("Calcular Salário Bruto"):
        st.success(f"O salário bruto da Ana é: R$ {h*v:.2f}")

def res_d5():
    idade = st.number_input("Digite a idade do Joaquim", key="d5", step=1)
    if st.button("Verificar Elegibilidade"):
        if idade >= 18:
            st.success("Joaquim tem idade suficiente para votar! ✅")
        else:
            st.warning("Joaquim ainda não tem idade mínima para votar. ❌")

def res_d6():
    nota = st.number_input("Nota da Maria", key="d6", min_value=0.0, max_value=10.0)
    if st.button("Verificar Conceito"):
        if nota >= 9: c, cor = "A", "success"
        elif nota >= 7: c, cor = "B", "info"
        elif nota >= 5: c, cor = "C", "warning"
        elif nota >= 3: c, cor = "D", "error"
        else: c, cor = "E", "error"
        st.write(f"Conceito Final: **{c}**")

def res_d7():
    v1 = st.number_input("Medição 1", key="d7_1")
    v2 = st.number_input("Medição 2", key="d7_2")
    v3 = st.number_input("Medição 3", key="d7_3")
    if st.button("Encontrar Maior Valor"):
        st.success(f"O maior valor coletado pelo Carlos é: {max(v1, v2, v3)}")

def res_d8():
    a = st.number_input("Segmento A", key="d8_a")
    b = st.number_input("Segmento B", key="d8_b")
    c = st.number_input("Segmento C", key="d8_c")
    if st.button("Validar Triângulo"):
        if a+b>c and a+c>b and b+c>a:
            st.success("Os segmentos formam um triângulo válido! 🔺")
        else:
            st.error("Os segmentos não podem formar um triângulo. ❌")

def res_d9():
    n = st.number_input("Valor de N", key="d9", step=1, min_value=1)
    if st.button("Calcular Soma Natural"):
        soma = sum(range(1, int(n)+1))
        st.success(f"A soma dos primeiros {n} números é: {soma}")

def res_d10():
    n = st.number_input("Número para Fatorial", key="d10", step=1, min_value=0)
    if st.button("Calcular Fatorial"):
        st.success(f"O fatorial de {n} é: {math.factorial(int(n))}")

def res_d11():
    n = st.number_input("Tabuada do número:", key="d11", step=1)
    if st.button("Gerar Tabuada"):
        for i in range(1, 11):
            st.write(f"{n} x {i} = {n*i}")

def res_d12():
    if st.button("Contar Pares (1 a 100)"):
        pares = [i for i in range(1, 101) if i % 2 == 0]
        st.success(f"Existem {len(pares)} números pares entre 1 e 100.")

def res_d13():
    texto = st.text_input("André, digite os 10 números (separados por vírgula)", key="d13")
    if st.button("Imprimir Vetor"):
        vetor = parse_lista(texto)
        if vetor: st.write("Vetor preenchido:", vetor)
        else: st.error("Por favor, digite números válidos.")

def res_d14():
    texto = st.text_input("Júlio, insira os dados do vetor", key="d14")
    if st.button("Somar Elementos"):
        vetor = parse_lista(texto)
        if vetor: st.success(f"A soma total é: {sum(vetor)}")

def res_d15():
    texto = st.text_input("Vetor de Temperaturas", key="d15")
    busca = st.number_input("Temperatura a buscar", key="d15_b")
    if st.button("Buscar"):
        vetor = parse_lista(texto)
        if vetor and busca in vetor: st.success("Temperatura encontrada no vetor! ✅")
        else: st.warning("Temperatura não encontrada. ❌")

def res_d16():
    texto = st.text_input("Dados de Concentração", key="d16")
    valor = st.number_input("Valor a contar", key="d16_v")
    if st.button("Contar Ocorrências"):
        vetor = parse_lista(texto)
        if vetor: st.success(f"O valor {valor} aparece {vetor.count(valor)} vezes.")

def res_d17():
    texto = st.text_area("Insira as 30 distâncias (separadas por vírgula ou espaço)", key="d17")
    if st.button("Calcular Média de Lançamentos"):
        vetor = parse_lista(texto)
        if vetor: st.success(f"A distância média alcançada foi: {sum(vetor)/len(vetor):.2f}")

def res_d18():
    texto = st.text_input("Preços das 10 camisetas", key="d18")
    if st.button("Filtrar Preços > R$ 50"):
        vetor = parse_lista(texto)
        if vetor:
            caras = [x for x in vetor if x > 50]
            st.success(f"{len(caras)} camisetas custam mais de R$ 50,00.")

def res_d19():
    texto = st.text_input("Livros lidos por cada membro", key="d19")
    if st.button("Analisar Clube de Leitura"):
        vetor = parse_lista(texto)
        if vetor:
            media = sum(vetor)/len(vetor)
            acima = [x for x in vetor if x > media]
            st.info(f"Média do grupo: {media:.2f} livros. {len(acima)} membros leram acima da média.")

def res_d20():
    texto = st.text_input("Preços dos 5 tipos de pães", key="d20")
    if st.button("Somar Preços Pares"):
        vetor = parse_lista(texto)
        if vetor:
            soma_par = sum([x for x in vetor if x % 2 == 0])
            st.success(f"O total arrecadado com pães de valor par é: R$ {soma_par:.2f}")

# ==============================
# DICIONÁRIO DE DADOS (ENUNCIADOS ORIGINAIS)
# ==============================
desafios_db = {
    "Desafio 1": {"desc": "Imagine que estamos ajudando um estudante chamado Pedro. Ele está cursando o ensino médio e precisa calcular a média das notas de três provas: Matemática, Português e Ciências. Pedro anotou suas notas em um pedaço de papel e agora quer saber qual é a média final. Vamos ajudá-lo a fazer esse cálculo!", "func": res_d1},
    "Desafio 2": {"desc": "Conheçamos a Maria, uma viajante entusiasta. Ela está planejando uma viagem para os Estados Unidos e quer ter uma ideia das temperaturas locais. Maria está acostumada com Celsius, mas nos EUA, eles usam Fahrenheit. Ela anotou a temperatura de um dia em sua cidade natal e quer converter para Fahrenheit. Vamos ajudar a Maria a fazer essa conversão!", "func": res_d2},
    "Desafio 3": {"desc": "Agora, vamos conhecer o João, um estudante de geometria. Ele está aprendendo sobre círculos e quer calcular a área de um círculo com um raio específico. João tem uma fita métrica e mediu o raio de um círculo em seu quintal. Qual seria a área desse círculo?", "func": res_d3},
    "Desafio 4": {"desc": "Por fim, temos a Ana, uma funcionária dedicada. Ela trabalha como atendente em uma lanchonete e anota suas horas trabalhadas todos os dias. Ana quer saber quanto receberá no final do mês com base nas horas que trabalhou e na taxa horária. Vamos ajudar a Ana a calcular seu salário bruto!", "func": res_d4},
    "Desafio 5": {"desc": "Imagine que estamos em um escritório de registro eleitoral. O cidadão Joaquim acaba de chegar para se registrar como eleitor. Ele nos informou sua data de nascimento e queremos verificar se ele tem idade suficiente para votar nas próximas eleições. Nosso critério é que a idade mínima para votar é 18 anos. Vamos realizar essa verificação!", "func": res_d5},
    "Desafio 6": {"desc": "Agora, conheçamos a aluna Maria. Ela está estuda em uma escola e acabou de receber sua nota em uma prova de Matemática. Queremos classificar essa nota com base em um sistema de conceitos (A, B, C, D ou E).", "func": res_d6},
    "Desafio 7": {"desc": "Vamos imaginar que estamos em um laboratório de pesquisa científica. O pesquisador Carlos coletou três valores de medição em um experimento. Agora, precisamos determinar qual desses valores é o maior.", "func": res_d7},
    "Desafio 8": {"desc": "Encontramo-nos em uma sala de geometria, onde o professor Silva está conduzindo uma aula sobre triângulos. Três alunos trouxeram comprimentos de segmentos e querem saber se esses segmentos podem formar um triângulo válido.", "func": res_d8},
    "Desafio 9": {"desc": "Imagine que estamos auxiliando o estudante Lucas em sua aula de matemática. O professor pediu a ele para calcular a soma dos primeiros N números naturais.", "func": res_d9},
    "Desafio 10": {"desc": "Agora, conheçamos a Maria, uma estudante de ciências exatas. Ela está estudando matemática avançada e se deparou com o conceito de fatorial.", "func": res_d10},
    "Desafio 11": {"desc": "Nosso próximo contexto envolve o aluno Pedro, que está no ensino fundamental. Ele está aprendendo sobre multiplicação e quer praticar a tabuada.", "func": res_d11},
    "Desafio 12": {"desc": "Suponha que estamos em uma sala de aula de programação. O professor Carlos desafiou seus alunos a escreverem um programa que conte quantos números pares existem entre 1 e 100.", "func": res_d12},
    "Desafio 13": {"desc": "Imagine que estamos auxiliando o estudante André em sua aula de programação. O professor pediu a ele para criar um vetor com 10 números inteiros.", "func": res_d13},
    "Desafio 14": {"desc": "Agora, conheçamos o programador Júlio. Ele está trabalhando em um projeto que envolve análise de dados. Júlio coletou informações em um vetor e precisa da soma total.", "func": res_d14},
    "Desafio 15": {"desc": "Maria, uma pesquisadora de dados, quer verificar se uma temperatura específica está presente em seu vetor de medições.", "func": res_d15},
    "Desafio 16": {"desc": "O técnico Pedro quer saber quantas vezes uma concentração específica aparece nos dados coletados em seu laboratório.", "func": res_d16},
    "Desafio 17": {"desc": "Competição de dardos: Temos 10 participantes com 3 lançamentos cada. Queremos calcular a média das 30 distâncias alcançadas.", "func": res_d17},
    "Desafio 18": {"desc": "Loja de roupas: O cliente quer ver apenas as camisetas que custam mais de R$ 50,00 entre as 10 disponíveis.", "func": res_d18},
    "Desafio 19": {"desc": "Clube de leitura: Queremos saber quantos membros leram mais livros do que a média geral do grupo.", "func": res_d19},
    "Desafio 20": {"desc": "Padaria: Queremos calcular o total arrecadado apenas com os pães que possuem preço de valor par.", "func": res_d20},
}

# ==============================
# INTERFACE PRINCIPAL
# ==============================
escolha = st.sidebar.selectbox("Selecione o Desafio", list(desafios_db.keys()))

st.markdown(f"## 📍 {escolha}")
st.info(desafios_db[escolha]["desc"])

st.markdown("### 💻 Execução do Desafio")
desafios_db[escolha]["func"]()
