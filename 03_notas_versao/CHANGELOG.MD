# Histórico de Versões

## 1.0.1 - 25/09/2026

### Corrigido
- Coleta de status após a página monitorada renomear a coluna
  "Status do Dado de Acesso" para "Status Login no Tribunal".
- Filtro de certificados monitorados/ignorados no monitor.py, que
  comparava pelo campo "Identificador" enquanto o config.py já usava o
  código de acesso como chave.

## 1.0.0 - 13/08/2026

### Adicionado
- Monitoramento automático de certificados digitais.
- Consulta da tabela de certificados através da URL configurada.
- Identificação de certificados operantes e inoperantes.
- Envio automático de e-mails via SMTP.
- Lista de certificados monitorados.
- Lista de certificados ignorados.
- Exibição do código, identificador, status e classificação no e-mail.
- Execução automatizada através do Windows Task Scheduler.

### Observações
- A ferramenta é executada duas vezes ao dia, de segunda a sexta-feira.
- Os certificados são identificados pelo campo "Identificador".