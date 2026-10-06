# Mini Avaliação Institucional

API desenvolvida em Django para o cadastro de alunos, disciplinas e avaliações institucionais.

## Estrutura do projeto

O projeto possui três apps principais:

- `aluno`: responsável pelos dados dos alunos.
- `disciplina`: responsável pelos dados das disciplinas.
- `avaliacao`: responsável pelas avaliações realizadas pelos alunos.

## Ambiente virtual

O ambiente virtual é criado para cada projeto para separar as dependências e versões das bibliotecas utilizadas. Assim, um projeto não interfere nas configurações ou bibliotecas de outro projeto.

## Por que utilizar três apps?

O sistema foi dividido em três apps para organizar melhor o projeto. Cada app possui uma responsabilidade específica: alunos, disciplinas ou avaliações. Isso facilita a organização, manutenção e entendimento do código.

## Migrations

O `makemigrations` cria os arquivos de migration a partir das alterações feitas nos models. Ele registra quais mudanças precisam ser aplicadas no banco de dados.

Depois usamos o `migrate`, que aplica essas migrations no banco de dados e cria ou altera as tabelas necessárias.

A ordem é:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Como executar o projeto

Entre na pasta `backend`, ative o ambiente virtual e execute:

```bash
source venv/bin/activate
python manage.py runserver
```

A API estará disponível em:

- `/api/alunos/`
- `/api/disciplinas/`
- `/api/avaliacoes/`
- `/api/avaliacoes/pendentes/`