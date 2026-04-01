import streamlit as st
import math

# Configuração da página
st.set_page_config(page_title="OmniLogic v6.2", layout="centered")

st.title("🧪 OmniLogic v6.2")
st.subheader("Sistema Híbrido: Desafios Python & C++")

# ==============================
# FUNÇÃO AUXILIAR PARA VETORES
# ==============================
def parse_lista(texto):
    try:
        separador = "," if "," in texto else " "
        return [float(x.strip()) for x in texto.split(separador) if x.strip()]
    except:
        return None

# ==============================
# BASE DE DADOS C++ (TODOS OS 20)
# ==============================
cpp_db = {
    1: "// Pedro: Soma 3 notas (float) e divide por 3.\n#include <iostream>\nusing namespace std;\nint main() {\n    float n1, n2, n3; cin >> n1 >> n2 >> n3;\n    cout << (n1+n2+n3)/3 << endl; return 0;\n}",
    2: "// Maria: Converte C p/ F usando (C * 9/5) + 32.\n#include <iostream>\nusing namespace std;\nint main() {\n    float c; cin >> c;\n    cout << (c * 9/5) + 32 << endl; return 0;\n}",
    3: "// João: Área do círculo (PI * r^2).\n#include <iostream>\n#include <cmath>\nusing namespace std;\nint main() {\n    float r; cin >> r;\n    cout << 3.1415 * pow(r, 2) << endl; return 0;\n}",
    4: "// Ana: Salário Bruto (horas * valor_hora).\n#include <iostream>\nusing namespace std;\nint main() {\n    float h, v; cin >> h >> v;\n    cout << \"R$ \" << h * v << endl; return 0;\n}",
    5: "// Joaquim: Verifica idade >= 18.\n#include <iostream>\nusing namespace std;\nint main() {\n    int i; cin >> i;\n    if(i>=18) cout << \"Pode votar\"; else cout << \"Nao\"; return 0;\n}",
    6: "// Maria: Classificação por conceitos A-E.\n#include <iostream>\nusing namespace std;\nint main() {\n    float n; cin >> n;\n    if(n>=9) cout<<'A'; else if(n>=7) cout<<'B'; else if(n>=5) cout<<'C'; else if(n>=3) cout<<'D'; else cout<<'E'; return 0;\n}",
    7: "// Carlos: Maior de 3 números.\n#include <iostream>\n#include <algorithm>\nusing namespace std;\nint main() {\n    float a,b,c; cin >> a >> b >> c;\n    cout << max({a,b,c}); return 0;\n}",
    8: "// Silva: Condição de existência de triângulo.\n#include <iostream>\nusing namespace std;\nint main() {\n    float a,b,c; cin >> a >> b >> c;\n    if(a+b>c && a+c>b && b+c>a) cout << \"Valido\"; else cout << \"Invalido\"; return 0;\n}",
    9: "// Lucas: Soma de 1 até N usando loop.\n#include <iostream>\nusing namespace std;\nint main() {\n    int n, s=0; cin >> n;\n    for(int i=1; i<=n; i++) s+=i;\n    cout << s; return 0;\n}",
    10: "// Maria: Fatorial (n!).\n#include <iostream>\nusing namespace std;\nint main() {\n    int n; long long f=1; cin >> n;\n    for(int i=1; i<=n; i++) f*=i;\n    cout << f; return 0;\n}",
    11: "// Pedro: Tabuada de 1 a 10.\n#include <iostream>\nusing namespace std;\nint main() {\n    int n; cin >> n;\n    for(int i=1; i<=10; i++) cout << n << \"x\" << i << \"=\" << n*i << endl;\n    return 0;\n}",
    12: "// Programação: Conta pares de 1 a 100.\n#include <iostream>\nusing namespace std;\nint main() {\n    int c=0; for(int i=1; i<=100; i++) if(i%2==0) c++;\n    cout << c; return 0;\n}",
    13: "// André: Vetor de 10 posições.\n#include <iostream>\nusing namespace std;\nint main() {\n    int v[10]; for(int i=0; i<10; i++) cin >> v[i];\n    for(int i=0; i<10; i++) cout << v[i] << \" \"; return 0;\n}",
    14: "// Júlio: Soma elementos do vetor.\n#include <iostream>\nusing namespace std;\nint main() {\n    int v[10], s=0; for(int i=0; i<10; i++) { cin >> v[i]; s+=v[i]; }\n    cout << s; return 0;\n}",
    15: "// Maria: Busca valor no vetor.\n#include <iostream>\nusing namespace std;\nint main() {\n    int v[10], b; bool f=false; for(int i=0; i<10; i++) cin >> v[i]; cin >> b;\n    for(int i=0; i<10; i++) if(v[i]==b) f=true; cout << (f?\"Achei\":\"Nao\"); return 0;\n}",
    16: "// Pedro: Contagem de ocorrências.\n#include <iostream>\nusing namespace std;\nint main() {\n    int v[10], b, c=0; for(int i=0; i<10; i++) cin >> v[i]; cin >> b;\n    for(int i=0; i<10; i++) if(v[i]==b) c++; cout << c; return 0;\n}",
    17: "// Dardos: Média de 30 lançamentos.\n#include <iostream>\nusing namespace std;\nint main() {\n    float v[30], s=0; for(int i=0; i<30; i++) { cin >> v[i]; s+=v[i]; }\n    cout << s/30; return 0;\n}",
    18: "// Loja: Filtra preços > 50.\n#include <iostream>\nusing namespace std;\nint main() {\n    float v[10]; int c=0; for(int i=0; i<10; i++) { cin >> v[i]; if(v[i]>50) c++; }\n    cout << c; return 0;\n}",
    19: "// Clube: Acima da média do grupo.\n#include <iostream>\nusing namespace std;\nint main() {\n    int v[10], s=0, c=0; for(int i=0; i<10; i++) { cin >> v[i]; s+=v[i]; }\n    float m = s/10.0; for(int i=0; i<10; i++) if(v[i]>m) c++; cout << c; return 0;\n}",
    20: "// Padaria: Soma preços de valor par.\n#include <iostream>\nusing namespace std;\nint main() {\n    int v[5], s=0; for(int i=0; i<5; i++) { cin >> v[i]; if(v[i]%2==0) s+=v[i]; }\n    cout << s; return 0;\n}"
}

