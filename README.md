# SCME - Sistema de Gestão da Central de Material e Esterilização
Este é um sistema de gerenciamento para uma Central de Material e Esterilização (CME), desenvolvido com Django no backend e React no frontend. O objetivo principal do projeto é permitir a rastreabilidade de materiais, cadastro de usuários e geração de relatórios.

## Tecnologias Utilizadas
+ Backend: Django, Django REST Framework
+ Frontend: React, Vite
+ Banco de Dados: PostgreSQL
+ Orquestração: Docker Compose
+ Funcionalidades
  1. Cadastro de Usuários: Adicionar usuários (técnicos, administrativos e de enfermagem) com informações como nome, email, CPF e profissão.
  2. Cadastro de Materiais: Registrar materiais com informações como nome, tipo, serial e validade.
  3. Rastreabilidade de Materiais: Acompanhar o histórico e status dos materiais, com detalhes de falhas e etapas completadas.
  4. Geração de Relatórios: Criar relatórios em PDF e XLSX sobre materiais e usuários.


## Estrutura do Projeto
A estrutura do projeto é organizada da seguinte maneira:

```
/SCME
     /backend                # Backend Django com a API
        /core                # Contém os modelos e views da aplicação
        /migrations          # Arquivos de migração do banco de dados
        manage.py            # Script principal para rodar o Django
    /frontend               # Frontend em React
        /src
        /public
        package.json         # Dependências do projeto React
    index.html              # Arquivo HTML principal
    docker-compose.yml      # Arquivo para orquestrar o Docker
    README.md               # Este arquivo de documentação
```
 

## Instalação e Configuração
1. Clone o repositório
2. Para subir os containers com Docker Compose
No diretório raiz do projeto, onde o arquivo docker-compose.yml está localizado, execute:

`docker-compose up --build`

Isso irá construir e iniciar os containers para o backend, frontend e banco de dados.

Para verificar se está funcionando:
O frontend estará disponível em http://localhost:3000.
O backend estará disponível em http://localhost:8000.
O pgAdmin para gerenciar o banco de dados estará disponível em http://localhost:5050 (acesso via navegador).


## Cadastro de Usuários e Materiais
+ Cadastro de Usuário: Acesse a API de cadastro de usuários através do frontend
http://localhost:8000/api/usuarios/
Corpo do Usuário:
```
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "cpf": "12345678901",
  "profissao": "Técnico"
}
```

+ Cadastro de Material: Acesse a API de cadastro de materiais. 
http://localhost:8000/api/materials/
Corpo do Material:

```
{
  "nome": "Esterilizador XYZ",
  "tipo": "Equipamento",
  "serial": "XYZ12345",
  "validade": "2025-12-31"
}
 
 
```

## Testando a Pesquisa
+ Pesquisar Usuários: Utilize o endpoint /api/usuarios/ para realizar uma pesquisa por usuários.
A partir dele, é aberto uma interface para o usuário interagir, que o possibilita pesquisar os materiais filtrando a partir de seus atributos, como nome, serial, id, etc.



## Testando a Pesquisa
+ Pesquisar Materiais: 
Utilize o endpoint /api/materials/ para realizar uma pesquisa por usuários.
+ Pesquisar Usuários: 
Utilize o endpoint /api/usuarios/ para realizar uma pesquisa por usuários.

Ex.: `http://localhost:8000/api/usuarios/?search=João`

Ex.: `http://localhost:8000/api/materials/?search=Esterilizador` 
