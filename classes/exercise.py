"""
Crie um sistema simples para uma biblioteca que possa gerenciar livros e empréstimos.

Requisitos:

1. Classe Livro:
   - Deve ter os atributos: título, autor, ano de publicação, e status (se está disponível ou emprestado).
   - Deve ter os seguintes métodos:
     - `get_info()`: Retorna uma string com as informações do livro (título, autor, ano de publicação).
     - `check_out()`: Marca o livro como emprestado.
     - `check_in()`: Marca o livro como disponível.

2. Classe Cliente:
   - Deve ter os atributos: nome, e-mail e lista de livros emprestados.
   - Deve ter os seguintes métodos:
     - `borrow_book(book)`: Adiciona um livro à lista de livros emprestados do cliente, marcando o livro como emprestado.
     - `return_book(book)`: Remove um livro da lista de livros emprestados do cliente, marcando o livro como disponível.

3. Classe Biblioteca:
   - Deve ter os atributos: nome da biblioteca e uma lista de livros.
   - Deve ter os seguintes métodos:
     - `add_book(book)`: Adiciona um livro à lista de livros da biblioteca.
     - `list_books()`: Exibe a lista de livros disponíveis na biblioteca.
     - `search_book(title)`: Pesquisa um livro pelo título e retorna as informações do livro.

Dicas:
- Utilize a herança para simplificar a criação de novas funcionalidades.
- Trate o status do livro para garantir que não possa ser emprestado se já estiver emprestado, e vice-versa.

Desafio Extra:
- Implemente um sistema de multas para livros não devolvidos dentro do prazo (adicionando data de empréstimo e devolução prevista). Se o livro for devolvido depois da data prevista, adicione uma multa. """