# ==============================
# INTERFACE E LÓGICA (SIDEBAR)
# ==============================
menu = [f"Desafio {i}" for i in range(1, 21)]
escolha = st.sidebar.selectbox("Selecione o Desafio", menu)
num_desafio = int(escolha.split(" ")[1])

# Enunciados originais
enunciados = {
    1: "Pedro quer calcular a média de Matemática, Português e Ciências.",
    2: "Maria quer converter Celsius para Fahrenheit.",
    3: "João quer calcular a área de um círculo.",
    4: "Ana quer calcular seu salário bruto.",
    5: "Verificar se Joaquim tem idade para votar (18 anos).",
    6: "Classificar nota da Maria em conceitos A-E.",
    7: "Carlos quer encontrar o maior de três valores.",
    8: "Silva quer saber se três segmentos formam um triângulo.",
    9: "Lucas quer a soma dos N primeiros números naturais.",
    10: "Maria quer calcular o fatorial de um número.",
    11: "Pedro quer gerar a tabuada de um número.",
    12: "Contar quantos números pares existem entre 1 e 100.",
    13: "André quer criar e imprimir um vetor de 10 números.",
    14: "Júlio precisa da soma dos elementos de um vetor.",
    15: "Maria busca uma temperatura específica em um vetor.",
    16: "Pedro quer contar as ocorrências de um valor no vetor.",
    17: "Média de 30 lançamentos de dardos (10 participantes).",
    18: "Filtrar camisetas com preço superior a R$ 50,00.",
    19: "Contar membros que leram acima da média do grupo.",
    20: "Soma total apenas dos pães com valor par."
}

