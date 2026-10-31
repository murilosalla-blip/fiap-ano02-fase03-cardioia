# Fase 3 — requisitos, evidências e pendências

Acompanhamos separadamente implementação, teste, documentação e submissão. Reavaliamos este checklist em **28/10/2026**, com os textos fornecidos, o enunciado Word arquivado e suas duas imagens. O prazo informado é **04/11/2026, às 23h59**. Os documentos e as evidências de testes abaixo não representam submissão concluída.

## Critérios da atividade obrigatória — 10 pontos

| Critério do enunciado | Pontos | Como avaliar e localizar | Situação |
|---|---:|---|---|
| Leitura de sensores | 2 | ESP32 com DHT22 (um sensor) e botão de pulsos (segunda entrada simulada); código comentado em `src/fase3/firmware/`; projetos públicos identificados no [guia](README.md) | Implementamos e validamos no Wokwi |
| Resiliência offline | 2 | Chave booleana, coleta offline, fila FIFO de 2.000 amostras, sincronização e perdas contabilizadas; [resultados Edge](../other/fase3/evidencias/2026-10-24/RESULTADOS.md) | Validamos recuperação, limite, botão segurado e reinício; documentamos volatilidade da RAM |
| MQTT e broker | 2 | Firmware `cardioia_mqtt`, broker real, consumidor SQLite e ACK; [resultados MQTT](../other/fase3/evidencias/2026-10-24/mqtt/RESULTADOS.md) | Validamos transmissão, persistência, reenvio e recuperação |
| Dashboard e alertas | 2 | [Export Node-RED](../../src/fase3/node-red/flows.json), gráfico de BPM, gauge ambiental e alertas; [capturas](../../assets/fase3/evidencias/) e [validação guiada](../other/fase3/evidencias/2026-10-24/dashboard/validacao_guiada/RESULTADOS.md) | Validamos gráfico, temperatura, entrada e retorno dos alertas e estabilidade |
| Documentação clara: código e relatórios | 2 | README e guias de execução, C++ comentado, relatório Edge **≥1 página** e relatório MQTT/dashboard **≥2 páginas** | Produzimos [Edge: duas páginas](CardioIA_Fase3_Relatorio_Edge.pdf) e [MQTT/dashboard: quatro páginas](CardioIA_Fase3_Relatorio_MQTT_Dashboard.pdf); conferimos paginação e conteúdo; concluímos a revisão técnica em 28/10/2026 |

Não atribuímos nota antecipada a esta matriz. A avaliação pertence à FIAP; a implementação testada não dispensa os relatórios ou a entrega na plataforma.

## Conferência detalhada dos artefatos

