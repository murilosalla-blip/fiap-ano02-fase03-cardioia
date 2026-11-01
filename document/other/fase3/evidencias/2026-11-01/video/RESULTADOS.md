# Publicação e conferência do vídeo do Ir Além 2

Publicamos o [vídeo CardioIA — Fase 3, Ir Além 2](https://youtu.be/-v9lWpZ_JJo) em 01/11/2026. Conferimos no YouTube o título, a indicação **Não listado**, a duração **2:59** e o início da reprodução em navegador sem login. Não alteramos configurações da conta durante essa consulta.

## Duração e apresentação visual

Na versão local utilizada para a publicação, medimos **179,25805 segundos**, em 1280 × 720, abaixo do limite de quatro minutos. Inspecionamos quadros a intervalos de cinco segundos e cruzamos os três gráficos com os originais do experimento. Conferimos partições 144/48/48 por sessão, logística com oito atributos, LIF com 24 neurônios e representação de 120 atributos, matrizes, 44/48 e 35/48 acertos, percentuais 91,67% e 72,92% e F1 macro 0,9165 e 0,7262.

Mantemos a limitação visual de gráficos LIF e matrizes reduzidos em algumas cenas. Os originais legíveis continuam disponíveis no [notebook](../../../../../../src/fase3/notebooks/comparacao_temporal_lif.ipynb), nos [resultados](../../../../../../assets/fase3/resultados/neuromorfismo/) e no [relatório comparativo](../../../../../fase3/CardioIA_Fase3_Relatorio_Neuromorfismo.pdf). A tabela do vídeo utiliza o rótulo genérico “Acurácia”; neste teste equilibrado os valores coincidem com a acurácia balanceada do relatório.

## Conteúdo narrado conferido pela transcrição

As legendas automáticas ficaram disponíveis durante a consulta. Obtivemos a transcrição em português e comparamos seu conteúdo com o experimento:

- **0:00–0:16:** identificamos os três integrantes e o objetivo de classificar regimes de oscilação sintéticos, sem diagnosticar doenças.
- **0:21–0:57:** distinguimos os regimes lento/rápido, apresentamos 240 sessões de 120 leituras, intervalo de cinco segundos e dez minutos por sessão, além da separação 144/48/48 antes das janelas. A fala esclarece que dez minutos correspondem a cada sessão, apesar da expressão abreviada “totais” na tela.
- **1:00–1:25:** comparamos logística com oito atributos e LIF com 24 neurônios/120 atributos, integração, fuga, limiar, disparo e reset; restringimos normalização ao treino e seleção à validação.
- **1:28–2:01:** apresentamos as mesmas 48 sessões de teste, os erros por classe, os acertos e as métricas coerentes com as matrizes e os resultados versionados.
- **2:04–2:37:** discutimos melhor desempenho e simplicidade do tradicional neste ensaio, dinâmica temporal do LIF, representações diferentes, dados sintéticos e uma semente. Não generalizamos inferioridade do LIF e declaramos ausência de validação clínica ou medição energética.
- **2:40–2:54:** indicamos código, notebook executado, relatório de duas páginas e nove testes aprovados no GitHub; creditamos o apoio do NotebookLM.

Esta conferência utiliza **transcrição automática**, sujeita a erros de reconhecimento de nomes e termos técnicos, e não equivale a uma escuta humana integral. Não atribuímos ao áudio os erros ortográficos produzidos pelas legendas. Mantemos os roteiros e tentativas de produção somente nos materiais internos locais.

## Situação da entrega

Atualizamos o link no README raiz, no guia do desafio, na matriz de requisitos e nos documentos de submissão/comparação. A publicação no YouTube e as verificações acima não representam envio na plataforma FIAP nem aprovação antecipada. Permanecem a conferência do cadastro dos integrantes, as regras de upload, a publicação desta revisão documental e a submissão acadêmica confirmada.
