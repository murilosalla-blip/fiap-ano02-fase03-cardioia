# Matriz de requisitos da Fase 3

Relacionamos os requisitos do enunciado às implementações, entregáveis e evidências. As Partes 1 e 2 e os dois desafios estão implementados e documentados.

## Critérios da atividade obrigatória — 10 pontos

| Critério | Pontos | Implementação e comprovação |
|---|---:|---|
| Leitura de sensores | 2 | ESP32 com DHT22 e botão de pulsos, conforme o exemplo do enunciado; [firmware](../../src/fase3/firmware/) e testes visuais registrados |
| Resiliência offline | 2 | Coleta contínua, fila FIFO de 2.000 amostras, recuperação ordenada e perdas contabilizadas; [cenários Edge](../other/fase3/evidencias/2026-10-24/RESULTADOS.md) |
| MQTT e broker | 2 | Publicação real no broker remoto, gravação SQLite, ACK e reenvio/deduplicação; [validação MQTT](../other/fase3/evidencias/2026-10-24/mqtt/RESULTADOS.md) |
| Dashboard e alertas automáticos | 2 | Node-RED com gráfico, gauge e alertas de pulsos/temperatura; [validação guiada](../other/fase3/evidencias/2026-10-27/reproducao/validacao_guiada/RESULTADOS.md) |
| Documentação clara | 2 | C++ comentado, [reprodução sequencial](README.md), relatórios e evidências; [índice dos documentos](../README.md) |

SPIFFS não integra a pontuação obrigatória. Os dois Ir Além foram incluídos por decisão do grupo; não constam nessa distribuição de dez pontos.

## Parte 1 — Edge Computing

