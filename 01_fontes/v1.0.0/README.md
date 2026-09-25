# Monitoramento de Certificados Digitais

## 1. Descrição

Aplicação desenvolvida para realizar o monitoramento automatizado de
certificados digitais disponibilizados em uma página web.

A ferramenta acessa a URL configurada, realiza a leitura da tabela de
certificados, identifica os certificados configurados para monitoramento,
verifica seus respectivos status e envia um relatório por e-mail utilizando
SMTP.

A aplicação foi desenvolvida com foco em simplicidade, automação e baixa
necessidade de intervenção manual.

## 2. Versão

Versão atual: 1.0.1
Status: Versão em produção

## 3. Funcionalidades

A aplicação possui as seguintes funcionalidades:
- Acesso automático à URL dos certificados;
- Leitura da tabela disponibilizada diretamente no HTML;
- Identificação dos certificados pelo campo "Código Acesso";
- Configuração de certificados monitorados;
- Configuração de certificados ignorados;
- Verificação do status dos certificados;
- Identificação da classificação/motivo quando o certificado está
  inoperante;
- Geração de relatório em HTML;
- Envio automático do relatório por e-mail utilizando SMTP;
- Destaque visual dos certificados operantes e inoperantes;
- Execução automatizada por meio do Windows Task Scheduler.

## 4. Identificação dos Certificados
A aplicação utiliza o campo "Código Acesso" do certificado como
referência principal para determinar quais certificados devem ser
monitorados.
O identificador/nome do certificado é coletado e apresentado no
relatório, mas não é utilizado como chave de filtro.
Essa abordagem exige atualizar a configuração sempre que um certificado é
renovado e recebe um novo código de acesso.

## 5. Estrutura do Projeto
A estrutura básica do projeto é:

    MonitorCertificados/
    │
    ├── monitor.py
    ├── coletor.py
    ├── email_sender.py
    ├── config.py
    ├── requirements.txt
    └── README.md

## 6. Responsabilidade dos Arquivos
### monitor.py
Arquivo principal da aplicação.
Responsável por:
- iniciar o processo de monitoramento;
- obter os certificados;
- aplicar os filtros de certificados monitorados e ignorados;
- identificar certificados inoperantes;
- encaminhar os dados para o módulo de envio de e-mail.

### coletor.py
Responsável pela coleta das informações da página web.
Realiza:
- acesso à URL;
- leitura do conteúdo HTML;
- localização da tabela de certificados;
- extração dos dados dos certificados.

As informações coletadas incluem:
- código de acesso;
- identificador;
- status;
- classificação.

### email_sender.py
Responsável pela geração e envio do relatório por e-mail.
O relatório apresenta os certificados monitorados em uma única tabela.
Informações apresentadas:

- Código;
- Identificador;
- Status;
- Classificação.

Certificados com status "Operante" são apresentados em verde.
Certificados com status "Inoperante" são apresentados em vermelho.

Quando o certificado está inoperante, sua classificação/motivo é
apresentada no relatório.
O envio é realizado utilizando SMTP.

### config.py
Responsável pelas configurações utilizadas pela aplicação.
Entre as configurações estão:
- URL;
- certificados monitorados;
- certificados ignorados;
- destinatários;
- assunto do e-mail;
- configurações relacionadas ao envio SMTP.

As credenciais sensíveis não devem ser armazenadas diretamente no código
ou versionadas no repositório.

## 7. Certificados Monitorados
Os certificados que devem ser acompanhados devem ser adicionados à
configuração de certificados monitorados.
Exemplo:
    CERTIFICADOS_MONITORADOS = {
        "100001",
        "100002",
        "100003"
    }

A aplicação compara esses valores com o campo "Código Acesso" obtido
da página.

## 8. Certificados Ignorados
Certificados que não devem participar do monitoramento devem ser
adicionados à configuração de certificados ignorados.
Exemplo:
    CERTIFICADOS_IGNORADOS = {
        "900001",
        "900002"
    }

Os certificados ignorados são desconsiderados durante o processamento.

## 9. Requisitos

Para executar o projeto em ambiente de desenvolvimento são necessários:

- Python;
- Acesso à internet/rede corporativa;
- Acesso à URL monitorada;
- Acesso ao servidor SMTP;
- Permissões necessárias para execução da aplicação.

As bibliotecas utilizadas devem estar especificadas no arquivo:
    requirements.txt

## 10. Instalação das Dependências

Em um ambiente de desenvolvimento com Python instalado, executar:
    pip install -r requirements.txt

As dependências devem ser instaladas em um ambiente apropriado para
desenvolvimento.
Não é necessário instalar Python no servidor de produção quando a
aplicação for distribuída como executável contendo suas dependências.