st.markdown(f"## 📍 {escolha}")
st.info(enunciados[num_desafio])

# ==============================
# RESOLUÇÕES PYTHON
# ==============================
if num_desafio == 1:
    v1 = st.number_input("Matemática", key="d1a"); v2 = st.number_input("Português", key="d1b"); v3 = st.number_input("Ciências", key="d1c")
    if st.button("Calcular"): st.success(f"Média: {(v1+v2+v3)/3:.2f}")

elif num_desafio == 2:
    c = st.number_input("Celsius", key="d2"); 
    if st.button("Converter"): st.success(f"Fahrenheit: {(c*9/5)+32:.2f}")

elif num_desafio == 3:
    r = st.number_input("Raio", key="d3"); 
    if st.button("Área"): st.success(f"Resultado: {math.pi*r**2:.2f}")

elif num_desafio == 4:
    h = st.number_input("Horas", key="d4a"); v = st.number_input("Taxa", key="d4b")
    if st.button("Salário"): st.success(f"Bruto: R$ {h*v:.2f}")

elif num_desafio == 5:
    i = st.number_input("Idade", step=1, key="d5")
    if st.button("Checar"): st.success("Pode votar" if i>=18 else "Não pode")

elif num_desafio == 6:
    n = st.number_input("Nota", key="d6")
    if st.button("Ver"):
        if n>=9: c="A"
        elif n>=7: c="B"
        elif n>=5: c="C"
        elif n>=3: c="D"
        else: c="E"
        st.success(f"Conceito: {c}")

elif num_desafio == 7:
    a = st.number_input("V1"); b = st.number_input("V2"); c = st.number_input("V3")
    if st.button("Maior"): st.success(max(a,b,c))

elif num_desafio == 8:
    a=st.number_input("L1"); b=st.number_input("L2"); c=st.number_input("L3")
    if st.button("Validar"): st.success("Triângulo" if a+b>c and a+c>b and b+c>a else "Invalido")

elif num_desafio == 9:
    n = st.number_input("N", step=1)
    if st.button("Somar"): st.success(sum(range(1, int(n)+1)))

elif num_desafio == 10:
    n = st.number_input("N", step=1)
    if st.button("Fatorial"): st.success(math.factorial(int(n)))

elif num_desafio == 11:
    n = st.number_input("N", step=1)
    if st.button("Gerar"): 
        for i in range(1,11): st.write(f"{n} x {i} = {n*i}")

elif num_desafio == 12:
    if st.button("Contar"): st.success(len([x for x in range(1,101) if x%2==0]))

elif num_desafio >= 13:
    txt = st.text_input("Valores (separados por vírgula)")
    if st.button("Executar"):
        vetor = parse_lista(txt)
        if vetor:
            if num_desafio == 13: st.write(vetor)
            if num_desafio == 14: st.success(sum(vetor))
            if num_desafio == 15: 
                b = st.number_input("Buscar", key="bs")
                st.write("Achei" if b in vetor else "Não")
            if num_desafio == 16: 
                b = st.number_input("Contar", key="bc")
                st.write(vetor.count(b))
            if num_desafio == 17: st.success(sum(vetor)/len(vetor))
            if num_desafio == 18: st.success(len([x for x in vetor if x>50]))
            if num_desafio == 19:
                m = sum(vetor)/len(vetor)
                st.success(len([x for x in vetor if x>m]))
            if num_desafio == 20: st.success(sum([x for x in vetor if x%2==0]))
        else: st.error("Dados inválidos.")

# ==============================
# ÁREA C++ (EXPANDER)
# ==============================
st.markdown("---")
with st.expander("🛠️ Desenvolvimento em C++"):
    st.markdown("### 📝 Explicação e Código")
    st.code(cpp_db[num_desafio], language="cpp")