| Exigência | Entrega e resultado |
|---|---|
| ESP32 e dois sensores distintos | [Wokwi Edge](https://wokwi.com/projects/478054573982428161), DHT22 e botão de pulsos. Contamos temperatura/umidade como um sensor; a chave não é sensor |
| Leitura periódica do DHT22 | Coleta a cada cinco segundos simulados, com validade do sensor e valores ausentes indicados como `null` |
| Conectividade booleana | Chave controla `connected`; coleta continua offline |
| Armazenamento local limitado | 2.000 amostras em RAM; 2h46min40s nominais. Preservamos histórico retido e descartamos novas leituras ao lotar, com contador de perdas |
| Sincronização ao reconectar | Saída Serial das pendências em ordem e liberação após escrita local completa, sem alegar persistência remota nesta parte |
| C++ comentado | [Código, núcleo e diagrama](../../src/fase3/firmware/cardioia_edge/) |
| Relatório mínimo de uma página | [Relatório Edge — duas páginas](CardioIA_Fase3_Relatorio_Edge.pdf), com fluxo, resiliência, limites e reprodução |

**Fundamentação e limites:** a Parte 2 do enunciado completo exemplifica o botão de pressão para simular batimentos. SPIFFS é opcional, e a atividade admite a alternativa Serial no simulador. Não criamos arquivo SPIFFS: retiramos da fila as amostras já escritas. A resiliência cobre conectividade enquanto o dispositivo permanece ligado; a RAM se perde ao reiniciar. Conferimos fila cheia com capacidade temporariamente reduzida e restauramos as 2.000 posições; não alegamos um ensaio contínuo de 2.000 coletas.

## Parte 2 — MQTT e visualização

| Exigência | Entrega e resultado |
|---|---|
| ESP32 envia dados à nuvem via MQTT | [Wokwi MQTT](https://wokwi.com/projects/478772789361460225) e broker remoto `broker.hivemq.com:1883` |
| Código ESP32 | [Firmware MQTT e diagrama](../../src/fase3/firmware/cardioia_mqtt/) |
| Dashboard Node-RED em tempo real | Subscrição de telemetria, estado e ACK; gráfico de BPM e gauge de temperatura ambiente |
| Alertas visuais automáticos | Pulsos >120 BPM ou ambiente >30 °C; duas leituras atuais consecutivas. Retorno até 108 BPM ou 28 °C, com a mesma confirmação |
| Prints ou export do dashboard | Entregamos ambos: [flows.json](../../src/fase3/node-red/flows.json) e [capturas](../../assets/fase3/evidencias/) |
| Relatório mínimo de duas páginas | [Relatório MQTT/dashboard — quatro páginas](CardioIA_Fase3_Relatorio_MQTT_Dashboard.pdf), com comunicação, tópicos, configuração e execução |

**Configuração e limites:** o broker é remoto; consumidor, SQLite e Node-RED executam localmente. O [guia Node-RED](node-red/README.md) explica os arquivos auxiliares necessários ao export. Grafana é opcional e não foi utilizado. Leituras recuperadas entram no histórico sem confirmar alertas do presente. Broker público sem autenticação/TLS é utilizado somente com dados fictícios.

## Ir Além 1 — REST e e-mail

| Entregável ou critério | Implementação e evidência |
|---|---|
| Cliente Python para envio e recebimento REST | [cliente_rest.py](../../src/fase3/python/cliente_rest.py): `POST /leituras`, `GET /leituras`, timeout e tratamento de erros |
| Lógica de verificação de risco | [servico_rest.py](../../src/fase3/python/servico_rest.py): >120 BPM artificial ou >30 °C ambiente; retorno até 108 BPM ou 28 °C; controle de episódios |
| Simulação de e-mail automatizado | Novo motivo gera `.eml` automaticamente, com remetente/destinatário fictícios, assunto e motivos. Permanência no episódio e reenvio não duplicam mensagens |
| Relatório de uma a duas páginas | [Relatório REST/e-mail — duas páginas](CardioIA_Fase3_Relatorio_REST_Email.pdf) |
| Clareza e organização | [Guia passo a passo](rest/README.md), contratos em `config/fase3/`, código e testes em `src/fase3/`, saídas locais ignoradas em `.tools/runtime/` |
| Funcionamento demonstrado | [Validação com cinco leituras e dois e-mails](../other/fase3/evidencias/2026-10-26/rest/validacao_guiada/RESULTADOS.md), persistência após reinício e sete testes HTTP |

**Escopo:** simulamos os e-mails em arquivos `.eml`. Aplicamos limites aos pulsos artificiais e à temperatura ambiente, com controle de episódios para evitar mensagens repetidas.

## Ir Além 2 — IA temporal e LIF

| Entregável ou critério | Implementação e evidência |
|---|---|
| Modelos funcionais | [Experimento Python](../../src/fase3/neuromorfismo/experimento.py): regressão logística e rede recorrente LIF de 24 neurônios, pesos internos fixos e leitura logística treinada |
| Comparação clara | Mesmas 48 sessões de teste; 44/48 acertos no tradicional e 35/48 no LIF. [Métricas, matrizes, previsões e divisões](../../assets/fase3/resultados/neuromorfismo/) |
| Notebook comentado e organizado | [Notebook executado](../../src/fase3/notebooks/comparacao_temporal_lif.ipynb), com dados, divisão, modelos, resultados, análise crítica e referências |
| Código e README públicos | Código, dependências e [guia de reprodução](neuromorfismo/README.md) disponíveis no repositório |
| Relatório comparativo de duas páginas | [Relatório tradicional/LIF — duas páginas](CardioIA_Fase3_Relatorio_Neuromorfismo.pdf) |
| Vídeo até quatro minutos e análise crítica | [YouTube não listado](https://youtu.be/-v9lWpZ_JJo), vinculado ao README raiz |

**Protocolo e limites:** utilizamos séries sintéticas de BPM, sem pacientes ou ECG. Separamos 144/48/48 sessões antes das janelas; normalização no treino e seleção de parâmetros na validação. O teste não ajusta o modelo. Discutimos representações diferentes, uma semente, incerteza e ausência de medição energética/validação clínica.

## Fontes e registros

- [Enunciado e materiais de referência](../other/referencias/README.md).
- [Reprodução em cópia nova e validação guiada IoT](../other/fase3/evidencias/2026-10-27/reproducao/RESULTADOS.md).
- [Guia de testes](tests/README.md), com contratos, persistência, modelos, núcleo C++ e validadores dos registros preservados.
