

	<h1>BiblioteKA</h1>

	## :memo:<h2>Objetivo do Projeto</h2>
	<p>
		BiblioteKA é uma aplicação web desenvolvida para a gestão de uma biblioteca. Ela permite o cadastro e gerenciamento de livros, controle de empréstimos, além de possibilitar o cadastro e autenticação de usuários.
	</p>

	## :wrench:<h2>Como Usar a API</h2>
	<p>
		A API do BiblioteKA oferece endpoints para interagir com a aplicação e realizar diversas operações. Você pode encontrar a documentação completa da API no arquivo <code>api-docs.md</code>. Consulte a documentação para obter mais detalhes sobre como usar cada endpoint e quais parâmetros são necessários.
	</p>

	<h2>Tabela de Rotas, Funcionalidades e Permissões</h2>
	<table>
		<thead>
			<tr>
				<th>Rota</th>
				<th>Funcionalidade</th>
				<th>Permissões</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>/api/books/</td>
				<td>Listar todos os livros</td>
				<td>Usuário autenticado</td>
			</tr>
			<tr>
				<td>/api/books/:book_id/</td>
				<td>Detalhes de um livro específico</td>
				<td>Usuário autenticado</td>
			</tr>
			<tr>
				<td>/api/books/:book_id/rent/</td>
				<td>Realizar empréstimo de um livro</td>
				<td>Usuário autenticado</td>
			</tr>
			<tr>
				<td>/api/rents/</td>
				<td>Realizar o registro de um empréstimo</td>
				<td>Usuário autenticado</td>
			</tr>
			<tr>
				<td>/api/users/</td>
				<td>Listar todos os usuários</td>
				<td>Usuário autenticado</td>
			</tr>
			<tr>
				<td>/api/users/:user_id/</td>
				<td>Detalhes de um usuário específico</td>
				<td>Usuário autenticado</td>
			</tr>
			<tr>
				<td>/api/users/:user_id/status/</td>
				<td>Verificar o status de um usuário</td>
				<td>Administrador</td>
			</tr>
		</tbody>
	</table>

	<h2>Dificuldades do Projeto</h2>
	<p>
		Durante o desenvolvimento do projeto BiblioteKA, foram encontradas algumas dificuldades, incluindo:
	</p>
	<ul>
		<li>Gerenciamento de datas e prazos de devolução.</li>
		<li>Implementação do bloqueio de novos empréstimos.</li>
		<li>Controle de permissões e autenticação dos usuários.</li>
	</ul>


	<h2>Serializers</h2>
	<p>Abaixo estão os serializers utilizados no projeto BiblioteKA:</p>

	<h3>BookSerializer</h3>
	<pre><code>
class BookSerializer(serializers.ModelSerializer):
    # Implementação do serializer BookSerializer
  </code></pre>

	<h3>CopySerializer</h3>
	<pre><code>
class CopySerializer(serializers.ModelSerializer):
    # Implementação do serializer CopySerializer
  </code></pre>

	<h3>RentSerializer</h3>
	<pre><code>
class RentSerializer(serializers.ModelSerializer):
    # Implementação do serializer RentSerializer
  </code></pre>

	<h3>UserSerializer</h3>
	<pre><code>
class UserSerializer(serializers.ModelSerializer):
    # Implementação do serializer UserSerializer
  </code></pre>

	<h3>UserStatusSerializer</h3>
	<pre><code>
class UserStatusSerializer(serializers.ModelSerializer):
    # Implementação do serializer UserStatusSerializer
  </code></pre>


	<h2>Colaboradores</h2>
	<p>
		O projeto BiblioteKA foi desenvolvido por uma equipe de colaboradores dedicados. Agradecemos a contribuição de
		todos os
		envolvidos. Os colaboradores que participaram deste projeto são:
	</p>
	<ul>
		<li>Adryel César - <a href="https://www.linkedin.com/in/adryel-bueno">LinkedIn</a> | <a href="https://github.com/adryel01">GitHub</a></li>
		<li>João Fernandes - <a href="">LinkedIn</a> | <a href="https://github.com/ja1rocambole">GitHub</a></li>
		<li>Nagilo Santos - <a href="https://www.linkedin.com/in/nagilo-santos-bb1b93199/">LinkedIn</a> | <a href="https://github.com/nagilosantos">GitHub</a></li>
		<li>Vitor Hugo Mendes - <a href="https://www.linkedin.com/in/vitorhugomendes/">LinkedIn</a> | <a href="https://github.com/vitorhugomendes">GitHub</a></li>
		
	</ul>
</body>

</html>