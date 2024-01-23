class Livro:
    livro = []
    def __init__(self,titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livro.append(self)
        
    
    @property
    def disponivel(self):
        return 'Livro disponivel' if self._disponivel else 'Livro não disponivel'
    
    @property
    def ano_publicacao(self):
        return int(self._ano_publicacao)
    
    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao}'
    
    @classmethod
    def listar_livro(cls):
        print(f'{'Nome do livro'.ljust(30)} | {'Autor / Autora'.ljust(30)} | {'Ano publicado'.ljust(30)} | {'Disponibilidade'.ljust(30)}')
        for li in cls.livro:
            print(f'{li._titulo.ljust(30)} | {li._autor.ljust(30)} | {str(li._ano_publicacao).ljust(30)} | {str(li.disponivel).ljust(30)}')
        
    @classmethod
    def verificar_disponibilidade(cls):
        lista_verificada = []
        ano = int(input('Digite o ano de publicação que deseja verificar: '))
        for a in cls.livro:
            if a.ano_publicacao == ano:
                lista_verificada.append(a._titulo)
        print(lista_verificada)
            

    def emprestar_livro(self):
        self._disponivel = not self._disponivel
      