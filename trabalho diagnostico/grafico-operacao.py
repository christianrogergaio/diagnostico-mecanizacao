import matplotlib.pyplot as plt
import numpy as np

# Configuração de Estilo Geral para parecer "Engenharia Moderna"
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.titleweight'] = 'bold'

# --- DADOS (Baseados no Relatório Calculos_Mecanizacao.tex) ---
piquetes = ['A3', 'A4', 'A5', 'A6', 'A7']
areas = [1.8, 2.2, 11.2, 14.2, 0.8]

# Tempos em Horas (Convertendo os minutos/horas da Tabela do relatório para decimal)
# Gradagem (com tempo auxiliar nas áreas grandes)
tempo_gradagem = [1.13, 1.38, 7.17, 9.08, 0.58] 
# Distribuição (com tempo auxiliar nas áreas grandes)
tempo_distribuicao = [0.53, 0.67, 3.43, 4.33, 0.32]

# Consumo de Diesel (Litros)
consumo_diesel = [30.0, 36.9, 190.8, 241.5, 16.2]

# Cores Personalizadas (Paleta sóbria e profissional)
cor_gradagem = '#d35400'      # Laranja terroso (solo)
cor_distribuicao = '#2980b9'  # Azul (químico/adubo)
cor_diesel = '#2c3e50'        # Cinza escuro (combustível)

# ==============================================================================
# GRÁFICO 1: ROSCA (Proporção de Tempo Total)
# ==============================================================================
fig1, ax1 = plt.subplots(figsize=(8, 6))

total_grad = sum(tempo_gradagem)
total_dist = sum(tempo_distribuicao)
tamanhos = [total_grad, total_dist]
labels = ['Gradagem\n(Preparo)', 'Distribuição\n(Sementes/Adubo)']
cores = [cor_gradagem, cor_distribuicao]

# Criando a rosca
wedges, texts, autotexts = ax1.pie(tamanhos, labels=labels, autopct='%1.1f%%', 
                                   startangle=90, colors=cores, pctdistance=0.85,
                                   wedgeprops=dict(width=0.3, edgecolor='w'),
                                   textprops={'fontsize': 12})

# Ajustando estilo do texto
for text in texts:
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Círculo central para efeito "Donut"
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig1.gca().add_artist(centre_circle)

ax1.set_title('Proporção do Tempo Operacional Total\n(Todas as Áreas)', pad=20)
plt.tight_layout()
plt.savefig('grafico_proporcao_tempo.png', dpi=300)
print("Gráfico 1 gerado: grafico_proporcao_tempo.png")

# ==============================================================================
# GRÁFICO 2: BARRAS EMPILHADAS (Tempo por Piquete)
# ==============================================================================
fig2, ax2 = plt.subplots(figsize=(10, 6))

# Plotando as barras
bar1 = ax2.bar(piquetes, tempo_gradagem, label='Gradagem', color=cor_gradagem, alpha=0.9)
bar2 = ax2.bar(piquetes, tempo_distribuicao, bottom=tempo_gradagem, label='Distribuição', color=cor_distribuicao, alpha=0.9)

# Labels e Títulos
ax2.set_ylabel('Tempo Operacional (Horas)')
ax2.set_xlabel('Piquetes')
ax2.set_title('Demanda de Tempo de Máquina por Piquete')
ax2.legend()

# Adicionando os valores totais no topo das barras
tempos_totais = [t_g + t_d for t_g, t_d in zip(tempo_gradagem, tempo_distribuicao)]
for i, v in enumerate(tempos_totais):
    ax2.text(i, v + 0.2, f"{v:.1f}h", ha='center', va='bottom', fontweight='bold', color='#555555')

# Remover bordas desnecessárias
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('grafico_tempo_por_piquete.png', dpi=300)
print("Gráfico 2 gerado: grafico_tempo_por_piquete.png")

# ==============================================================================
# GRÁFICO 3: BARRAS HORIZONTAIS (Consumo de Diesel)
# ==============================================================================
fig3, ax3 = plt.subplots(figsize=(10, 5))

# Ordenar os dados para ficar mais bonito (do maior para o menor)
indices_ordenados = np.argsort(consumo_diesel)
piquetes_ord = [piquetes[i] for i in indices_ordenados]
diesel_ord = [consumo_diesel[i] for i in indices_ordenados]

bars = ax3.barh(piquetes_ord, diesel_ord, color=cor_diesel, alpha=0.8)

# Adicionar os valores na frente das barras
for bar in bars:
    width = bar.get_width()
    ax3.text(width + 5, bar.get_y() + bar.get_height()/2, 
             f'{width:.1f} L', 
             ha='left', va='center', fontweight='bold', color='black')

ax3.set_xlabel('Volume (Litros)')
ax3.set_title('Consumo Total de Óleo Diesel por Piquete\n(Ciclo Completo)')
ax3.grid(axis='x', linestyle='--', alpha=0.7)

# Remover bordas
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('grafico_consumo_diesel.png', dpi=300)
print("Gráfico 3 gerado: grafico_consumo_diesel.png")

# Mostra os gráficos (se estiver rodando em ambiente interativo)
# plt.show()