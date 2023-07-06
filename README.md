

<h1>BiblioteKA</h1>

<h2>Objetivo do Projeto</h2>
	
BiblioteKA é uma aplicação web desenvolvida para a gestão de uma biblioteca. Ela permite o cadastro e gerenciamento de livros, controle de empréstimos, além de possibilitar o cadastro e autenticação de usuários.

<h2>Como Usar a API</h2>
	
A API do BiblioteKA oferece endpoints para interagir com a aplicação e realizar diversas operações. Você pode encontrar a documentação completa da API no arquivo <code>api-docs.md</code>. Consulte a documentação para obter mais detalhes sobre como usar cada endpoint e quais parâmetros são necessários.


<h2>Tabela de Rotas, Funcionalidades e Permissões</h2>

|Rota                            |Funcionalidade                        |Permissões        |
|--------------------------------|--------------------------------------|------------------|
|`/api/books/`                   |Listar todos os livros                 |Usuário autenticado|
|`/api/books/:book_id/`          |Detalhes de um livro específico        |Usuário autenticado|
|`/api/books/:book_id/rent/`     |Realizar empréstimo de um livro        |Usuário autenticado|
|`/api/rents/`                   |Realizar o registro de um empréstimo   |Usuário autenticado|
|`/api/users/`                   |Listar todos os usuários               |Usuário autenticado|
|`/api/users/:user_id/`          |Detalhes de um usuário específico      |Usuário autenticado|
|`/api/users/:user_id/status/`   |Verificar o status de um usuário       |Administrador      |

<h2>Dificuldades do Projeto</h2>

##Durante o desenvolvimento do projeto BiblioteKA, foram encontradas algumas dificuldades, incluindo:

- Gerenciamento de datas e prazos de devolução.
- Implementação do bloqueio de novos empréstimos.
- Controle de permissões e autenticação dos usuários.

<h2>Colaboradores</h2>

O projeto BiblioteKA foi desenvolvido por uma equipe de colaboradores dedicados. Agradecemos a contribuição de todos os envolvidos. Os colaboradores que participaram deste projeto são:
	
Adryel César - <a href="https://www.linkedin.com/in/adryel-bueno">LinkedIn</a> | <a href="https://github.com/adryel01">GitHub</a>
João Fernandes - <a href="">LinkedIn</a> | <a href="https://github.com/ja1rocambole">GitHub</a>
Nagilo Santos - <a href="https://www.linkedin.com/in/nagilo-santos-bb1b93199/">LinkedIn</a> | <a href="https://github.com/nagilosantos">GitHub</a>
Vitor Hugo Mendes - <a href="https://www.linkedin.com/in/vitorhugomendes/">LinkedIn</a> | <a href="https://github.com/vitorhugomendes">GitHub</a>
		
