

## :books: BiblioteKA

## :dart: Objetivo do Projeto
	
BiblioteKA é uma aplicação web desenvolvida para a gestão de uma biblioteca. Ela permite o cadastro e gerenciamento de livros, controle de empréstimos, além de possibilitar o cadastro e autenticação de usuários.

## :rocket: Como Usar a API
	
A API do BiblioteKA oferece endpoints para interagir com a aplicação e realizar diversas operações. Você pode encontrar a documentação completa da API através deste <a href='https://m5-t15-deployfinalproject.onrender.com/api/docs/' target='_blank'>link</a>. Consulte a documentação para obter mais detalhes sobre como usar cada endpoint e quais parâmetros são necessários.


<h2>Tabela de Rotas, Funcionalidades e Permissões</h2>

| Rota                         | Funcionalidade                     | Permissões            | Tipo de Requisição |
|------------------------------|-----------------------------------|-----------------------|-------------------|
| `/api/books/`                | Lista todos os livros            | Usuário autenticado   | GET               |
| `/api/books/`                | Cadastra um novo livro           | Usuário autenticado   | POST              |
| `/api/books/{id}/`           | Detalhes de um livro específico   | Usuário autenticado   | GET               |
| `/api/rents/`                | Realiza empréstimo de um livro   | Usuário autenticado   | POST              |
| `/api/rents/{id}`            | Realiza a devolução de um livro emprestado | Usuário autenticado | PATCH      |
| `/api/users/`                | Lista todos os usuários          | Usuário autenticado   | GET               |
| `/api/users/`                | Cadastra um novo usuário         | Qualquer usuário      | POST              |
| `/api/users/{id}/`           | Detalhes de um usuário específico | Usuário autenticado   | GET               |
| `/api/users/{id}/`           | Atualiza os dados de um usuário específico | Usuário autenticado   | PATCH    |
| `/api/users/{id}/`           | Deleta um usuário específico   | Administrador         | DELETE            |
| `/api/users/{id}/status/`    | Verifica o status de um usuário  | Administrador         | GET               |
| `/api/users/{id}/history/`   | Verifica o histórico de empréstimos de um usuário | Usuário autenticado | GET|
| `/api/users/login/`          | Autentica um usuário cadastrado   | Qualquer usuário      | POST              |


## :wrench: Dificuldades do Projeto

Durante o desenvolvimento do projeto BiblioteKA, foram encontradas algumas dificuldades, incluindo:

- Gerenciamento de datas e prazos de devolução.
- Implementação do bloqueio de novos empréstimos.
- Controle de permissões e autenticação dos usuários.

## :handshake: Colaboradores

O projeto BiblioteKA foi desenvolvido por uma equipe de colaboradores dedicados. Agradecemos a contribuição de todos os envolvidos. Os colaboradores que participaram deste projeto são:
	
- Adryel César <a href="https://www.linkedin.com/in/adryel-bueno">LinkedIn</a> | <a href="https://github.com/adryel01">GitHub</a>
- João Fernandes <a href="https://www.linkedin.com/in/jo%C3%A3o-fernandes-da-silva-neto/">LinkedIn</a> | <a href="https://github.com/ja1rocambole">GitHub</a>
- Nagilo Santos <a href="https://www.linkedin.com/in/nagilo-santos-bb1b93199/">LinkedIn</a> | <a href="https://github.com/nagilosantos">GitHub</a>
- Vitor Hugo Mendes <a href="https://www.linkedin.com/in/vitorhugomendes/">LinkedIn</a> | <a href="https://github.com/vitorhugomendes">GitHub</a>

