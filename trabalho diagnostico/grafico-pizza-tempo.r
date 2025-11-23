import matplotlib.pyplot as plt
import numpy as np

# --- 1. DADOS EXTRAÍDOS DO TEXTO ---

# Tempos unitários (uma passada) por Piquete em MINUTOS
# (Já incluindo os tempos de deslocamento mencionados no texto)
# A3, A4, A5, A6, A7
tempos_gradagem_min = [50, 63, 321, 405, 28] 
tempos_distribuidor_min = [25.7, 31.4, 165, 207, 16]

# Somatório de uma passada completa na propriedade
total_gradagem_passada = sum(tempos_gradagem_min)
total_distribuidor_passada = sum(tempos_distribuidor_min)

# --- 2. ESTRUTURA ANUAL DE OPERAÇÕES ---
# O texto menciona: Gradagem x2 + Distribuidor x2 (Semeadura + Adubação)

labels = [
    'Gradagem Pré-Semeadura', 
    'Semeadura (Distribuidor)', 
    'Gradagem Pós (Incorporação)', 
    'Adubação Ureia (Distribuidor)'
]

# Valores em horas para o gráfico
valores_minutos = [
    total_gradagem_passada,      # Gradagem 1
    total_distribuidor_passada,  # Semeadura
    total_gradagem_passada,      # Gradagem 2
    total_distribuidor_passada   # Adubação
]

valores_horas = [v / 60 for v in valores_minutos]
total_horas_ano = sum(valores_horas)

# --- 3. CONFIGURAÇÃO DO GRÁFICO ---
# Cores profissionais (Tons terrosos para solo, Tons verdes para insumos)
colors = ['#8D6E63', '#66BB6A', '#A1887F', '#98E69C']
explode = (0.05, 0.05, 0.05, 0.05)  # Separa levemente todas as fatias

fig, ax = plt.subplots(figsize=(10, 7))

# Criação do Gráfico de Pizza (com furo no meio = Donut)
wedges, texts, autotexts = ax.pie(
    valores_horas, 
    labels=labels, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    explode=explode,
    pctdistance=0.85, # Distância da porcentagem do centro
    textprops=dict(color="black")
)

# Desenha um círculo branco no centro para transformar em Donut
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# --- 4. ESTILIZAÇÃO ---
plt.setp(texts, size=11, weight="bold")
plt.setp(autotexts, size=10, weight="bold", color="white")

# Ajuste das cores dos textos de porcentagem para garantir contraste
autotexts[0].set_color('white')
autotexts[1].set_color('black')
autotexts[2].set_color('white')
autotexts[3].set_color('black')

# Título e Subtítulo central
ax.set_title(f'Distribuição do Tempo Operacional Anual\n(Total Estimado: {total_horas_ano:.1f} horas)', 
             fontsize=14, fontweight='bold', pad=20)

# Adiciona texto no centro do Donut
ax.text(0, 0, f'{total_horas_ano:.0f}h\nTotais', ha='center', va='center', fontsize=14, fontweight='bold', color='#555')

plt.tight_layout()

# Salvar
plt.savefig('grafico_operacoes_pizza.png', dpi=300)
plt.show()