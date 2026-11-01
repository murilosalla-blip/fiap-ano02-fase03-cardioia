# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%"></a>
</p>

<br>

# CardioIA — Fases 1, 2 e 3

## Grupo Aura

## 👨‍🎓 Integrantes:

- Murilo Salla — RM568041
- Elias da Silva de Souza — RM568500
- Julia Duarte de Carvalho — RM567816

## 👩‍🏫 Professores:

### Tutor(a)

- Leonardo Ruiz Orabona

### Coordenador(a)

- André Godoi Chiovato

## 📜 Descrição

Desenvolvemos o **CardioIA** como projeto acadêmico da FIAP. Na Fase 1, organizamos dados numéricos, textuais e visuais; na Fase 2, implementamos modelos e aplicações; na Fase 3, acrescentamos captura simulada, resiliência offline, MQTT, dashboard e desafios de automação e IA temporal. Preservamos as entregas anteriores e documentamos os limites de cada experimento.

> **Uso exclusivamente educacional.** Não realizamos diagnóstico, não estimamos risco clínico real e não substituímos avaliação médica.

## 📊 Fase 1 — Batimentos de Dados

Organizamos a entrega obrigatória da Fase 1 em três partes complementares, preparando os dados para as etapas seguintes do CardioIA:

**Parte 1 — Dados Numéricos:** utilizamos o dataset público *Heart Disease (Cleveland)*, do UCI Machine Learning Repository (303 registros, 14 variáveis clínicas — idade, sexo, pressão arterial, colesterol, sintomas, frequência cardíaca, entre outras), processado em `assets/fase1/dados/processed/`, com dicionário de variáveis e justificativa clínica da relevância de cada atributo documentados em `document/fase1/` para os experimentos tabulares de Machine Learning da Fase 2.

**Parte 2 — Dados Textuais:** reunimos dois textos `.txt` derivados de publicações oficiais do Ministério da Saúde/CONITEC — um sobre prevenção cardiovascular (fatores de risco, atenção básica) e outro sobre manejo de síndromes coronarianas agudas (sintomas, diagnóstico, tratamento) — formando um corpus complementar (antes vs. depois do evento cardíaco). Esse corpus poderá apoiar futuramente tarefas de NLP como identificação e extração de termos clínicos (sintomas, fatores de risco, procedimentos), classificação temática (prevenção vs. evento agudo), recuperação de informação e sumarização, além de servir de base textual para um sistema de perguntas e respostas ou para o Assistente Cardiológico Virtual (Fase 5).

**Parte 3 — Dados Visuais:** reunimos 120 imagens de eletrocardiograma (ECG), curadas a partir do dataset público *ECG Images dataset of Cardiac Patients* (Mendeley Data), balanceadas em 4 classes (`normal`, `myocardial_infarction`, `history_mi`, `abnormal_heartbeat`), com curadoria rigorosa (deduplicação por hash, remoção de dados administrativos/pessoais). Cada arquivo `.jpg` representa uma imagem de um exame de ECG de 12 derivações — não necessariamente um paciente único. Esse conjunto poderá ser reutilizado futuramente para classificação de imagens de ECG, aprendizado de padrões visuais e experimentos de distinção entre as quatro classes disponibilizadas com técnicas de Visão Computacional (Fase 4), sem qualquer promessa de capacidade diagnóstica clínica nesta etapa.

Nas três partes, seguimos um processo de **governança de dados** com atenção à proveniência, privacidade, qualidade e rastreabilidade. Limitações e possíveis vieses identificados, detalhados nos documentos específicos em `document/fase1/`: a Parte 1 usa uma base originada na Cleveland Clinic (EUA, década de 1980), sem representatividade populacional garantida para outros contextos; a Parte 2 usa textos institucionais brasileiros de linguagem técnica (não espontânea de pacientes), sendo que um dos materiais tem contexto temporal mais antigo (2006); a Parte 3 usa um dataset originado no Paquistão, com possíveis vieses de população e de equipamento de aquisição, e a amostra curada e balanceada não representa necessariamente a prevalência real das condições nas classes.

