# 📊 Análise de Dados do Spotify - Script Python

Este projeto contém um script Python que analisa seus dados de histórico de reprodução do Spotify, fornecendo insights valiosos sobre seus hábitos de escuta.

## 🎯 Objetivo

O script analisa dados exportados do Spotify para revelar padrões interessantes sobre:
- Suas músicas e artistas favoritos
- Horários de pico de escuta
- Comportamento de "skip" (pular músicas)
- Uso por diferentes plataformas
- Tempo total de escuta


## 🛠️ Pré-requisitos

Para executar o script, você precisa ter instalado:

```bash
pip install pandas matplotlib seaborn
```

## 📊 Dados Analisados

O script trabalha com os seguintes campos do seu histórico do Spotify:

| Campo | Descrição |
|-------|-----------|
| `spotify_track_uri` | URI único da faixa no Spotify |
| `ts` | Timestamp de quando a faixa parou de tocar (UTC) |
| `platform` | Plataforma usada (Android, Web Player, etc.) |
| `ms_played` | Milissegundos reproduzidos |
| `track_name` | Nome da faixa |
| `artist_name` | Nome do artista |
| `album_name` | Nome do álbum |
| `reason_start` | Motivo do início da reprodução |
| `reason_end` | Motivo do fim da reprodução |
| `shuffle` | Se o modo aleatório estava ativo |
| `skipped` | Se a faixa foi pulada |

## 🎵 Insights Gerados

### 1. Top 15 Músicas Mais Ouvidas
Lista das músicas que você mais reproduziu, baseada na contagem de plays.

![Gráfico de Análise 1](figure_1.png)

### 2. Top 15 Artistas Mais Ouvidos
Ranking dos artistas mais reproduzidos, com visualização em gráfico de barras.

### 3. Tempo Total de Escuta
Cálculo do tempo total gasto ouvindo música (em horas).

### 4. Análise de "Skips"
Análise do comportamento de pular músicas:
- `trackdone`: Música tocou até o fim
- `fwdbtn`: Música foi pulada manualmente

### 5. Horários de Pico de Escuta
Identificação dos horários do dia em que você mais ouve música, com visualização em gráfico de barras.

### 6. Análise por Plataforma
Distribuição do uso por diferentes plataformas (Android, Web Player, etc.) com gráfico de pizza e tempo total por plataforma.






