# espresso
Api em Flask com intenção de ser escalável, com estrutura pensada para seguir um padrão *Domain Drive Design*. O nome *espresso* veio em homenagem ao grande companheiro dos desenvolvedores, o café expresso.

### Execução Docker:
O repositório possui ambiente Docker pronto para levantar a estrutura necessária, localmente. 

Para levantar o ambiente é necessário:
- Adicionar um arquivo *.env* baseado no arquivo *.env_example*.

## Docker:

### Instalação:
`$ make install`

### Execução ambiente dev:
`$ make run`

### Remoção de containers & diretórios *lib* e *mysql-data*:
`$ make clean`

---

### Execução Local:
Aconselhamos que seja utilizado o Docker para testes, mas se desejar executar a api em seu ambiente local, você poderá efetuar os seguintes passos:
- Crie o seu próprio *virutalenv* baseado no python 3.8
- Instale as dependências contidas no arquivo *requirements.txt*
- Registre as variáveis do arquivo *.env_example* junto ao seu *virtualenv*

#### run:
`$(venv) uwsgi --ini="uwsgi.ini"`

---

## #TODO:
- [x] Adicionar execução através de script uWSGI.
- [x] Renomear o domínio de teste 'File' para algo mais intuitivo.
- [ ] Adicionar driver MongoDB em "app/core".
- [x] Adicionar driver Mysql em "app/core".
- [ ] Adicionar driver PostgreSQL em "app/core".
- [ ] Adicionar suporte ao Redis em "app/core".
- [x] Melhorar código por linters.
- [x] Criar comando 'make lint'.
- [ ] Criar paradigma de migrations.
- [ ] Criar entidades/models de exemplo.
- [ ] Incluír unittest.


<br>

## Domínios e Bibliotecas:

### Domínio 'example':
O domínio 'example' serve apenas como teste para iniciar o desenvolvimento da API.

### *Bibliotecas do domínio:*
- jsonify

<br>

### *Endpoints:*

---

#### /main - [GET]:
Testa se a rota do domínio está respondendo de acordo, executando no *Controller* do domínio *File*, a função *mainPage()*.

<br>

***Resposta:***
```json
{
  "message": "Main Success",
  "status": 200
}
```

#### /check_db - [GET]:
Testa a comunicação com o banco. Retorna os bancos disponíveis na base.

<br>

***Resposta:***
```json
{
  "message": [
    [
      "espresso_db"
    ],
    [
      "information_schema"
    ],
    [
      "mysql"
    ],
    [
      "performance_schema"
    ]
  ],
  "status": 200
}
```

---

### *CLI:*

---

#### espresso hello:
```
Usage: espresso hello [OPTIONS]

  A greet function.

Options:
  --name TEXT  Your name.
  --help       Show this message and exit.
```