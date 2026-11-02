# Validação local do Ir Além 2 — 27/10/2026

Implementamos e executamos a comparação em séries sintéticas, separadamente dos ensaios do Wokwi. Conferimos o protocolo antes da execução: semente 42, 240 sessões, divisão por sessão antes das janelas, 144/48/48 e seleção de C na validação.

Instalamos `config/fase3/requirements-neuromorfismo.txt` em ambiente virtual novo, em caminho curto no Windows. A primeira tentativa de criação no diretório temporário restrito não concluiu; não contamos essa tentativa como validação. A criação em diretório temporário apropriado e a instalação do zero concluíram sem erro. Nesse ambiente, executamos os seis testes e todas as células do notebook pelo inicializador do projeto. Conferimos o encerramento explícito do kernel.

As métricas por sessão e o SHA-256 dos sinais coincidiram com a primeira execução: tradicional com 44/48 acertos e LIF com 35/48. Preservamos resultados em `assets/fase3/resultados/neuromorfismo/` e o notebook executado em `src/fase3/notebooks/`. Não ajustamos parâmetros ou gerador para inverter o resultado após consultar o teste.

Conferimos visualmente as duas páginas do relatório comparativo, as matrizes de confusão e o gráfico de atividade LIF. Conferimos a série ilustrativa e a ausência de erros nas células. O notebook exportado em HTML inclui as imagens para leitura local.



## Continuidade da validação guiada — 28/10/2026

Instalamos os requisitos no ambiente `.venv` do projeto e reproduzimos as métricas de referência na comparação simples. Conferimos visualmente as séries, as matrizes e a atividade LIF. Ao executar o notebook depois de abrir os gráficos no visualizador do Windows, encontramos `OSError 22` ao regravar `series.png`.

Reproduzimos esse erro em uma cópia de PNG mantida em mapeamento de memória somente para leitura. Alteramos o notebook para criar uma pasta exclusiva em `.tools/runtime/fase3/neuromorfismo/notebooks/execucao-...` a cada execução. Mantivemos os caminhos de abertura do HTML e da cópia executada, bem como os resultados da comparação simples.

Executamos todas as células pelo Python `.venv` do projeto enquanto mantivemos o PNG anterior bloqueado. O notebook terminou sem erro; conferimos que o hash e a data de modificação do PNG anterior permaneceram intactos e que as métricas e o hash dos sinais coincidiram com a referência.

Confirmamos depois a repetição acompanhada do notebook, com a mensagem de execução sem erro, e a abertura do HTML pelo grupo. Conferimos diretamente o HTML local: seis células executadas sem erro, seis seções de desenvolvimento, métricas iguais à referência e três PNGs incorporados com hashes idênticos aos gráficos entregues. Corrigimos o link do guia na exportação, ajustando seu caminho relativo à pasta de destino, e verificamos o destino existente, os links externos e as âncoras.

Executamos os seis testes dos modelos, em 0,357 s, com `OK`: agregação/métricas, atributos temporais, dinâmica LIF, separação de sessões/janelas, geração reproduzível e normalização restrita ao treino. A instalação, a comparação simples, os três gráficos, o notebook, a leitura do HTML e os testes compõem a validação guiada concluída em 28/10/2026.
