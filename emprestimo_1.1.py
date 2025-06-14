#Emprestimos de Livro 

class livros:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return print(f'\nO livro "{self.titulo}" foi emprestado com sucesso.\n')
        else:
            return print(f'\nO livro "{self.titulo}" não está disponível para empréstimo.\n')

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return print(f'O livro "{self.titulo}" foi devolvido com sucesso.')
     
    def exibirinformacoes(self):
        status = "Disponivel" 
        if not self.disponivel:
            status = "Indisponivel"
        return print(f"\nTitulo: {self.titulo}\nAutor: {self.autor}\nISBN: {self.isbn}\nStatus:{status}\n")
    
    def __str__(self):
        return f"{self.titulo}" 
    

class usuario:
    def __init__(self, nome, num_id):
        self.nome = nome
        self.num_id = num_id 

    def exibirtipousuario(self):
        pass 

    def __str__(self):
        return f"{self.nome}"

class aluno(usuario):
    def __init__(self, nome, num_id, curso):
        super().__init__(nome, num_id)
        self.curso = curso
    
    def exibirtipousuario(self):
        return print(f"\nAluno: {self.nome}\nID:{self.num_id}\nCurso:{self.curso}\n")

class professor(usuario):
    def __init__(self, nome, num_id, departamento):
        super().__init__(nome, num_id)
        self.departamento = departamento
    
    def exibirtipousuario(self):
        return print(f"\nProfessor: {self.nome}\nID:{self.num_id}\nDepartamento:{self.departamento}\n")

class emprestimo: 
    def __init__(self, titulo, nome, data_emprestimo, data_devolucao):
        self.titulo = titulo
        self.nome = nome
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
    
    def ExibirResumoEmprestimo(self):
       print("="* 10)
       print("Resumo do Empréstimo")
       print(f"Livro: {self.titulo}")
       print(f"Usuário: {self.nome}")
       print(f"Data de Empréstimo: {self.data_emprestimo}")
       print(f"Data de Devolução: {self.data_devolucao}")
       print("="*10)   


livros_registrados = []
usuarios_registrados = []
emprestimos_registrados = []


def exibir_menu():
    print("Menu:")
    print("1. Entrada da bibliotecaria")
    print("2. Entrada da Administração")
    print("3. Emprestimo de livros")
    print("4. Pegar emprestado de livros")
    print("5. sair")

def menu_administracao():
    print("\nMenu de Administração:")
    print("1. Cadastrar novo Aluno")
    print("2. Cadastrar novo Professor")
    print("3. Voltar ao menu principal")


if __name__ == "__main__":

    print("Bem-vindo a Biblioteca Dev!")
    
    while True: 
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            print("Introduza os dados do novo livro:")
            titulo = input("Título: ")
            autor = input("Autor: ")    
            isbn = input("ISBN: ")
            novo_livro = livros(titulo, autor, isbn)
            livros_registrados.append(novo_livro)
            print(f"\nLivro {novo_livro.exibirinformacoes()} adicionado com sucesso!")
        elif opcao == "2":
            while True:
                menu_administracao()
                opcao_admin = input("\nEscolha uma opção: ")
                if opcao_admin == "1":
                    nome = input("Nome do Aluno: ")
                    num_id = input("ID do Aluno: ")
                    curso = input("Curso do Aluno: ")
                    novo_aluno = aluno(nome, num_id, curso)
                    usuarios_registrados.append(novo_aluno)
                    print("=="*20)
                    novo_aluno.exibirtipousuario()
                    print(f"Aluno cadastrado com sucesso!\n")
                    print("=="*20)
                elif opcao_admin == "2":
                    nome = input("Nome do Professor: ")
                    num_id = input("ID do Professor: ")
                    departamento = input("Departamento do Professor: ")
                    novo_professor = professor(nome, num_id, departamento)
                    usuarios_registrados.append(novo_professor)
                    print("=="*20)
                    novo_professor.exibirtipousuario()
                    print(f"Professor cadastrado com sucesso!\n")
                    print("=="*20)
                elif opcao_admin == "3":
                    print("\nVoltando ao menu principal...\n")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif opcao == "3":
            titulo = input("Título do livro: ")
            nome_usuario = input("Nome do usuário: ")
            data_emprestimo = input("Data de empréstimo (DD/MM/AAAA): ")
            data_devolucao = input("Data de devolução (DD/MM/AAAA): ")
            livro = next((l for l in livros_registrados if l.titulo == titulo), None)
            usuario = next((u for u in usuarios_registrados if u.nome == nome_usuario), None)
           
            if livro and usuario:
                if livro.disponivel:
                    livro.emprestar()
                    emprestimo = emprestimo(livro, usuario, data_emprestimo, data_devolucao)
                    emprestimos_registrados.append(emprestimo)
                    print("\nLivro emprestado com sucesso!")
                    emprestimo.ExibirResumoEmprestimo()
                else:
                    print("\nLivro indisponível.")
            else:
                print("\nLivro ou usuário não encontrado.")

        elif opcao == "4":
            titulo = input("Digite o título do livro: ")
            livro = next((l for l in livros_registrados if l.titulo == titulo), None)

            if livro:
                acao = input("\nDeseja (1) Emprestar ou (2) Devolver o livro? \n")
                if acao == "1":
                    livro.emprestar()
                elif acao == "2":
                    livro.devolver()
                else:
                    print("Opção inválida.")
            else:
                print("Livro não encontrado.")
        elif opcao == "5":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

