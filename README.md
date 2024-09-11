## Projeto de Envio de Mensagens
Este projeto foi desenvolvido para enviar mensagens personalizadas através de uma API, utilizando dados de um arquivo Excel. Ele usa requests para fazer as requisições HTTP e pandas para manipulação de dados. Além disso, o projeto possui integração com Docker, utilizando contêineres para PostgreSQL e Redis.

# Estrutura do Projeto
- ```send_message.py:``` Este script é responsável por ler os dados de um arquivo YAML e de um arquivo Excel, gerar o payload de mensagens e enviá-las através de uma API HTTP.
- ```opens.py:``` Contém a classe ReadArchive, que lida com a leitura e extração de dados do arquivo Excel.
- ```datas.yaml:``` Arquivo de configuração YAML contendo o token de acesso e o caminho do arquivo Excel.
- ```Dockerfile e docker-compose.yml:``` Arquivos de configuração do Docker para subir contêineres do PostgreSQL e Redis.
  
## Dependências
```Python 3.8+```  
```requests```  
```pyyaml```  
```pandas```  
```openpyxl (para ler arquivos Excel)```  
```Docker (para gerenciar PostgreSQL e Redis)```  


## Instalação
### Clone este repositório:

``` bash
Copiar código
git clone https://github.com/seu-repositorio.git
cd seu-repositorio
```

### Crie um ambiente virtual:

```bash
Copiar código
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### Instale as dependências:

```bash
Copiar código
pip install -r requirements.txt
```

### Configure o arquivo datas.yaml com as informações necessárias, como o token de acesso e o caminho do arquivo Excel:

```yaml
Copiar código
access_token: "seu_token_aqui"
path: "caminho/para/seu/arquivo.xlsx"
URL: "caminho/do/endpoint"
```

### Execute o script principal para enviar mensagens:

```bash
Copiar código
python send_message.py
Uso do Docker
```

Este projeto inclui um ambiente Docker para PostgreSQL e Redis.
## Para iniciar os contêineres, use o docker-compose:

### Suba os serviços com o Docker:

``` bash
Copiar código
docker-compose up -d
```

### Verifique se os contêineres estão rodando:

```bash
Copiar código
docker ps
```

## Funcionalidades
```Envio de Mensagens:``` O script envia mensagens personalizadas para números de telefone fornecidos em um arquivo Excel. Muito útil para disparo de marketing e etc, mas se atente com as políticas do whatsapp.

```Leitura de Arquivos Excel:``` Lê o nome, número de telefone e IDs dos destinatários a partir de um arquivo Excel (Totalemente customizável, basta adicionar a lógica as colunas que deseja extrair os valores).  

```Integração com API:``` Faz requisições POST para a API de mensagens utilizando tokens de autenticação.

```Docker:``` O projeto pode rodar com suporte de bancos de dados e cache através de PostgreSQL e Redis.

**Estrutura do Arquivo YAML**   
```access_token:``` Token de autenticação usado para a API de mensagens.
```path:``` Caminho para o arquivo Excel contendo os dados dos destinatários.
```URL:``` Caminho do endpoint.

# Licença
Este projeto está licenciado sob a licença MIT.
