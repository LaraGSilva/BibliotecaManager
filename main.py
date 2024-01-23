from helpers.livro import Livro

def main():
    pass

if __name__ == '__main__':
    main()
    
livro_um = Livro('O pequeno principe', 'Antoine de Saint-Exupéry', 1943)
livro_dois = Livro('Biblia', 'Jesus', 1003)
livro_tres = Livro('Querido Jhonn', 'Nicholas Sparks', 2013)
livro_quatro = Livro('Procurando Dory', 'Disney Plus', 2013)
livro_cinco = Livro('Anne a ruiva', 'Lily Jim', 1449)

livro_um.emprestar_livro()
livro_dois.emprestar_livro()

Livro.verificar_disponibilidade()
#Livro.listar_livro()
