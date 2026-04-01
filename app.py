import streamlit as st
import math

# Configuração visual da página
st.set_page_config(page_title="OmniLogic v5.0 - Unigranrio", layout="centered")

# Cabeçalho do Trabalho Acadêmico
st.title("🚀 OmniLogic v5.0")
st.subheader("Sistema de Desafios - Algoritmos e Programação")
st.markdown(f"**Acadêmico:** José Henrique Jardim | **Professor:** Oswaldo Peres")
st.markdown("---")

# Menu Lateral para Navegação
opcao = st.sidebar.selectbox(
    "Selecione o Desafio:",
    [f"Desafio {i}" for i in range(1, 21)]
)

# Dicionário com todos os Enunciados
enunciados = {
    "Desafio 1": "Calcular a média aritmética simples entre duas notas bimestrais.",
    "Desafio 2": "Converter uma temperatura de graus Celsius para Fahrenheit.",
    "Desafio 3": "Calcular a área de um círculo (π * r²).",
    "Desafio 4": "Calcular o salário total baseado no valor da hora e horas trabalhadas.",
    "Desafio 5": "Verificar se uma pessoa já possui idade mínima para votar (16 anos).",
    "Desafio 6": "Calcular o novo salário de um funcionário com 15% de aumento.",
    "Desafio 7": "Identificar qual é o maior valor entre dois números digitados.",
    "Desafio 8": "Verificar se um valor é Positivo, Negativo ou Neutro (Zero).",
    "Desafio 9": "Calcular o IMC (Peso / Altura²) e exibir o índice.",
    "Desafio 10": "Verificar se um número inteiro é Par ou Ímpar.",
    "Desafio 11": "Gerar a tabuada completa (1 a 10) de um número escolhido.",
    "Desafio 12": "Calcular o Fatorial de um número (ex: 5! = 120).",
    "Desafio 13": "Calcular a média ponderada de 3 notas (Pesos: 2, 3 e 5).",
    "Desafio 14": "Somar todos os elementos de um vetor de 5 números.",
    "Desafio 15": "Conversor de Moeda: Transformar Reais em Dólares (Cotação fixa: 5.00).",
    "Desafio 16": "Calcular a área de um triângulo retângulo (Base * Altura / 2).",
    "Desafio 17": "Calcular o valor final de uma compra com 10% de desconto à vista.",
    "Desafio 18": "Verificar se três medidas podem formar um triângulo (Condição de existência).",
    "Desafio 19": "Calcular a potência: elevar uma base X a um expoente Y.",
    "Desafio 20": "Cálculo de Juros Simples sobre um capital inicial."
}

# Exibição do Enunciado Selecionado
st.info(f"**ENUNCIADO:** {enunciados[opcao]}")

# --- LÓGICA DE CADA DESAFIO ---

if opcao == "Desafio 1":
    n1 = st.number_input("Nota 1:", 0.0, 10.0, 7.0)
    n2 = st.number_input("Nota 2:", 0.0, 10.0, 8.0)
    st.success(f"Resultado: Média **{(n1+n2)/2:.2f}**")

elif opcao == "Desafio 2":
    c = st.number_input("Graus Celsius:", value=30.0)
    st.warning(f"Resultado: **{(c * 9/5) + 32:.2f}°F**")

elif opcao == "Desafio 3":
    raio = st.number_input("Raio do círculo:", min_value=0.0, value=5.0)
    area = 3.14159 * (raio ** 2)
    st.info(f"Área: **{area:.2f} m²**")

elif opcao == "Desafio 4":
    v_hora = st.number_input("Valor por Hora (R$):", value=25.0)
    horas = st.number_input("Horas Trabalhadas:", value=160.0)
    st.success(f"Salário Total: **R$ {v_hora * horas:.2f}**")

elif opcao == "Desafio 5":
    idade = st.number_input("Sua Idade:", min_value=0, step=1, value=18)
    status = "Pode Votar" if idade >= 16 else "Não pode votar"
    st.write(f"Status: **{status}**")

