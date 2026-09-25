# Monitor de Certificados Digitais

Ferramenta em Python para monitoramento automatizado de certificados digitais
disponibilizados em uma página web. Acessa a URL configurada, lê a tabela de
certificados, verifica o status de cada um e envia um relatório por e-mail via
SMTP. Pensada para rodar como executável agendado no Windows Task Scheduler.

## Funcionalidades

- Leitura automática da tabela de certificados (scraping com BeautifulSoup);
- Identificação dos certificados pelo campo "Código Acesso";
- Listas configuráveis de certificados monitorados e ignorados;
- Relatório HTML com destaque visual para operantes (verde) e inoperantes (vermelho);
- Envio automático do relatório por e-mail via SMTP;
- Execução agendada via Windows Task Scheduler.

## Estrutura do repositório

```
01_fontes/v1.0.1/        # Código-fonte da aplicação
02_documentacao/v1.0.1/  # Documentação técnica
03_notas_versao/         # Changelog
```

## Uso

Detalhes de configuração, instalação e execução estão no
[README do código-fonte](01_fontes/v1.0.1/README.md).

> Os valores em `config.py` neste repositório são exemplos fictícios —
> substitua pela URL, destinatários e servidor SMTP do seu ambiente antes de
> usar.

## Stack

Python · requests · BeautifulSoup · SMTP
