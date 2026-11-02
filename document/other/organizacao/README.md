# Organização e preservação do CardioIA

Organizamos o repositório conforme o [modelo FIAP](https://github.com/agodoi/templateFiapVfinal). Mantemos `.github`, `assets`, `config`, `document`, `scripts` e `src` na raiz, com os materiais das três fases em suas respectivas subpastas.

## Caminhos e preservação

- [Mapa de arquivos](mapa_arquivos.json): relaciona os caminhos anteriores aos atuais.
- [Mudanças de padronização](mudancas_padronizacao.json): registra a organização por fase.
- [Inventário da Fase 1](preservacao_fase1.json): identifica os arquivos e seus hashes de origem.
- [Registro de higienização](higienizacao.json): identifica materiais retirados por caminho, categoria, hash e commit de recuperação.

Preservamos dados, código, notebooks, resultados e PDFs das entregas anteriores. Os [guias atuais](../../README.md) utilizam os caminhos organizados por fase; os documentos históricos mantêm os caminhos originais.

## Links anteriores

Mantemos as três pastas Drive da Fase 1 e o vídeo da Fase 2 nas respectivas seções do README raiz. Os endereços estão registrados em [links_externos_preservados.json](links_externos_preservados.json).

As versões históricas das [Fases 1](https://github.com/murilosalla-blip/fiap-ano02-fase01-cardioia) e [2](https://github.com/murilosalla-blip/fiap-ano02-fase02-cardioia) estão em repositórios próprios. O [endereço original](https://github.com/murilosalla-blip/fiap-ano02-fase01-cap01-cardioia) e a [URL Git original](https://github.com/murilosalla-blip/fiap-ano02-fase01-cap01-cardioia.git) redirecionam ao repositório da Fase 3.

## Arquivos gerados durante a execução

Ambientes virtuais, dependências, bancos SQLite e e-mails simulados ficam nas pastas locais indicadas nos guias, fora do versionamento. `src/fase2/app.py` e seu `requirements.txt` permanecem como entrada da aplicação Streamlit.

Em cópias antigas com dados em `fase3/runtime`, encerrar o painel e o consumidor antes de executar `python scripts/fase3/migrar_runtime.py`. O migrador preserva a origem e recusa sobrescrever destinos existentes. Cópias novas utilizam diretamente os caminhos dos guias.

## Como verificar a preservação

Após preparar o ambiente Python, executar na raiz:

```powershell
.\.venv\Scripts\python.exe scripts/validar_organizacao.py
.\.venv\Scripts\python.exe scripts/fase1/verificar_preservacao.py
.\.venv\Scripts\python.exe -m unittest discover -s scripts/tests -p 'test_*.py' -v
```

O primeiro verificador confere os destinos, conteúdos protegidos e links locais. O segundo compara os arquivos da Fase 1 com o inventário de origem. Os testes verificam as regras de preservação e recuperação.
