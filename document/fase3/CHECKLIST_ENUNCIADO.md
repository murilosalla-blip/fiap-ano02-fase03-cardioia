# Matriz de requisitos da Fase 3

Relacionamos os requisitos do enunciado às implementações, entregáveis e evidências. As Partes 1 e 2 e os dois desafios estão implementados e documentados. O fechamento acadêmico permanece separado da publicação no GitHub e no YouTube; não antecipamos nota.

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
| ESP32 envia dados à nuvem via MQTT | [Wokwi MQTT](https://wokwi.com/projects/478772789361460225) e broker remoto `broker.hivemq.com:1883`; HiveMQ Cloud é um exemplo de produto, não uma plataforma específica obrigatória |
| Código ESP32 | [Firmware MQTT e diagrama](../../src/fase3/firmware/cardioia_mqtt/) |
| Dashboard Node-RED em tempo real | Subscrição de telemetria, estado e ACK; gráfico de BPM e gauge de temperatura ambiente |
| Alertas visuais automáticos | Pulsos >120 BPM ou ambiente >30 °C; duas leituras atuais consecutivas. Retorno até 108 BPM ou 28 °C, com a mesma confirmação |
| Prints ou export do dashboard | Entregamos ambos: [flows.json](../../src/fase3/node-red/flows.json) e [capturas](../../assets/fase3/evidencias/) |
| Relatório mínimo de duas páginas | [Relatório MQTT/dashboard — quatro páginas](CardioIA_Fase3_Relatorio_MQTT_Dashboard.pdf), com comunicação, tópicos, configuração e execução |

**Configuração e limites:** o broker é remoto; consumidor, SQLite e Node-RED executam localmente. O [guia Node-RED](node-red/README.md) explica os arquivos auxiliares necessários ao export. Grafana é opcional e não foi utilizado. Os limites dos alertas são definidos pelo grupo; 38 °C é exemplo, não exigência de temperatura corporal. Leituras recuperadas entram no histórico sem confirmar alertas do presente. Broker público sem autenticação/TLS é utilizado somente com dados fictícios.

## Ir Além 1 — REST e e-mail

| Entregável ou critério | Implementação e evidência |
|---|---|
| Cliente Python para envio e recebimento REST | [cliente_rest.py](../../src/fase3/python/cliente_rest.py): `POST /leituras`, `GET /leituras`, timeout e tratamento de erros |
| Lógica de verificação de risco | [servico_rest.py](../../src/fase3/python/servico_rest.py): >120 BPM artificial ou >30 °C ambiente; retorno até 108 BPM ou 28 °C; controle de episódios |
| Simulação de e-mail automatizado | Novo motivo gera `.eml` automaticamente, com remetente/destinatário fictícios, assunto e motivos. Permanência no episódio e reenvio não duplicam mensagens |
| Relatório de uma a duas páginas | [Relatório REST/e-mail — duas páginas](CardioIA_Fase3_Relatorio_REST_Email.pdf) |
| Clareza e organização | [Guia passo a passo](rest/README.md), contratos em `config/fase3/`, código e testes em `src/fase3/`, saídas locais ignoradas em `.tools/runtime/` |
| Funcionamento demonstrado | [Validação com cinco leituras e dois e-mails](../other/fase3/evidencias/2026-10-26/rest/validacao_guiada/RESULTADOS.md), persistência após reinício e sete testes HTTP |

**Escopo:** o enunciado solicita simulação de e-mail, portanto não exigimos SMTP ou recebimento em caixa real. Taquicardia, febre e ausência de movimento são exemplos de riscos, não três detecções cumulativas obrigatórias. Nossas regras são didáticas: temperatura ambiente não é febre. O desafio não exige serviço externo, interface gráfica de RPA ou encaminhamento automático MQTT → REST.

## Ir Além 2 — IA temporal e LIF

| Entregável ou critério | Implementação e evidência |
|---|---|
| Modelos funcionais | [Experimento Python](../../src/fase3/neuromorfismo/experimento.py): regressão logística e rede recorrente LIF de 24 neurônios, pesos internos fixos e leitura logística treinada |
| Comparação clara | Mesmas 48 sessões de teste; 44/48 acertos no tradicional e 35/48 no LIF. [Métricas, matrizes, previsões e divisões](../../assets/fase3/resultados/neuromorfismo/) |
| Notebook comentado e organizado | [Notebook executado](../../src/fase3/notebooks/comparacao_temporal_lif.ipynb), com dados, divisão, modelos, resultados, análise crítica e referências |
| Código e README públicos | Código, dependências e [guia de reprodução](neuromorfismo/README.md) disponíveis no repositório |
| Relatório comparativo de duas páginas | [Relatório tradicional/LIF — duas páginas](CardioIA_Fase3_Relatorio_Neuromorfismo.pdf) |
| Vídeo até quatro minutos e análise crítica | [YouTube não listado — 2min59s](https://youtu.be/-v9lWpZ_JJo), vinculado ao README raiz; [publicação e conferência da transcrição](../other/fase3/evidencias/2026-11-01/video/RESULTADOS.md) |

**Protocolo e limites:** utilizamos séries sintéticas de BPM, sem pacientes ou ECG. Separamos 144/48/48 sessões antes das janelas; normalização no treino e seleção de parâmetros na validação. O teste não ajusta o modelo. Discutimos representações diferentes, uma semente, incerteza e ausência de medição energética/validação clínica. O enunciado permite LIF ou FHN, sem exigir os dois ou superioridade neuromórfica. Conferimos nove testes dos modelos/exportação e o conteúdo narrado por transcrição automática, sujeita a erros de reconhecimento; não a apresentamos como escuta integral.

## Aceite antes da submissão

- [x] Implementamos e validamos sensores, resiliência, MQTT, dashboard e alertas.
- [x] Entregamos código, diagramas, export e capturas, com execução documentada.
- [x] Conferimos relatórios obrigatórios com duas e quatro páginas.
- [x] Implementamos e validamos REST/e-mail e entregamos relatório de duas páginas.
- [x] Executamos a comparação tradicional/LIF, entregamos notebook, resultados e relatório de duas páginas.
- [x] Publicamos o vídeo não listado e conferimos duração, reprodução sem login, gráficos, números e transcrição automática.
- [x] Preservamos as entregas e links essenciais das fases anteriores.
- [x] Conferimos os três integrantes e RMs nos documentos.
- [ ] Conferir o cadastro efetivo dos integrantes no grupo da plataforma FIAP.
- [ ] Conferir formatos, tamanho e campos aceitos no upload.
- [ ] Publicar a revisão documental final e anexar o arquivo correto na atividade.
- [ ] Confirmar o envio, baixar/reabrir o conteúdo e guardar o comprovante.

O [documento de submissão](CardioIA_Fase3_Documento_de_Submissao.pdf) reúne os acessos para avaliação; não substitui os quatro relatórios específicos. O enunciado informa grupo de um a cinco integrantes e prazo de 04/11/2026 às 23h59; confirmar as regras efetivas na plataforma. Até três dias de atraso há limitação de nota conforme a orientação fornecida. Não registramos submissão ou avaliação como concluída sem confirmação da FIAP.

## Fontes e registros

- [Enunciado e materiais de referência](../other/referencias/README.md).
- [Reprodução em cópia nova e validação guiada IoT](../other/fase3/evidencias/2026-10-27/reproducao/RESULTADOS.md).
- [Revisão técnica dos documentos e acessos](../other/fase3/evidencias/2026-10-28/REVISAO_ENTREGA.md).
- [Guia de testes](tests/README.md), com contratos, persistência, modelos, núcleo C++ e validadores dos registros preservados.

Os registros datados documentam o que foi executado em cada revisão. Reexecutar validadores desses registros não equivale a uma nova sessão visual autônoma no Wokwi. O planejamento do grupo permanece em material interno local.