| Requisito | Entrega | Evidência prevista | Estado |
|---|---:|---|---|
| ESP32 no Wokwi e dois sensores distintos, incluindo DHT22 | 1 | Sketch, diagrama e projeto público | Compilamos, conferimos no simulador e concluímos a revisão da primeira entrega |
| Coleta periódica e conectividade booleana | 1 | Firmware e demonstração Serial | Conferimos no Wokwi e salvamos registros em `document/other/fase3/evidencias/` |
| Resiliência offline e armazenamento limitado | 1–2 | Fila, testes e cenário de recuperação | Testamos o núcleo C++ e conferimos no Wokwi recuperação Serial, fila cheia, botão segurado e reinício; também implementamos MQTT, confirmamos reenvio e recuperação após reiniciar o consumidor |
| C++ comentado e link Wokwi | 1 | `src/fase3/firmware/cardioia_edge/` e https://wokwi.com/projects/478054573982428161 | Comentamos o código, publicamos o link e reorganizamos o circuito durante nossa revisão |
| Relatório Edge mínimo uma página | 6 | [Relatório Edge](CardioIA_Fase3_Relatorio_Edge.pdf) | Produzimos duas páginas e conferimos a renderização; revisão técnica concluída em 28/10/2026 |
| Transmissão MQTT e broker | 2 | Firmware compilado, consumidor, eventos de rede e projeto https://wokwi.com/projects/478772789361460225 | Confirmamos a troca real do ESP32 pelo broker, a confirmação após persistência e a recuperação após reiniciar o consumidor; também conferimos falha controlada do endpoint, recuperação ordenada e retorno à fila vazia |
| Dashboard Node-RED com gráfico, gauge e alerta | 3 | `src/fase3/node-red/flows.json` e `document/other/fase3/evidencias/2026-10-24/dashboard/` | Implementamos e testamos regras, rede e recebimento do ESP32; concluímos a revisão visual guiada com entrada e retorno dos dois alertas |
| Relatório MQTT/dashboard mínimo duas páginas | 6 | [Relatório MQTT/dashboard](CardioIA_Fase3_Relatorio_MQTT_Dashboard.pdf) | Produzimos quatro páginas e conferimos a renderização; revisão técnica concluída em 28/10/2026 |
| Ir Além 1 cliente REST envia e recebe | 4 | [Guia e evidência REST](rest/README.md) | Implementamos, testamos e concluímos a validação guiada com consulta após reinício |
| Ir Além 1 regras de risco e e-mail simulado | 4 | Código, sete testes e demonstração de dois e-mails locais | Conferimos os dois e-mails na validação guiada |
| Ir Além 1 relatório de uma a duas páginas | 4 | [Relatório de duas páginas](CardioIA_Fase3_Relatorio_REST_Email.pdf) | Produzimos e conferimos a renderização; revisão técnica concluída em 28/10/2026 |
| Ir Além 2 classificador tradicional e LIF/FHN | 5 | [Notebook executado](../../src/fase3/notebooks/comparacao_temporal_lif.ipynb) e [resultados](../../assets/fase3/resultados/neuromorfismo/) | Implementamos e executamos tradicional/LIF em ambiente novo; validação guiada concluída em 28/10/2026; nove testes locais aprovados após conferir a exportação |
| Ir Além 2 repositório público, código e README | 5–6 | Código da comparação, notebook e reprodução | O repositório já é público; código, notebook executado, resultados e guia acompanham esta revisão |
| Ir Além 2 relatório comparativo de duas páginas | 5 | [Relatório comparativo](CardioIA_Fase3_Relatorio_Neuromorfismo.pdf) | Produzimos duas páginas e conferimos a renderização; revisão técnica concluída em 28/10/2026 |
| Ir Além 2 vídeo até quatro minutos não listado | 5 | YouTube e link README | Ainda precisamos concluir |
| Clareza, organização e revisão de evidências | Todas | Roteiro e pacote final | Estamos acompanhando as evidências |

SPIFFS e hardware físico não são obrigatórios segundo o enunciado fornecido; Grafana é opcional. A implementação Serial da primeira entrega não satisfaz, sozinha, a Parte 2 de MQTT.

## Exigências, exemplos e escolhas do grupo

- **Obrigatórios:** dois sensores/entradas distintos, incluindo DHT22; coleta periódica e conectividade booleana; armazenamento limitado na ordem de milhares de amostras, com estratégia explícita; sincronização; código comentado e link Wokwi; MQTT com broker; Node-RED com gráfico, gauge e alerta; relatórios com os mínimos de páginas.
- **Opcionais:** SPIFFS no simulador, hardware físico, microSD e Grafana. Não apresentamos SPIFFS como realizado.
- **Escolhas da implementação:** cinco segundos simulados por coleta, 2.000 posições, descarte da amostra nova quando a fila enche, reenvio em três segundos, dado atual por 15 segundos reais, histerese e confirmação em duas janelas. Sete segundos no teste de botão segurado foi uma duração de ensaio, não um critério da FIAP.
- **Limites de alerta:** >120 BPM para pulsos artificiais e >30 °C para temperatura ambiente. O >38 °C citado no enunciado é exemplo, não obrigação de medir temperatura corporal. Zero pulsos indica ausência de acionamentos, não ausência de atividade cardíaca.
- **Ir Além 1:** o cliente Python precisa **enviar e receber** por REST, verificar risco e simular e-mail. O endpoint de consulta do painel não satisfaz sozinho esse requisito. O relatório deve ter **uma a duas páginas**.
- **Ir Além 2:** classificador tradicional comparado a LIF ou FHN em séries temporais, notebook comentado, código e README públicos, relatório de **duas páginas** e vídeo de **até quatro minutos**, não listado no YouTube, com link no README raiz. Ainda não temos esse vídeo; o link da Fase 2 não o substitui.

