# Continuidade do CardioIA na Fase 3

Na Fase 1, preparamos dados numéricos, textos e imagens de ECG. Na Fase 2, implementamos extração de sintomas, classificação e interfaces demonstrativas. Na Fase 3, acrescentamos monitoramento simulado com ESP32, resiliência offline, MQTT e Node-RED.

## Relação entre os dados

As bases Cleveland e de imagens de ECG não contêm séries longitudinais das leituras do ESP32. Utilizamos dados próprios da simulação IoT e séries sintéticas no experimento temporal. Mantemos as fontes e resultados de cada fase identificados separadamente.

## Arquitetura da Fase 3

1. O ESP32 lê temperatura ambiente e umidade pelo DHT22 e conta acionamentos do botão como pulsos artificiais.
2. A coleta ocorre a cada cinco segundos simulados, com fila limitada a 2.000 amostras em RAM.
3. Na Parte 1, a chave controla a conectividade booleana e a sincronização utiliza o Monitor Serial.
4. Na Parte 2, o ESP32 publica por MQTT; o consumidor Python grava em SQLite e confirma a leitura após a transação.
5. O Node-RED apresenta gráfico, gauge e alertas, distinguindo leituras atuais de dados recuperados.

A RAM é volátil. A fila preserva leituras durante interrupções da conectividade enquanto o dispositivo permanece ligado; ao lotar, descartamos novas amostras e contabilizamos perdas.

## Desafios Ir Além

- **REST e e-mail:** cliente e serviço Python para envio e consulta, avaliação de limites e geração automática de mensagens `.eml` simuladas.
- **IA temporal:** comparação de regressão logística com reservatório LIF nas mesmas sessões sintéticas de teste, com notebook, relatório e vídeo.

## Documentação

- [Guia de execução da Fase 3](../../fase3/README.md).
- [Requisitos e entregáveis](../../fase3/CHECKLIST_ENUNCIADO.md).
- [Relatórios e documentos das três fases](../../README.md).