## 11. Execução em Ambiente de Desenvolvimento
Para executar a aplicação diretamente pelo código-fonte:
    python monitor.py

Durante a execução, a aplicação deverá:
1. Acessar a URL configurada;
2. Obter os certificados;
3. Filtrar os certificados monitorados e ignorados;
4. Verificar os respectivos status;
5. Montar o relatório;
6. Enviar o e-mail através do SMTP.

## 12. Geração do Executável

A versão de produção é distribuída como um executável.
O executável deve ser gerado somente após a conclusão dos testes da
versão correspondente.
Exemplo utilizando PyInstaller:
    pyinstaller --onefile monitor.py

O arquivo gerado deverá ser validado antes de ser disponibilizado para
produção.
O nome final esperado é:
    MonitorCertificados.exe

## 13. Testes Antes da Publicação
Antes de gerar uma nova versão publicável, verificar:

- [ ] A URL está acessível;
- [ ] A tabela é localizada corretamente;
- [ ] Os certificados são coletados;
- [ ] Os certificados monitorados são identificados;
- [ ] Os certificados ignorados são desconsiderados;
- [ ] O status é identificado corretamente;
- [ ] A classificação dos inoperantes é apresentada;
- [ ] O e-mail é enviado corretamente;
- [ ] Os certificados operantes aparecem em verde;
- [ ] Os certificados inoperantes aparecem em vermelho;
- [ ] O executável funciona corretamente;
- [ ] Não existem credenciais expostas no código.

## 14. Processo de Publicação
O processo recomendado para uma nova versão é:

Alteração no código
    ↓
Testes em desenvolvimento
    ↓
Correção de problemas
    ↓
Atualização da versão
    ↓
Atualização do CHANGELOG
    ↓
Geração do executável
    ↓
Teste do executável
    ↓
Criação do Publicável
    ↓
Implantação no servidor
    ↓
Teste no ambiente de produção

## 15. Controle de Versão
As versões devem seguir o padrão:
    MAJOR.MINOR.PATCH
Exemplos:
    1.0.0
    1.0.1
    1.1.0
    2.0.0

Alterações maiores devem incrementar o número MAJOR.
Novas funcionalidades compatíveis devem incrementar o número MINOR.
Correções e pequenos ajustes devem incrementar o número PATCH.

## 16. Segurança
Não armazenar no código-fonte:
- Senhas;
- Tokens;
- Chaves de API;
- Credenciais SMTP;
- Outras informações sensíveis.

O código-fonte deve permanecer restrito às pessoas autorizadas.
As credenciais utilizadas para envio de e-mail devem ser armazenadas
de maneira compatível com as políticas de segurança da organização.

## 17. Manutenção
Alterações na lista de certificados monitorados ou ignorados devem ser
realizadas no código-fonte.
Como essas configurações fazem parte da aplicação atual, uma alteração
de configuração exige:

1. Alteração do código;
2. Teste;
3. Geração de novo executável;
4. Atualização da versão;
5. Atualização das notas de versão;
6. Criação de novo publicável;
7. Implantação no servidor.

A versão anterior deve ser preservada para permitir rollback.

## 18. Rollback
Caso uma nova versão apresente problemas em produção, deve ser possível
retornar à versão anterior.
Para isso, devem ser mantidos:

- Código-fonte da versão anterior;
- Executável da versão anterior;
- Notas de versão;
- Documentação correspondente.

O executável publicado no servidor deve sempre estar associado a uma
versão conhecida.

## 19. Histórico

### Versão 1.0.0
Implementação inicial da ferramenta.
Funcionalidades incluídas:

- Monitoramento de certificados;
- Identificação por nome/identificador;
- Lista de certificados monitorados;
- Lista de certificados ignorados;
- Verificação de status;
- Identificação da classificação;
- Envio de e-mail via SMTP;
- Relatório HTML;
- Execução como executável;
- Agendamento pelo Windows Task Scheduler.

### Versão 1.0.1
Correção de bugs na coleta e no filtro de certificados:

- Ajuste da coleta de status após alteração da coluna na página
  monitorada ("Status do Dado de Acesso" renomeada para "Status Login
  no Tribunal");
- Correção do filtro de certificados monitorados/ignorados no
  monitor.py para comparar pelo código de acesso, conforme a chave
  utilizada no config.py.

## 20. Responsável

Projeto: Monitoramento de Certificados Digitais
Responsável pelo desenvolvimento: João Pedro Barboza Godoi
Área: Tecnologia da Informação
Data: 13/08/2026