**Materiais externos:** [dados numéricos](https://drive.google.com/drive/folders/1I_gzbCuJUYvx0lwPtg5XhDf-IH039t2s?usp=sharing), [textos](https://drive.google.com/drive/folders/1Qc5W_RoAIq1sopROYvCss5uBwO0IlI6C?usp=sharing) e [imagens ECG](https://drive.google.com/drive/folders/135ZuObt02AxX13aiQG_sqef9nxAjkPMy?usp=sharing), preservados no Google Drive.

**Versão histórica:** [repositório da Fase 1](https://github.com/murilosalla-blip/fiap-ano02-fase01-cardioia), com a estrutura original da entrega.

**Documentação completa:** [Guia da Fase 1](document/fase1/README.md)

**Dados numéricos e variáveis:** [Preparação e justificativas](document/fase1/parte1_dados_numericos.md) e [dicionário das variáveis](document/fase1/parte1_dicionario_variaveis.md)

**Dados textuais:** [Fontes, contexto e aplicações de NLP](document/fase1/parte2_dados_textuais.md)

**Dados visuais:** [Curadoria, rastreabilidade e aplicações de visão computacional](document/fase1/parte3_dados_visuais.md)

**Documento submetido:** [Entrega original da Fase 1](document/fase1/cardioia_fase1_entrega_fiap.pdf)

### ▶️ Como executar a Fase 1

Antes dos comandos, seguir a [preparação comum do ambiente](#-como-executar-o-código).

Os dados finais da **Fase 1** já estão preparados e disponíveis nas pastas do projeto e nos links externos; não é necessário executar código para avaliá-los. Fornecemos os scripts para reprodução e rastreabilidade da preparação. Para reexecutá-los, utilizar o ambiente preparado acima e executar os comandos na raiz do repositório.

**Reproduzir o dataset numérico da Parte 1** — gera o CSV a partir da fonte bruta incluída no repositório:

```powershell
.\.venv\Scripts\python.exe src/fase1/preparar_dataset_numerico.py
.\.venv\Scripts\python.exe scripts/fase1/verificar_preservacao.py
```

Resultado esperado: CSV em `assets/fase1/dados/processed/heart_disease_cleveland.csv`, com **303 registros**, e conferência dos **223 itens inventariados no início da Fase 2**, incluindo os 181 do fechamento da Fase 1. Mantemos 212 arquivos nos destinos atuais e identificamos no histórico os 11 PDFs de aulas retirados; os dados e programas permanecem disponíveis. Os documentos das três modalidades estão no [guia da Fase 1](document/fase1/README.md).

**Reproduzir a amostra de imagens de ECG da Parte 3** — requer preparação manual antes de executar:

1. Consultar a [fonte do dataset](document/other/referencias/fase1/parte3/fonte_dataset.md), baixar a base bruta do Mendeley Data e extraí-la localmente.
2. Ajustar `RAW_DIR` em `src/fase1/preparar_amostra_ecg.py` para a pasta extraída.
3. Instalar Pillow e executar:

```powershell
.\.venv\Scripts\python.exe -m pip install -r config/fase1/requirements.txt
.\.venv\Scripts\python.exe src/fase1/preparar_amostra_ecg.py
```

Resultado esperado: **120 JPG**, distribuídos em quatro categorias, e manifesto em `document/other/referencias/fase1/parte3/manifesto_amostra.csv`. Essa reconstrução depende da fonte externa; para apenas avaliar, utilizar a amostra já entregue. Os dois TXT estão prontos em `assets/fase1/textos/` e podem ser lidos sem executar preparação.

## 🧠 Fase 2 — Machine Learning

Organizamos a entrega obrigatória da Fase 2 em duas partes independentes:

1. **Extração de sintomas:** preparamos dez relatos simulados completos em `.txt`, um mapa de conhecimento sintoma–doença em CSV e um extrator Python tolerante a maiúsculas, acentos e pontuação.
2. **Classificação textual de risco:** preparamos uma base simulada com 120 frases únicas e balanceadas, aplicamos TF-IDF e Regressão Logística e separamos treino e teste por cenário, com avaliação de desempenho e viés.

Também implementamos os dois desafios **Ir Além**:

- **Portal React + Vite:** autenticação simulada com token local, rotas protegidas, pacientes, agendamentos e dashboard, com testes automatizados;
- **Classificação visual de ECG:** baseline binário com 60 exames equilibrados e revisão ampliada com os 491 conteúdos únicos recuperados da mesma fonte pública, pré-processamento em escala de cinza e MLP Keras. Mantemos hashes distintos entre treino, validação e teste e documentamos a ausência de identificador confiável de paciente.

Como extensão adicional, preservamos o modelo tabular da base Heart Disease — Cleveland e sua aplicação Streamlit. Apresentamos as modalidades separadamente, pois utilizam fontes, pessoas e objetivos distintos.

**Aplicação principal:** [cardioia-fiap.streamlit.app](https://cardioia-fiap.streamlit.app/)

**Portal administrativo:** [julia-carvalho96.github.io/grupo-aura-cardioia-portal](https://julia-carvalho96.github.io/grupo-aura-cardioia-portal/)

**Repositório separado do portal:** [Julia-carvalho96/grupo-aura-cardioia-portal](https://github.com/Julia-carvalho96/grupo-aura-cardioia-portal)

**Documentação completa:** [Guia da Fase 2](document/fase2/README.md)

**Checklist do enunciado:** [Critérios e evidências](document/fase2/CHECKLIST_ENUNCIADO.md)

**Resultados reproduzíveis:** [Resultados dos experimentos](assets/fase2/resultados/README.md)

**Relatório de entrega:** [Relatório da Fase 2](document/fase2/RELATORIO_ENTREGA.md)

Resultados dos experimentos, apresentados no mesmo formato da entrega da Fase 2:

| Experimento | Amostra de teste | Resultado principal |
|---|---:|---:|
| NLP — TF-IDF + Regressão Logística | 24 frases | acurácia 100,0% |
| Tabular — Cleveland | 61 registros | ROC AUC 0,958 |
| Visual — MLP de ECG ampliada | 99 imagens | acurácia balanceada 74,5%; ROC AUC 0,824 |

> Os dados textuais são simulados e intencionalmente separáveis; por isso, 100% no teste não demonstra validade clínica. Na revisão visual, a acurácia simples foi 69,7%, diferente da acurácia balanceada de 74,5%; o recall da classe anormal foi 62,9%. Preservamos o teste e definimos o limiar somente na validação. Não validamos os modelos para uso assistencial.

**Documento submetido:** [Entrega original da Fase 2](document/fase2/CardioIA_Fase2_Documento_de_Submissao.pdf).

**Versão histórica:** [repositório da Fase 2](https://github.com/murilosalla-blip/fiap-ano02-fase02-cardioia).

**Vídeo da entrega:** [Fase 2 completa — YouTube não listado](https://youtu.be/qoKjl6oeotY), com NLP, portal React e MLP visual.

### ▶️ Como executar a Fase 2

Antes dos comandos, seguir a [preparação comum do ambiente](#-como-executar-o-código).

As aplicações públicas indicadas acima podem ser avaliadas sem usar o terminal.

Para reprodução técnica da entrega obrigatória de NLP, executar na raiz com o ambiente Python preparado:

```powershell
.\.venv\Scripts\python.exe -m pip install -r config/fase2/requirements.txt
.\.venv\Scripts\python.exe src/fase2/src/extrair_sintomas.py
.\.venv\Scripts\python.exe src/fase2/src/classificar_risco_texto.py
.\.venv\Scripts\python.exe src/fase2/tests/test_nlp.py
.\.venv\Scripts\python.exe src/fase2/tests/test_app.py
.\.venv\Scripts\python.exe -m streamlit run src/fase2/app.py
```

Resultado esperado: processamento dos **dez relatos**, treinamento e resultados textuais em `assets/fase2/resultados/nlp/`, testes concluídos e aplicação em [localhost:8501](http://localhost:8501). Utilizar exemplos fictícios para conferir extração, classificação e histórico temporário. Encerrar o servidor com **Ctrl+C**.

Para o portal React, executar em outro terminal, também na raiz:

```powershell
npm.cmd ci --prefix src/fase2/portal-cardioia
npm.cmd test --prefix src/fase2/portal-cardioia
npm.cmd run build --prefix src/fase2/portal-cardioia
npm.cmd run dev --prefix src/fase2/portal-cardioia
```

Abrir o endereço exibido pelo Vite. Utilizar um e-mail fictício em formato válido e senha de pelo menos seis caracteres. Conferir pacientes simulados, busca, agendamento e indicadores; não utilizar credenciais reais. Os sete testes e o build devem concluir.

Para o experimento visual, utilizar um ambiente separado com as versões de TensorFlow e Keras fixadas nos requisitos:

```powershell
python -m venv src/fase2/.venv
.\src\fase2\.venv\Scripts\python.exe -m pip install -r config/fase2/requirements-visual.txt
.\src\fase2\.venv\Scripts\python.exe src/fase2/tests/test_visual.py
.\src\fase2\.venv\Scripts\python.exe src/fase2/src/treinar_mlp_ecg.py
```

O baseline utiliza a amostra versionada da Fase 1 e gera resultados em `assets/fase2/resultados/visual/`. Para reproduzir a revisão ampliada com 491 conteúdos únicos, o treinamento tabular e os notebooks, seguir o [guia completo da Fase 2](document/fase2/README.md). Os quatro notebooks já incluem saídas para avaliação; novas execuções devem ser gravadas separadamente.

Os workflows do GitHub Actions verificam dados, testes, treinamentos, notebooks e build do portal. Preservamos as evidências dos resultados e suas limitações na documentação de cada experimento.

## 📡 Fase 3 — Monitoramento Contínuo: IoT na Saúde

Acrescentamos monitoramento IoT à evolução do CardioIA, com dados simulados independentes das bases clínicas anteriores. Implementamos as duas partes obrigatórias e os dois desafios Ir Além, com código, guias, testes e relatórios. Não é necessário comprar hardware nem executar os treinamentos das fases anteriores para avaliar esta fase.

### Parte 1 — Edge Computing

Utilizamos ESP32 no Wokwi, DHT22 para temperatura/umidade e botão para pulsos artificiais. Coletamos a cada cinco segundos simulados e mantemos uma fila FIFO de **2.000 leituras**, equivalente a **2h46min40s** nominais. A coleta continua offline; ao reconectar, recuperamos as pendências em ordem pelo Serial, conforme a alternativa prevista no enunciado.

A chave à esquerda representa offline e, à direita, online. O DHT22 conta como um sensor; o botão simula o segundo sinal, conforme o exemplo da atividade. A fila está em RAM e se perde após reinício. Ao lotar, preservamos as amostras antigas, descartamos a nova e contabilizamos perdas. SPIFFS e hardware físico são opcionais.

- **Simulação:** [Wokwi Edge — saída Serial](https://wokwi.com/projects/478054573982428161).
- **Código comentado e diagrama:** [firmware Edge](src/fase3/firmware/cardioia_edge/).
- **Relatório:** [Edge — duas páginas](document/fase3/CardioIA_Fase3_Relatorio_Edge.pdf), acima do mínimo de uma página.
- **Evidências:** [coleta offline, recuperação, fila cheia e reinício](document/other/fase3/evidencias/2026-10-24/RESULTADOS.md).

### Parte 2 — MQTT e dashboard Node-RED

Transmitimos pelo broker remoto `broker.hivemq.com:1883`. O consumidor Python grava em SQLite e confirma cada leitura após o commit; reenvios não duplicam a medição persistida. O Node-RED exibe gráfico de BPM, gauge de temperatura, umidade, histórico e alertas visuais.

Definimos entrada de alerta acima de **120 BPM** ou **30 °C** e retorno até **108 BPM** ou **28 °C**, com duas leituras atuais consecutivas. Medimos temperatura ambiente, não corporal; zero pulsos significa ausência de acionamentos do botão. Dados recuperados entram no histórico sem confirmar alertas do presente. Grafana é opcional e não foi utilizado.

- **Simulação:** [Wokwi MQTT — demonstração principal](https://wokwi.com/projects/478772789361460225).
- **Código:** [firmware MQTT](src/fase3/firmware/cardioia_mqtt/) e [consumidor Python](src/fase3/python/consumidor_mqtt.py).
- **Dashboard:** [export Node-RED](src/fase3/node-red/flows.json), [configuração](document/fase3/node-red/README.md) e [capturas](assets/fase3/evidencias/).
- **Relatório:** [MQTT/dashboard — quatro páginas](document/fase3/CardioIA_Fase3_Relatorio_MQTT_Dashboard.pdf), acima do mínimo de duas páginas.
- **Evidências:** [transmissão e recuperação MQTT](document/other/fase3/evidencias/2026-10-24/mqtt/RESULTADOS.md) e [sensores, alertas e recuperação no painel](document/other/fase3/evidencias/2026-10-27/reproducao/validacao_guiada/RESULTADOS.md).

Os dois Wokwi reutilizam o circuito, mas têm firmwares e transportes diferentes. A Parte 1 demonstra resiliência pelo Serial e dispensa serviços locais. A Parte 2 transmite MQTT real e alimenta o [painel local](http://127.0.0.1:1880/dashboard/monitoramento) após iniciar os serviços. Não é necessário executar ambos simultaneamente.

### Ir Além 1 — REST e e-mail automatizado

Implementamos cliente e API Python com envio por `POST /leituras`, consulta por `GET /leituras`, regras didáticas e e-mail automático simulado em `.eml`. Um novo episódio gera uma mensagem; reenvio e permanência no mesmo episódio não duplicam e-mails. A demonstração registra **cinco leituras e dois e-mails**, preservados após reinício.

- **Código:** [cliente](src/fase3/python/cliente_rest.py) e [serviço REST](src/fase3/python/servico_rest.py).
- **Execução e diagnóstico:** [guia REST](document/fase3/rest/README.md).
- **Relatório:** [REST/e-mail — duas páginas](document/fase3/CardioIA_Fase3_Relatorio_REST_Email.pdf), dentro do intervalo de uma a duas páginas.
- **Evidências:** [respostas HTTP, e-mails e persistência](document/other/fase3/evidencias/2026-10-26/rest/validacao_guiada/RESULTADOS.md).

O fluxo é uma simulação local: não utiliza SMTP, não envia e-mail externo e não interpreta temperatura ambiente como febre. Os sete testes REST conferem o funcionamento e os casos de falha.

### Ir Além 2 — IA em séries temporais e rede LIF

Comparamos regressão logística e rede recorrente LIF de **24 neurônios**, com pesos internos fixos e saída logística treinada. Geramos **240 sessões sintéticas de BPM**, separadas em **144/48/48** para treino/validação/teste antes de criar janelas. No mesmo teste de 48 sessões, o tradicional acertou **44** e o LIF **35**, com F1 macro **0,9165** e **0,7262**.

Discutimos desempenho, erros, representações diferentes, dados artificiais e incerteza. Não concluímos superioridade geral, validação clínica ou eficiência energética medida.

- **Código e notebook:** [experimento](src/fase3/neuromorfismo/experimento.py) e [notebook comentado e executado](src/fase3/notebooks/comparacao_temporal_lif.ipynb).
- **Reprodução:** [guia completo](document/fase3/neuromorfismo/README.md), com instalação, gráficos, notebook e nove testes.
- **Resultados:** [métricas, matrizes, previsões e divisão das sessões](assets/fase3/resultados/neuromorfismo/).
- **Relatório:** [comparação tradicional/LIF — duas páginas](document/fase3/CardioIA_Fase3_Relatorio_Neuromorfismo.pdf).
- **Vídeo:** [Ir Além 2 — YouTube não listado, 2min59s](https://youtu.be/-v9lWpZ_JJo), com resultados e análise crítica.
- **Conferência:** [gráficos, transcrição automática e acesso ao vídeo](document/other/fase3/evidencias/2026-11-01/video/RESULTADOS.md).

### Documentação e situação da entrega

O [guia passo a passo da Fase 3](document/fase3/README.md) reúne preparação, execução, resultados esperados e diagnóstico. A [matriz de requisitos](document/fase3/CHECKLIST_ENUNCIADO.md) relaciona as exigências às implementações e evidências. O [documento de submissão — seis páginas](document/fase3/CardioIA_Fase3_Documento_de_Submissao.pdf) concentra os acessos para avaliação.

As implementações, relatórios, testes e vídeo estão disponíveis. Restam a conferência do cadastro do grupo, das regras de upload e o envio confirmado na FIAP. Publicar no GitHub e no YouTube não substitui a submissão acadêmica. Os desafios são parte do escopo escolhido pelo grupo; não atribuímos pontuação adicional nem antecipamos nota.

### ▶️ Como executar a Fase 3

Seguir a sequência abaixo. O [guia passo a passo da Fase 3](document/fase3/README.md#como-reproduzir--preparação) explica cada ação desde abrir o PowerShell, com comandos completos, resultados esperados e solução de erros. Não é necessário executar os treinamentos das fases anteriores.

#### 1. Preparar o computador

- Instalar Git, Python 3.12 e Node.js 24 pelos links oficiais indicados no guia.
- Abrir um novo PowerShell e conferir as versões antes de continuar.
- Escolher uma pasta curta, baixar o repositório e entrar na pasta criada.
- Conferir que `README.md` e `src` existem nessa pasta.
- Criar `.venv`, conferir seu Python e instalar as dependências da Fase 3.
- **Avançar quando:** os comandos de instalação terminarem sem erro. Seguir os passos 1 a 6 da preparação no guia; não presumir que o ambiente já existe.

#### 2. Testar o circuito da Parte 1

- Abrir o [Wokwi Serial](https://wokwi.com/projects/478054573982428161) e clicar em Play.
- Mover a chave para a esquerda e aguardar pelo menos três coletas no Monitor Serial.
- Pressionar e soltar o botão verde e alterar a temperatura no DHT22.
- Mover a chave para a direita e conferir a saída das leituras acumuladas em ordem, com `transport: serial_demo`, até esvaziar a fila.
- Clicar em Stop ao terminar.
- **Resultado esperado:** a coleta continua offline e os dados acumulados aparecem após reconectar. Esta parte não alimenta o painel.

#### 3. Iniciar o painel da Parte 2

- No PowerShell, na raiz do projeto, selecionar o Python e iniciar os serviços, uma linha por vez:

```powershell
$env:CARDIOIA_PYTHON = (Resolve-Path .\.venv\Scripts\python.exe).Path
node scripts/fase3/iniciar_dashboard.js --com-consumidor
```

- Manter esse terminal aberto. O comando inicia painel e um consumidor; não iniciar outro consumidor junto.
- Aguardar aparecerem `Server now running` e `Started flows` no terminal. A linha inicial `Painel: ...` apenas informa o endereço; ela aparece antes de o serviço estar pronto. Depois abrir o [painel local](http://127.0.0.1:1880/dashboard/monitoramento).
- Abrir o [Wokwi MQTT](https://wokwi.com/projects/478772789361460225), clicar em Play e mover a chave para a direita.
- **Resultado esperado:** `# ack_confirmado` no Serial e avanço das leituras no painel. Se só houver `mqtt_publicacao=tentada`, conferir o consumidor conforme o guia.

#### 4. Conferir os sensores e alertas

- Pressionar e soltar o botão verde: seis acionamentos na mesma janela de cinco segundos simulados equivalem a aproximadamente 72 BPM. Segurar conta um único pulso.
- Obter mais de dez acionamentos por janela em duas coletas atuais consecutivas para conferir o alerta; depois reduzir para até 108 BPM por duas leituras e conferir o retorno.
- Clicar no DHT22 durante a simulação, ajustar para 31 °C e aguardar duas leituras atuais. Conferir temperatura e alerta no painel.
- Reduzir para 28 °C e aguardar duas leituras para conferir o retorno.
- **Resultado esperado:** pontos no gráfico, temperatura atualizada e eventos de entrada/retorno. Manter Wokwi e painel visíveis; o tempo simulado pode desacelerar em segundo plano.

#### 5. Testar a interrupção e encerrar o painel

- Mover a chave para a esquerda e aguardar pelo menos três novas coletas.
- Conferir a fila crescendo no Serial, mesmo sem conexão.
- Mover a chave à direita e acompanhar recuperação ordenada, confirmações e redução da fila.
- Conferir o histórico preservado no painel. Valores antigos podem ficar cinza, com indicação de falta de atualização.
- Clicar em Stop no Wokwi e pressionar Ctrl+C no PowerShell do painel.
- **Resultado esperado:** os dados recebidos ficam em SQLite; não apagar `.tools/runtime/` para repetir testes.

#### 6. Executar o Ir Além 1 — REST e e-mail

- Seguir os [nove passos do guia REST](document/fase3/rest/README.md).
- Iniciar o serviço no terminal A e verificar `/saude` no navegador.
- Abrir um terminal B na mesma pasta, executar a demonstração e consultar as cinco leituras.
- Abrir os dois arquivos de e-mail e conferir os motivos dos alertas.
- Reiniciar o serviço, consultar novamente e conferir a mesma sessão.
- Encerrar com Ctrl+C.
- **Resultado esperado:** cinco leituras únicas, dois e-mails locais e reenvio sem duplicação. A API mostra JSON; a raiz `/` não tem página e retorna “Rota inexistente”. Não há envio real de e-mails.

#### 7. Executar o Ir Além 2 — comparação tradicional e LIF

- Usar o PowerShell na raiz, com Python 3.12 e `.venv` preparado. Esta trilha dispensa Wokwi, broker e Node-RED.
- Instalar as dependências e executar, uma linha por vez:

```powershell
.\.venv\Scripts\python.exe -m pip install -r config/fase3/requirements-neuromorfismo.txt
.\.venv\Scripts\python.exe scripts/fase3/executar_neuromorfismo.py
```

- Esperar as linhas `tradicional` e `lif`. Na referência, o F1 macro foi 0,9165 e 0,7262; o LIF teve desempenho inferior neste conjunto sintético.
- Abrir `series.png`, `matrizes_confusao.png` e `atividade_lif.png` na pasta `.tools/runtime/fase3/neuromorfismo/`.
- Executar o notebook completo e abrir a versão de leitura:

```powershell
.\.venv\Scripts\python.exe scripts/fase3/executar_neuromorfismo.py --notebook
Invoke-Item .tools/runtime/fase3/neuromorfismo/comparacao_temporal_lif.html
```

- Seguir os [oito passos de execução e conferência](document/fase3/neuromorfismo/README.md), incluindo nove testes (seis dos modelos e três de exportação). Os programas terminam sozinhos; não há servidor para encerrar.
- A classificação compara regimes artificiais, sem diagnóstico ou medição de economia energética.

#### 8. Conferir a entrega e os próximos passos

- Marcar a lista de conferência no [guia da Fase 3](document/fase3/README.md) somente após observar cada resultado.
- Para verificações adicionais de contrato, fila e confirmações, seguir o [guia de testes](document/fase3/tests/README.md).
- Consultar os relatórios e as evidências pelo [índice da documentação](document/README.md).
- O **Ir Além 2 está implementado e testado localmente**. Concluímos a validação guiada e publicamos o vídeo; restam a conferência do cadastro do grupo e o envio na FIAP, acompanhados na [matriz de requisitos](document/fase3/CHECKLIST_ENUNCIADO.md#aceite-antes-da-submissão).

#### Se algum passo não funcionar

- **Executável `.venv` não encontrado:** voltar à criação do ambiente; conferir a raiz e a versão do Python.
- **`ModuleNotFoundError`:** instalar os requisitos da trilha com o mesmo executável `.venv` usado para rodar o código. Instalar no Python global não prepara automaticamente o ambiente virtual.
- **Porta ocupada:** encerrar com Ctrl+C a instância anterior do próprio serviço; não encerrar processos desconhecidos. Conferir a porta indicada no guia (8501 Streamlit, 1880 Node-RED, 8765 REST; React informa seu endereço).
- **REST retorna rota inexistente:** abrir `/saude` ou `/leituras`, não a raiz `/`. São respostas JSON, não painel gráfico.
- **MQTT não conecta:** conferir internet, acesso TCP 1883, serviço consumidor e Wokwi da Parte 2. Preservar a mensagem de erro; a disponibilidade do broker público é externa ao projeto.
- **Dependência ou download falhou:** não continuar o treinamento; guardar a saída e conferir conexão e requisitos. Os arquivos e resultados já entregues continuam disponíveis para inspeção.

Não apagar `.tools/runtime/` para resolver problemas: ali ficam as medições e os e-mails dos testes. Reexecuções de treinamento podem substituir resultados locais; utilizar uma cópia de avaliação separada para preservar o material entregue. Confirmar as instruções da revisão baixada, pois alterações ainda locais não aparecem em um novo clone público.

## 📁 Estrutura de pastas

Seguimos o [modelo oficial FIAP](https://github.com/agodoi/templateFiapVfinal). Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: mantemos as configurações específicas do GitHub e os workflows de verificação automática.

- <b>assets</b>: reunimos datasets, textos, imagens, resultados e capturas, organizados por fase.

- <b>config</b>: mantemos requisitos, contratos de dados e parâmetros de configuração do projeto.

- <b>document</b>: reunimos os guias e documentos de cada entrega. Na subpasta `other`, mantemos referências, estudos, auditorias e cópias históricas.

- <b>scripts</b>: mantemos scripts auxiliares de inicialização, migração e validação.

- <b>src</b>: organizamos o código-fonte desenvolvido ao longo das fases, incluindo firmware, aplicações, notebooks e testes.

- <b>README.md</b>: apresentamos o projeto, sua evolução e as instruções gerais de reprodução.

Os artefatos estão organizados dentro das pastas oficiais:

- `assets/fase1/dados/raw/` e `assets/fase1/dados/processed/`: fonte bruta e dataset numérico preparado.
- `assets/fase1/textos/` e `assets/fase1/imagens/ecg/`: corpus textual e 120 imagens de ECG.
- `assets/fase2/dados/` e `assets/fase2/resultados/`: dados e resultados da Fase 2.
- `assets/fase3/evidencias/`: capturas da simulação e do painel.
- `config/fase1/`, `config/fase2/` e `config/fase3/`: dependências e configurações de cada fase.
- `document/fase1/`, `document/fase2/` e `document/fase3/`: documentação principal, documentos anteriores submetidos e acompanhamento da entrega atual.
- `document/other/referencias/`: enunciados, fontes e materiais de aula separados por fase.
- `document/other/fase3/evidencias/`: registros e resultados dos testes de IoT.
- `document/other/historico/`: cópias das versões anteriores, preservadas como registros históricos.
- `src/fase1/` e `scripts/fase1/`: preparação dos dados e verificação da preservação.
- `src/fase2/`: aplicação Streamlit, modelos, notebooks e testes; portal em `src/fase2/portal-cardioia/`.
- `src/fase3/` e `scripts/fase3/`: firmware, consumidor MQTT, Node-RED, testes e inicialização do monitoramento.

O [índice da documentação](document/README.md) identifica os documentos principais e os [registros de organização](document/other/organizacao/README.md) explicam os caminhos anteriores. `.venv/`, `.tools/` e `node_modules/` são pastas locais geradas durante a execução e não fazem parte da entrega versionada.

## 🔧 Como executar o código

Esta preparação é comum às três fases. Depois, seguir “Como executar” dentro da fase desejada. Para a demonstração Edge no Wokwi, basta o navegador; as demais trilhas indicam as dependências necessárias.

**Pré-requisitos:** Git e Python **3.12**. Para as imagens, utilizamos Pillow. Para o portal React e o Node-RED, utilizamos Node.js **24** com npm. O Wokwi e o broker público exigem internet e acesso à porta TCP **1883**. Não é necessário comprar hardware.

### Preparar a máquina e conferir o terminal

Instalar Git, Python 3.12 e, somente para React ou Node-RED, Node.js 24 com npm. Abrir um **novo PowerShell** após a instalação e conferir:

```powershell
git --version
python --version
node --version
npm.cmd --version
```

Esperar Python `3.12.x` e Node `v24.x`. Se `python` não for encontrado ou apontar para outra versão, conferir `py -3.12 --version` e usar `py -3.12` apenas para criar o ambiente. Se nenhum funcionar, instalar Python 3.12 antes de continuar. Os comandos seguintes utilizam o Python do ambiente criado, sem depender da ativação. `npm.cmd` evita o bloqueio de `npm.ps1` pela política do PowerShell.

### Obter o código e criar o ambiente

No Windows, escolher uma pasta curta, por exemplo `C:\projetos`, com permissão de escrita. Evitar pastas muito aninhadas: a instalação limpa revelou falha de caminho longo em uma dependência de Jupyter. Se aparecer `No such file or directory` acompanhado de aviso sobre `Long Path`, criar uma nova cópia e um novo ambiente em caminho curto, preservando a anterior. Não mover um ambiente virtual existente.

Executar o clone **na pasta onde se deseja guardar o projeto**; o comando cria a subpasta abaixo. Não clonar novamente dentro de uma cópia existente:


```powershell
git clone https://github.com/murilosalla-blip/fiap-ano02-fase03-cardioia.git
Set-Location -LiteralPath './fiap-ano02-fase03-cardioia'
python -m venv .venv
```

Se a cópia já existe, abrir o PowerShell nessa pasta e conferir `Test-Path .\README.md` e `Test-Path .\src`: ambos devem retornar `True`. Não utilizar o caminho pessoal de outro integrante. Se `.venv` ainda não existe, executar a criação acima; caso exista, conferir `.\.venv\Scripts\python.exe --version` antes de seguir.

**Como acompanhar os passos:** executar um comando por vez e aguardar sua conclusão. Instalação bem-sucedida retorna ao prompt sem erro; avisos de atualização do pip não exigem atualização. Se aparecer erro, corrigir antes de avançar. Comandos de servidor permanecem ocupados: manter esse terminal aberto e usar outro, na mesma raiz, para consultas. Não digitar comandos Python no editor ou no Monitor Serial do Wokwi.

**Escolher a trilha:** Fase 1 para dados; Fase 2 para NLP, Streamlit e extras; Fase 3 Parte 1 somente no navegador; Parte 2 para MQTT/painel; Ir Além 1 para HTTP local; Ir Além 2 para comparar modelos de séries temporais. Não é necessário executar fases ou treinamentos anteriores para testar IoT ou REST.

Utilizamos o executável do ambiente virtual sem precisar ativá-lo ou alterar a política de execução do PowerShell. No Linux/macOS, criar com `python3.12 -m venv .venv` e substituir `.venv/Scripts/python.exe` por `.venv/bin/python`, nas pastas correspondentes. Usar `cd` em lugar de `Set-Location` e `npm` em lugar de `npm.cmd` no Linux/macOS. Cada guia indica as demais diferenças de terminal; os testes locais desta revisão foram feitos no Windows, não nos três sistemas.

## 🗃 Histórico de lançamentos

- **01/11/2026:** publicamos o vídeo do Ir Além 2 e consolidamos a documentação e os acessos por fase; mantivemos o planejamento como material interno.
- **31/10/2026:** revisamos os requisitos e preparamos o documento consolidado de submissão.
- **28/10/2026:** concluímos a validação guiada tradicional/LIF e a revisão técnica dos quatro relatórios.
- **27/10/2026:** detalhamos a reprodução, validamos IoT em ambiente novo e implementamos a comparação temporal com LIF.
- **26/10/2026:** concluímos os relatórios obrigatórios e a validação REST com e-mail simulado.
- **25/10/2026:** preservamos as versões históricas das Fases 1 e 2 e organizamos o repositório no modelo FIAP.
- **24/10/2026:** validamos sensores, fila offline, MQTT, persistência e dashboard Node-RED.
- **07/10/2026:** concluímos a documentação e o vídeo da Fase 2, incluindo os dois desafios.
- **14/09/2026:** desenvolvemos os modelos, aplicações e experimentos de Machine Learning da Fase 2.
- **21/08/2026:** estruturamos as bases numérica, textual e visual da Fase 1.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