elif opcao == "Desafio 6":
    sal = st.number_input("Salário Atual:", value=2000.0)
    st.success(f"Novo Salário (15%): **R$ {sal * 1.15:.2f}**")

elif opcao == "Desafio 7":
    v1 = st.number_input("Valor 1:", value=10.0)
    v2 = st.number_input("Valor 2:", value=20.0)
    st.write(f"O maior é: **{max(v1, v2)}**")

elif opcao == "Desafio 8":
    num = st.number_input("Digite um número:", value=0.0)
    if num > 0: st.success("POSITIVO")
    elif num < 0: st.error("NEGATIVO")
    else: st.warning("ZERO / NEUTRO")

elif opcao == "Desafio 9":
    p = st.number_input("Peso (kg):", value=75.0)
    a = st.number_input("Altura (m):", value=1.75)
    st.info(f"Seu IMC é: **{p/(a*a):.2f}**")

elif opcao == "Desafio 10":
    inteiro = st.number_input("Número Inteiro:", step=1, value=4)
    st.write("Resultado: **PAR**" if inteiro % 2 == 0 else "Resultado: **ÍMPAR**")

elif opcao == "Desafio 11":
    tab = st.number_input("Ver tabuada do:", step=1, value=5)
    for i in range(1, 11):
        st.write(f"{tab} x {i} = **{tab*i}**")

elif opcao == "Desafio 12":
    f = st.number_input("Fatorial de:", min_value=0, step=1, value=5)
    st.success(f"Resultado {f}! = **{math.factorial(f)}**")

elif opcao == "Desafio 13":
    p1 = st.number_input("Nota 1 (Peso 2):", 0.0, 10.0, 5.0)
    p2 = st.number_input("Nota 2 (Peso 3):", 0.0, 10.0, 6.0)
    p3 = st.number_input("Nota 3 (Peso 5):", 0.0, 10.0, 7.0)
    med_p = (p1*2 + p2*3 + p3*5) / 10
    st.success(f"Média Ponderada: **{med_p:.2f}**")

elif opcao == "Desafio 14":
    st.write("Insira 5 valores para o vetor:")
    v = [st.number_input(f"Valor {i+1}:", key=i) for i in range(5)]
    st.success(f"Soma Total do Vetor: **{sum(v)}**")

elif opcao == "Desafio 15":
    reais = st.number_input("Valor em R$:", value=100.0)
    st.success(f"Convertido: **US$ {reais / 5.0:.2f}**")

elif opcao == "Desafio 16":
    b = st.number_input("Base:", value=10.0)
    h = st.number_input("Altura:", value=5.0)
    st.info(f"Área do Triângulo: **{(b*h)/2:.2f}**")

elif opcao == "Desafio 17":
    compra = st.number_input("Valor da Compra:", value=500.0)
    st.success(f"Com 10% de desconto: **R$ {compra * 0.90:.2f}**")

elif opcao == "Desafio 18":
    l1 = st.number_input("Lado 1:", value=3.0)
    l2 = st.number_input("Lado 2:", value=4.0)
    l3 = st.number_input("Lado 3:", value=5.0)
    if (l1+l2 > l3) and (l1+l3 > l2) and (l2+l3 > l1):
        st.success("Triângulo Válido")
    else:
        st.error("Triângulo Inválido")

elif opcao == "Desafio 19":
    base = st.number_input("Base X:", value=2.0)
    exp = st.number_input("Expoente Y:", value=10.0)
    st.write(f"Resultado: **{base**exp}**")

elif opcao == "Desafio 20":
    cap = st.number_input("Capital Inicial:", value=1000.0)
    taxa = st.number_input("Taxa mensal (%):", value=2.0)
    meses = st.number_input("Meses:", step=1, value=12)
    j = cap * (taxa/100) * meses
    st.error(f"Juros: R$ {j:.2f} | Montante Final: **R$ {cap+j:.2f}**")

st.markdown("---")
st.caption("Desenvolvido por José Henrique Jardim | Ciência de Dados")
