import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('spotify_history.csv')

# --- Preparação e Limpeza dos Dados ---
# Converte a coluna de timestamp (ts) para o formato de data e hora
df['ts'] = pd.to_datetime(df['ts'])
# Converte milissegundos (ms_played) para minutos para facilitar a leitura
df['minutes_played'] = df['ms_played'] / 60000



# Suas Músicas Mais Ouvidas
print("--- 🎶 Top 15 Músicas Mais Ouvidas ---")
top_15_musicas = df['track_name'].value_counts().head(15)
print(top_15_musicas)
print("-" * 30)


# Seus Artistas Mais Ouvidos
print("\n--- 🎤 Top 15 Artistas Mais Ouvidos ---")
top_15_artistas = df['artist_name'].value_counts().head(15)
print(top_15_artistas)
print("-" * 30)

# Visualização dos Top Artistas
plt.figure(figsize=(12, 7))
sns.barplot(x=top_15_artistas.values, y=top_15_artistas.index, palette='viridis')
plt.title('Top 15 Artistas Mais Ouvidos (por nº de plays)')
plt.xlabel('Número de Músicas Tocadas')
plt.ylabel('Artista')
plt.tight_layout()
plt.show()


# Tempo Total de Escuta
print("\n--- 🎧 Tempo Total de Escuta ---")
total_horas_ouvidas = df['minutes_played'].sum() / 60
print(f"Você ouviu um total de {total_horas_ouvidas:.2f} horas de música neste relatório.")
print("-" * 30)


# Análise de "Skips" (Músicas Puladas)
print("\n--- ⏭️ Análise de Músicas Puladas (Skips) ---")
# Analisa a coluna 'reason_end' para ver por que as faixas pararam
# 'trackdone' significa que a música tocou até o fim.
# 'fwdbtn' significa que você pulou para a próxima.
razoes_final = df['reason_end'].value_counts(normalize=True) * 100
print(razoes_final)
print("\nIsso significa que, por exemplo, você ouve as músicas até o fim em {:.2f}% das vezes.".format(razoes_final.get('trackdone', 0)))
print("-" * 30)


# Seus Horários de Pico de Escuta
print("\n--- ⏰ Horários em que Você Mais Ouve Música ---")
# Extrai a hora do dia da coluna de timestamp
df['hour_played'] = df['ts'].dt.hour
horas_de_pico = df['hour_played'].value_counts().sort_index()

# Visualização dos horários de pico
plt.figure(figsize=(12, 6))
horas_de_pico.plot(kind='bar', color='salmon')
plt.title('Número de Músicas Tocadas por Hora do Dia')
plt.xlabel('Hora do Dia')
plt.ylabel('Quantidade de Músicas')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()

# Análise por Plataforma de Escuta ---
print("\n--- 📱 Análise por Plataforma (Android, Web Player, etc.) ---")
plataforma_uso = df['platform'].value_counts()
print("Contagem de plays por plataforma:")
print(plataforma_uso)

# Visualização da Análise de Plataforma
plt.figure(figsize=(10, 7))
# Usamos autopct para mostrar a porcentagem diretamente no gráfico
plt.pie(plataforma_uso, labels=plataforma_uso.index, autopct='%1.1f%%', startangle=140, 
        wedgeprops={'edgecolor': 'white'})
plt.title('Distribuição de Uso por Plataforma')
plt.ylabel('') # Remove o label 'platform' que o matplotlib adiciona por padrão
plt.axis('equal')  # Garante que o gráfico de pizza seja um círculo.
plt.show()

# Tempo de escuta por plataforma
tempo_por_plataforma = df.groupby('platform')['minutes_played'].sum() / 60
print("\nTempo total de escuta por plataforma (em horas):")
print(tempo_por_plataforma.round(2))
print("-" * 30)


