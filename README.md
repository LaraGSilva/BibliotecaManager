# Projeto de Prática de POO em Python: Gerenciamento de Biblioteca 📚

Este projeto foi desenvolvido para praticar os conceitos de Programação Orientada a Objetos (POO) na linguagem Python. Ele consiste em uma classe chamada `Livro`, que representa livros em uma biblioteca. A classe possui um construtor para inicializar os livros e uma lista para armazenar os novos livros criados (objetos). Além disso, utiliza decoradores de `property` para facilitar o retorno dos valores dos atributos e o método `classmethod` para indicar que o método pertence à classe.

## Funcionalidades da Classe `Livro`:

- **Construtor:** O construtor da classe `Livro` é responsável por inicializar os livros e adicioná-los à lista de livros disponíveis na biblioteca.

- **Decoradores de Property:** Os decoradores de `property` são utilizados para facilitar o acesso aos atributos dos livros, tornando mais fácil retornar seus valores.Eles permitem que métodos sejam acessados como se fossem atributos simples, melhorando a legibilidade e a manutenção do código.

- **Método `classmethod`:** O método `classmethod` é utilizado para definir métodos que pertencem à classe como um todo, em vez de pertencerem a instâncias específicas da classe.

- **Métodos:**
    - `emprestar()`: Este método permite emprestar um livro da biblioteca, marcando-o como indisponível.
    - `verificar_disponibilidade()`: Este método verifica se um livro está disponível na biblioteca para empréstimo.
    - `listar_livros()`: Este método lista todos os livros disponíveis na biblioteca.

Essas funcionalidades permitem gerenciar os livros em uma biblioteca de forma eficiente, facilitando o empréstimo e a verificação de disponibilidade dos livros. O uso de conceitos avançados de POO, como decoradores e métodos de classe, torna o código mais modular e fácil de manter.
