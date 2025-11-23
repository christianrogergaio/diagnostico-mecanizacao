import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# --- Dados do Calendário Operacional (baseado no PDF) ---
# Cada tupla contém: (Operação, Data Início, Data Fim)
# As datas são 'YYYY-MM-DD'. Assumi 2024 como ano base.
# Q1 = 1º ao 15º dia / Q2 = 16º ao fim do mês

dados_operacoes = [
    # Gradagem pré-semeadura: Fev (Q2), Jun (Q2)
    ("Gradagem pré-semeadura", "2024-02-16", "2024-02-29"),
    ("Gradagem pré-semeadura", "2024-06-16", "2024-06-30"),

    # Semeadura (pasto): Jun (Q2)
    ("Semeadura (pasto)", "2024-06-16", "2024-06-30"),

    # Gradagem pós-semeadura: Fev (Q2), Jun (Q2), Ago (Q1)
    ("Gradagem pós-semeadura", "2024-02-16", "2024-02-29"),
    ("Gradagem pós-semeadura", "2024-06-16", "2024-06-30"),
    ("Gradagem pós-semeadura", "2024-08-01", "2024-08-15"),

    # Adubação (Ureia): Jul (Q2), Ago (Q1+Q2), Set (Q1), Dez (Q1)
    ("Adubação (Ureia)", "2024-07-16", "2024-07-31"),
    ("Adubação (Ureia)", "2024-08-01", "2024-08-31"), # Q1+Q2
    ("Adubação (Ureia)", "2024-09-01", "2024-09-15"),
    ("Adubação (Ureia)", "2024-12-01", "2024-12-15"),
    
    # Calagem (não plotada, pois é a cada 1-2 anos)
    # ("Calagem", "2024-01-01", "2024-12-31"), 
]

# --- Processamento dos Dados ---

# Nomes únicos das operações (para o eixo Y)
operacoes = sorted(list(set([d[0] for d in dados_operacoes])))

# Cores para cada operação
cores_hex = ['#4285F4', '#DB4437', '#F4B400', '#0F9D58']
mapa_cores = {op: cor for op, cor in zip(operacoes, cores_hex)}

# Estrutura para o plot
barras = []
for i, op in enumerate(operacoes):
    for dado in dados_operacoes:
        if dado[0] == op:
            # Converter datas de string para datetime
            inicio = datetime.strptime(dado[1], '%Y-%m-%d')
            fim = datetime.strptime(dado[2], '%Y-%m-%d')
            
            # Converter para o formato numérico do matplotlib
            inicio_num = mdates.date2num(inicio)
            fim_num = mdates.date2num(fim)
            duracao = fim_num - inicio_num
            
            # Adicionar à lista de barras: (posição_y, inicio_x, duracao_x)
            barras.append((i, inicio_num, duracao))

# --- Criação do Gráfico ---
fig, ax = plt.subplots(figsize=(12, 6))

# Plotar as barras horizontais
for i, barra in enumerate(barras):
    pos_y, inicio_x, duracao_x = barra
    # Encontrar a operação correspondente para pegar a cor
    op_nome = operacoes[pos_y]
    ax.barh(pos_y, duracao_x, left=inicio_x, height=0.6, 
            color=mapa_cores[op_nome], edgecolor='black', alpha=0.8)

# --- Formatação ---

# Eixo Y (Operações)
ax.set_yticks(range(len(operacoes)))
ax.set_yticklabels(operacoes, fontsize=12)
ax.invert_yaxis()  # Coloca a primeira operação no topo

# Eixo X (Datas/Meses)
ax.set_xlabel("Mês", fontsize=12, labelpad=10)
ax.xaxis_date() # Informa que o eixo X é de datas

# Definir os limites do eixo X (de Jan a Dez)
ax.set_xlim(mdates.date2num(datetime(2024, 1, 1)), 
            mdates.date2num(datetime(2024, 12, 31)))

# Formatar os "ticks" (marcas) do eixo X para mostrar os meses
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b')) # %b = Mês abreviado (Jan, Fev, ...)
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=mdates.MO))

# Título
ax.set_title("Calendário Operacional - Fazenda Canoas", fontsize=16, pad=20, weight='bold')

# Adicionar grid
ax.grid(axis='x', linestyle='--', alpha=0.7)
ax.grid(axis='y', linestyle='-', alpha=0.2)

# Remover as bordas (spines) de cima e da direita
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

# --- Salvar o arquivo ---
nome_arquivo = 'gantt_mecanizacao.png'
plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')

print(f"Gráfico salvo como '{nome_arquivo}'")

plt.show() # Opcional: mostrar o gráfico na tela