Mantemos os dois desafios no escopo por decisão do grupo, seguindo a Fase 2. Eles não constam na distribuição dos dez pontos acima; não afirmamos bonificação nem obrigação geral não expressa no enunciado.

## Revisão específica da Parte 1 — 31/10/2026

Reavaliamos a primeira entrega requisito por requisito, com o texto da atividade, o enunciado completo arquivado, o firmware `cardioia_edge`, seu diagrama, o relatório Edge e os registros de validação. Não realizamos uma nova sessão visual no Wokwi nesta revisão; reexecutamos a conferência automatizada dos registros preservados.

- **ESP32 e dois sensores distintos:** utilizamos DHT22 para temperatura/umidade e botão para simular pulsos. Contamos o DHT22 como um único sensor. O trecho isolado da Parte 1 não exemplifica o botão, mas a Parte 2 do enunciado completo cita expressamente um “botão de pressão, que você aperta x vezes por minuto” para simular batimentos. Essa é a fundamentação da segunda entrada escolhida; a chave de conectividade não conta como sensor.
- **Leitura periódica do DHT22:** coletamos a cada 5.000 ms simulados. Validamos temperatura e umidade; leituras inválidas são indicadas por `dht_valid=false` e valores `null` na saída, sem inventar medições.
- **Conectividade booleana:** a chave em GPIO 27 controla `bool connected`. A posição offline impede o escoamento, mas não interrompe a coleta.
- **Armazenamento local limitado:** mantemos 2.000 amostras em fila circular RAM. No ESP32 validado, registramos 40 bytes por amostra e 80.016 bytes para a fila completa. A cinco segundos por amostra, a cobertura nominal é de 2 h 46 min 40 s simulados. Priorizamos o histórico já retido para reconstruir a sequência durante interrupções no acompanhamento; ao lotar, descartamos novas amostras e contabilizamos as perdas. Essa política é demonstrativa e não equivale a uma garantia de monitoramento clínico.
- **Sincronização ao reconectar:** enviamos as pendências antigas em ordem no Monitor Serial, com `transport=serial_demo`, e removemos cada uma somente após a escrita local completa. Utilizamos `Serial.write` seguido de `Serial.println()` para produzir a linha JSON: é a demonstração Serial solicitada, sem alegar transmissão real à nuvem nesta parte.
- **SPIFFS opcional e remoção após envio:** não implementamos arquivo SPIFFS; utilizamos a alternativa demonstrativa admitida para o simulador. A operação equivalente de liberar armazenamento ocorre ao retirar da fila a amostra já escrita. Não há arquivo local a apagar. A fila é volátil e cobre desconexão enquanto o dispositivo permanece ligado; reinício ou encerramento da simulação perde as pendências.
- **Entregáveis:** disponibilizamos o [Wokwi Edge](https://wokwi.com/projects/478054573982428161), o [C++ comentado e diagrama](../../src/fase3/firmware/cardioia_edge/) e o [relatório Edge de duas páginas](CardioIA_Fase3_Relatorio_Edge.pdf), acima do mínimo de uma página, com fluxo, estratégia, limites e reprodução.
- **Evidência conferida nesta revisão:** executamos `scripts/fase3/validar_cenarios_edge.py`; aprovamos os registros de fila cheia, recuperação ordenada, perdas, pulso único, reinício e restauração da capacidade de 2.000. O ensaio de fila cheia usa três posições temporárias para tornar o teste viável; não afirmamos um ensaio contínuo de 2.000 coletas.

Concluímos que a Parte 1 possui implementação, documentação e evidências para os requisitos descritos, considerando a alternativa Serial e o exemplo de pulsos do enunciado completo. MQTT real, dashboard e reflexão sobre segurança/eficiência integram a revisão das demais partes; esta conclusão não representa uma nota atribuída nem submissão confirmada.

## Revisão específica da Parte 2 — 31/10/2026

Conferimos o firmware `cardioia_mqtt`, o fluxo Node-RED, as regras do painel, as capturas, o relatório MQTT/dashboard e os registros preservados de transmissão e validação guiada. Nesta revisão, não iniciamos outra simulação nem um novo ensaio pelo broker; reexecutamos os testes do painel e a conferência dos registros MQTT.

- **ESP32 → nuvem via MQTT:** utilizamos Wi-Fi `Wokwi-GUEST` e o broker remoto `broker.hivemq.com:1883`, com publicação real no tópico de telemetria. HiveMQ Cloud é um exemplo no enunciado, não uma exigência de produto ou plano específico. O broker público pela internet atende ao transporte remoto; consumidor, SQLite e Node-RED executam no computador local. Não afirmamos que o banco ou o painel estejam hospedados na nuvem.
- **Dashboard Node-RED em tempo real:** o fluxo assina telemetria, estado e ACK. A cada leitura recebida, atualizamos os indicadores; o dispositivo coleta a cada cinco segundos simulados. O relógio real pode divergir no Wokwi. Distinguimos conexão MQTT de atualidade da leitura e sinalizamos dados sem atualização, sem substituí-los por zeros.
- **Gráfico de sinal escolhido:** apresentamos BPM calculado dos acionamentos do botão, com histórico por sequência, limite didático e identificação das amostras recuperadas. O DHT22 fornece temperatura e umidade, e o botão simula o outro sinal conforme o exemplo do exercício.
- **Gauge de outro parâmetro:** apresentamos temperatura ambiente simulada em graus Celsius. O medidor e o gráfico são implementados no template do FlowFuse Dashboard dentro do Node-RED; o enunciado não exige um tipo específico de nó para esses componentes.
- **Alerta visual automático:** apresentamos texto, destaque visual e eventos para BPM acima de 120 e temperatura ambiente acima de 30 °C. Confirmamos entrada em duas leituras atuais consecutivas e retorno em duas leituras até 108 BPM ou até 28 °C. Esses limites e a histerese são escolhas documentadas do grupo; 38 °C é exemplo do enunciado, não um limite obrigatório. Dados recuperados não acionam um alerta como se fossem do presente.
- **Grafana:** não utilizamos; a integração é opcional e sua ausência não constitui pendência.
- **Código do ESP32:** disponibilizamos [firmware e diagrama MQTT](../../src/fase3/firmware/cardioia_mqtt/) e o [Wokwi da Parte 2](https://wokwi.com/projects/478772789361460225).
- **Prints ou export do dashboard:** entregamos ambos: [export flows.json](../../src/fase3/node-red/flows.json) e [capturas da validação guiada](../other/fase3/evidencias/2026-10-27/reproducao/validacao_guiada/RESULTADOS.md). O export possui arquivos auxiliares no mesmo diretório; o inicializador e o guia configuram as dependências para reprodução.
- **Relatório mínimo de duas páginas:** entregamos o [relatório de quatro páginas](CardioIA_Fase3_Relatorio_MQTT_Dashboard.pdf), com arquitetura, tópicos, protocolo, configuração, dependências, execução, alertas, evidências e limites.
- **Verificação atual:** os 19 testes de `test_dashboard.cjs` passaram. Executamos `scripts/fase3/validar_cenarios_mqtt.py document/other/fase3/evidencias/2026-10-24/mqtt`, que aprovou ACK omitido/reenvio, reinício do consumidor, recuperação do endpoint e da chave, com fila final zero e nenhuma perda reportada nos pacotes conferidos. A validação visual acompanhada de 27/10 preserva entrada/retorno dos dois alertas e 41 medições únicas sem lacunas ou perdas.

Concluímos que os requisitos obrigatórios e os três entregáveis da Parte 2 estão cobertos. O broker público sem autenticação/TLS é utilizado somente com dados fictícios, com essa limitação explicitada no relatório. A conclusão se refere à aderência técnica e documental, não à atribuição de nota ou à confirmação do envio acadêmico.

## Revisão específica do Ir Além 1 — 31/10/2026

Conferimos o cliente, o serviço REST, as regras, os testes, a documentação, o relatório e a validação guiada preservada. Reexecutamos os sete testes do desafio em servidor HTTP local com porta temporária; todos passaram, sem modificar os dados da demonstração guiada ou enviar mensagens externas.

- **Cliente REST Python para envio e recebimento:** `cliente_rest.py` envia JSON por `POST /leituras` e consome a resposta de `GET /leituras`, com timeout e tratamento de erros HTTP/conexão. Disponibilizamos modos para demonstração, envio de um JSON e consulta. A API local é real, embora as medições sejam sintéticas; não exigimos serviço externo, interface gráfica ou integração automática com MQTT para este desafio.
- **Lógica de risco definida:** avaliamos BPM artificial acima de 120 e temperatura ambiente acima de 30 °C, com retorno até 108 BPM e 28 °C. Esses são alertas didáticos, sem classificar temperatura ambiente como febre ou zero acionamentos como parada cardíaca. Taquicardia, febre e ausência de movimento são exemplos do objetivo, não três detecções obrigatórias cumulativas.
- **Automação de e-mail funcional na modalidade simulada:** ao identificar um novo motivo de alerta, geramos automaticamente uma mensagem com remetente, destinatário, assunto e corpo, persistimos seu conteúdo e exportamos `.eml`. Não há composição manual nem envio SMTP. Essa modalidade atende à simulação solicitada; não afirmamos entrega em uma caixa de entrada real.
- **Controle de episódios e integridade:** não repetimos e-mails ao manter o mesmo episódio nem ao reenviar a mesma leitura. Um novo episódio pode gerar outra mensagem. Validamos contrato, coerência, ordem e conflitos; dados históricos ou sensor inválido não encerram indevidamente o episódio correspondente. Preservamos leituras e episódios após reinício e reconstruímos arquivos de e-mail ausentes.
- **Demonstração observável:** o cenário de cinco leituras produz dois e-mails, mantém o primeiro episódio sem nova mensagem na leitura 3, encerra na 4 e abre novo episódio na 5. Consultamos os dados pela API e inspecionamos os `.eml`; a validação guiada inclui consulta após reinício.
- **Relatório e clareza:** o [relatório REST/e-mail](CardioIA_Fase3_Relatorio_REST_Email.pdf) tem duas páginas, dentro do intervalo exigido de uma a duas, e descreve fluxo, regras, resultados, limites e execução sequencial. O [guia REST](rest/README.md) distingue os dois terminais, resultados esperados, arquivos e diagnóstico de falhas.
- **Organização:** mantemos cliente e serviço em `src/fase3/python/`, testes em `src/fase3/tests/test_rest.py`, dependências/contrato em `config/fase3/`, relatório e guia em `document/fase3/` e evidências em `document/other/fase3/evidencias/`. Banco e e-mails novos são gerados em `.tools/runtime/fase3/rest/`, sem misturar saídas de execução com o código versionado.

Concluímos que os quatro entregáveis e os cinco critérios descritos para o Ir Além 1 estão cobertos. A simulação de e-mail é a entrega adotada, conforme o enunciado; publicação SMTP ou RPA por interface gráfica não são exigências adicionais do texto. Esta conclusão não representa envio acadêmico confirmado nem atribuição de nota.

## Revisão específica do Ir Além 2 — 31/10/2026

Conferimos código, notebook, métricas, relatório e roteiro de vídeo contra os entregáveis e critérios apresentados. Consultamos a API do GitHub e confirmamos `private=false` no repositório da Fase 3. O vídeo continua reservado para o último passo de produção; não o consideramos entregue.

- **Modelos funcionais:** implementamos regressão logística sobre oito atributos temporais/estatísticos e rede recorrente LIF de 24 neurônios com fuga, limiar, disparo, reset e refratariedade. A representação LIF participa efetivamente das previsões por meio de leitura logística treinada; os pesos internos são fixos. O texto permite LIF ou FHN, portanto não precisamos implementar os dois.
- **Séries temporais e comparação:** utilizamos 240 sessões sintéticas de BPM com origem e rótulos documentados. Separamos 144/48/48 sessões antes de criar janelas e comparamos nos mesmos 48 casos de teste; selecionamos parâmetros somente na validação. O objetivo não exige pacientes reais, treinamento no ESP32 ou ligação automática com o painel. Não classificamos as oscilações artificiais como doenças.
- **Comparação clara e análise crítica:** registramos métricas, matrizes, erros, intervalos e limites. O tradicional acertou 44/48 e o LIF 35/48, com F1 macro 0,9165 e 0,7262. Explicamos as diferenças de representação e os limites de semente única, dados sintéticos e medição em CPU. O enunciado não exige que o modelo neuromórfico supere o tradicional.
- **Notebook comentado e organizado:** entregamos [notebook](../../src/fase3/notebooks/comparacao_temporal_lif.ipynb) com objetivo, dados, divisão, modelos, avaliação, visualizações, interpretação, referências e reprodução. Conferimos seis células de código com execução registrada, sem saída de erro. O notebook utiliza o módulo do experimento no próprio repositório; dependências e caminhos estão documentados.
- **GitHub público com código e README:** confirmamos a visibilidade pública e a presença local do código, README e guia. As revisões documentais de 31/10 ainda dependem de commit/publicação; não tratamos o texto local como publicado.
- **Relatório comparativo:** o [relatório tradicional/LIF](CardioIA_Fase3_Relatorio_Neuromorfismo.pdf) possui exatamente duas páginas, com metodologia, resultados, análise crítica, limitações e reprodução.
- **Vídeo com análise crítica:** ainda precisamos gravar até quatro minutos, publicar no YouTube como não listado, incluir o endereço real no campo reservado do README e conferir o acesso. O roteiro de narração é material interno, não integra a entrega pública e não substitui o vídeo nem comprova sua qualidade final.

Concluímos que código, notebook, comparação e relatório estão implementados e documentados. O Ir Além 2 ainda não está 100% entregue: falta o vídeo e sua publicação/link/conferência. Só vamos marcar o quarto entregável e o critério de demonstração em vídeo após sua realização.

## Aceite antes da submissão

- [x] Produzimos os dois relatórios obrigatórios e conferimos as duas páginas do Edge e as quatro de MQTT/dashboard.
- [x] Concluímos a revisão técnica dos dois relatórios obrigatórios em 28/10/2026: conteúdo, comandos, identificação e paginação.
- [x] Produzimos o relatório REST/e-mail de duas páginas e conferimos sua paginação.
- [x] Produzimos o relatório comparativo do Ir Além 2 e conferimos suas duas páginas.
- [x] Concluímos a validação guiada do Ir Além 2: comparação, gráficos, notebook, HTML e seis testes com `OK`.
- [x] Concluímos a revisão técnica dos relatórios REST/e-mail e tradicional/LIF em 28/10/2026.
- [x] Executamos o cliente REST e a simulação de e-mail, com consulta após reinício e evidências preservadas.
- [x] Executamos os dois modelos nas mesmas sessões de teste e preservamos métricas, previsões, divisão e notebook executado.
- [ ] Publicar o vídeo específico do Ir Além 2 e inserir o link no README raiz.
- [x] Reproduzimos instalação e serviços em cópia nova, conferimos REST após reinício e concluímos a repetição visual acompanhada no Wokwi: sensores, entrada/retorno dos alertas e recuperação pela chave. Preservamos 41 medições únicas sem lacunas ou perdas na [validação guiada de 27/10](../other/fase3/evidencias/2026-10-27/reproducao/validacao_guiada/RESULTADOS.md). A operação acompanhada está identificada separadamente do ensaio de rede Python.
- [x] Conferimos acesso público aos repositórios, dois Wokwi, pastas do Drive, portal e vídeo da Fase 2; reativamos o Streamlit em repouso e confirmamos sua página inicial. Preservamos os links anteriores.
- [ ] Publicar e conferir o novo vídeo do Ir Além 2 sem autenticação obrigatória.
- [x] Conferimos os três integrantes/RMs no README e nos quatro relatórios.
- [ ] Conferir o cadastro efetivo do grupo na plataforma antes do envio: o recorte fornecido lista apenas um participante, enquanto o projeto identifica três integrantes.
- [ ] Conferir o arquivo correto, enviar pela plataforma com antecedência e reabrir/baixar o arquivo enviado para confirmar o conteúdo. A imagem de orientação avisa que não é possível substituir o arquivo após o fechamento da entrega ou a correção.
- [ ] Registrar o envio efetivamente confirmado, sem confundir merge no GitHub com submissão na FIAP.

## Resultado da auditoria de 26/10/2026

Relemos o enunciado Word e suas duas imagens, comparamos a estrutura com o modelo oficial FIAP e conferimos a `main` publicada no commit `6fd6aba`. Confirmamos repositório público e aprovação dos quatro workflows nesse commit, incluindo os treinamentos e notebooks da Fase 2. Conferimos os 372 destinos atuais do mapa de organização, 286 conteúdos protegidos, 157 links locais e os seis testes de proteção. Mantemos os 223 itens do inventário anterior: 212 arquivos locais e 11 aulas identificadas pelo hash original no histórico. As 63 retiradas de apoio continuam individualizadas no registro de higienização; mantemos os documentos submetidos, os enunciados, os dados e as evidências funcionais.

Conferimos no código os parâmetros documentados de sensores, fila, MQTT e alertas. Corrigimos trechos remanescentes no singular, uma forma verbal incorreta e a referência a aulas já retiradas. Ampliamos o guia de testes para reunir as verificações Python, Node-RED, os dois núcleos C++, os registros Edge/MQTT e a compilação das duas variantes ESP32. Esses ajustes são documentais; não alteramos os programas ou as evidências.

**Conclusão:** a organização e a implementação obrigatória estão acompanhadas por evidências, mas a entrega acadêmica ainda está incompleta. Após a auditoria, produzimos os dois relatórios obrigatórios e conferimos seu conteúdo, renderização e paginação. Ainda precisamos concluir a revisão final do grupo, os dois desafios e seus relatórios, publicar o vídeo específico e fechar a reprodução e a submissão. Não atribuímos nota antecipada nem marcamos essas pendências como concluídas.

Os dois links Wokwi continuam identificados por finalidade. Nesta auditoria, as consultas automatizadas receberam HTTP 403; esse bloqueio não comprova que os projetos estejam privados ou inválidos. Mantemos pendente a conferência manual em sessão sem autenticação dos projetos, das pastas do Drive, das publicações e dos vídeos. Conferir os acessos novamente no fechamento do pacote final.

## Atualização da revisão técnica de 28/10/2026

Concluímos a revisão dos quatro relatórios, a validação guiada dos dois desafios implementados e a conferência dos links públicos e dos integrantes nos documentos. Os nove testes de modelos/exportação passaram, além dos testes de contratos, persistência, REST e painel. A [conferência do pacote](../other/fase3/evidencias/2026-10-28/REVISAO_ENTREGA.md) atualiza as pendências da auditoria histórica acima: faltam o vídeo do Ir Além 2, a conferência do cadastro/formatos na plataforma e o envio. O vídeo da Fase 2 foi preservado.

## Regras da plataforma para o fechamento

- [ ] Entregar até **04/11/2026 às 23h59**; o enunciado limita a até 70% a nota das atividades entregues nos três dias seguintes ao prazo.
- [ ] Conferir integrantes e RMs no cadastro efetivo: o recorte arquivado lista somente Murilo, enquanto o repositório identifica três integrantes. O recorte não confirma o cadastro atual.
- [ ] Conferir o arquivo enviado e seu conteúdo pela plataforma. A orientação informa que não é possível substituí-lo após o fechamento da entrega ou a correção do professor.
- [ ] Respeitar a orientação de não compartilhar respostas em grupos de WhatsApp, Discord ou Microsoft Teams.

Após a publicação da nota, eventual pedido de revisão deve observar o prazo máximo de 15 dias indicado na orientação arquivada. O merge no GitHub não representa envio à plataforma.

Adotamos PDF como formato planejado para os relatórios; o enunciado fornecido exige paginação, mas não especifica extensão ou tamanho máximo do upload. Conferir os formatos aceitos e os limites efetivos da plataforma antes de montar o pacote final.
