import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Configuração de estilo para ficar "bonito" e acadêmico
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']

# 1. DADOS DO GRÁFICO
# Mapeamento: O ano tem 24 quinzenas (0 a 23).
# Tuplas representam (início, duração) em quinzenas.
# Ex: (0, 2) começa na 1ª quinzena de Jan e dura 2 quinzenas (o mês todo).

atividades = {
    "Calagem": [
        (9, 2),   # Mai 2 - Jun 1
        (21, 2)   # Nov 2 - Dez 1
    ],
    "Adubação": [
        (0, 5),   # Jan 1 - Mar 1
        (11, 7),  # Jun 2 - Set 2
        (23, 1)   # Dez 2
    ],
    "Gradagem pós-semeadura": [
        (0, 2),   # Jan 1 - Jan 2
        (9, 5),   # Mai 2 - Jul 2
        (21, 3)   # Nov 2 - Dez 2
    ],
    "Semeadura (pasto)": [
        (0, 2),   # Jan 1 - Jan 2
        (9, 5),   # Mai 2 - Jul 2
        (21, 3)   # Nov 2 - Dez 2
    ],
    "Gradagem pré-semeadura": [
        (0, 2),   # Jan 1 - Jan 2
        (9, 5),   # Mai 2 - Jul 2
        (21, 3)   # Nov 2 - Dez 2
    ]
}

# Cores para cada atividade (Paleta profissional / Agronomia)
cores = {
    "Calagem": "#E74C3C",                # Vermelho suave
    "Adubação": "#F39C12",               # Laranja/Amarelo
    "Gradagem pós-semeadura": "#8E44AD", # Roxo
    "Semeadura (pasto)": "#27AE60",      # Verde
    "Gradagem pré-semeadura": "#2980B9"  # Azul
}

# 2. CONFIGURAÇÃO DA PLOTAGEM
fig, ax = plt.subplots(figsize=(14, 6)) # Tamanho da imagem (largura, altura)

# Altura e posição das barras
y_pos = range(len(atividades))
altura_barra = 0.6

# Loop para desenhar as barras
titulos_y = []
for i, (nome_atividade, periodos) in enumerate(atividades.items()):
    titulos_y.append(nome_atividade)
    cor = cores.get(nome_atividade, "#333333")
    
    # Desenha todas as faixas de tempo para essa atividade
    ax.broken_barh(periodos, (i - altura_barra/2, altura_barra), 
                   facecolors=cor, edgecolor='white', linewidth=1, alpha=0.9)

# 3. CUSTOMIZAÇÃO DOS EIXOS

# Eixo Y
ax.set_yticks(range(len(atividades)))
ax.set_yticklabels(titulos_y, fontsize=12, fontweight='bold', color='#333333')

# Eixo X (Meses e Quinzenas)
# Vamos configurar 24 ticks (quinzenas) mas mostrar rótulos apenas nos meses
ax.set_xlim(0, 24)
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
         'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

# Ticks principais (Meses) - colocados no meio do mês (ex: 1, 3, 5...)
ticks_meses = [x * 2 + 1 for x in range(12)]
ax.set_xticks(ticks_meses)
ax.set_xticklabels(meses, fontsize=11, fontweight='bold')

# Adicionar linhas verticais para separar os meses visualmente
for x in range(0, 25, 2):
    ax.axvline(x, color='gray', linestyle='--', alpha=0.3, linewidth=0.8)

# Títulos e Legendas
ax.set_title('Cronograma de Operações Agrícolas - Fazenda Canoas', 
             fontsize=16, fontweight='bold', pad=20, color='#2C3E50')
ax.set_xlabel('Meses (divididos em quinzenas)', fontsize=11, labelpad=10)

# Inverter eixo Y para que a primeira atividade da lista fique no topo (opcional, 
# mas como inserimos de baixo pra cima no dict, o matplotlib inverte por padrão se não tratarmos.
# Aqui mantivemos a ordem de inserção visualmente).

# Ajustes finais de layout
plt.tight_layout()

# Salvar imagem em alta resolução
caminho_arquivo = "grafico_gantt_mecanizacao.png"
plt.savefig(caminho_arquivo, dpi=300)
plt.show()

print(f"Gráfico salvo como {caminho_arquivo}")