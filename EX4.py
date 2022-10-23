lista = []
identificador = 0

def cadastrar_funcionario(id):
    print('\nO ID do novo funcionário: |>{}<|'.format(id))
    nome = input('Digite o nome do funcionário: ')
    setor = input('Digite o setor: ')
    salario = input('Informe o salário:R$ ')
    dicionarioFuncionario = {'\nID': id,
                             'Nome': nome,
                             'Setor': setor,
                             'Salario': salario}
    lista.append(dicionarioFuncionario.copy())
    print('\nFuncionário cadastrado!'.upper())

def consultar_funcionarios():
    while True:
        try:    
            print('\nConsultar funcionários:'.upper())
            consulta = int(input('Entre com a opção desejada:\n'
                                '1 - Consultar todos os funcionários\n'
                                '2 - Consultar Funcionário po id\n'
                                '3 - Consultar Funcionários(s) por setor\n'
                                '4 - Retornar\n'
                                '=>' ))
            if consulta == 1:
                print('\nBem-vindo consultar todos!'.upper())
                for dicionarioFuncionario in lista:
                    for key, value in dicionarioFuncionario.items():
                        print('{}:> {}'.format(key,value))
                        
            elif consulta == 2:
                print('\nBem-vindo a consultar o id!'.upper())
                entra = int(input('Digite o id de funcionário:> '))
                for funcionario in lista:
                    if funcionario['ID'] == entra:
                        for key, value in funcionario.items():
                            print('{}:> {}'.format(key,value))
                            
            elif consulta == 3:
                print('\tBem-vindo aconsultar funcionário(s) por setor!')
                entra = input('Digite o setor do funcionário:> ')
                for funcionario in lista:
                    if funcionario['Setor'] == entra:
                        for key, value in funcionario.items():
                            print('{}:> {}'.format(key,value))
                            
            elif consulta == 4:
                return
            else:
                print('Digite apenas os números apresentados!')
                continue
        except ValueError:
            print('Pare de inserir um valor não inteiro!')

def remover_funcionario():
    print('\tBem-vindo a remover funcionário(s)!')
    entra = input('Digite o id do funcionário:> ')
    for funcionario in cadastrar_funcionario:
        if funcionario['id'] == entra:
            funcionario.remove(funcionario)

while True:
    try:
        print('\nBem-vindo ao controle de funcionários do Gabryel Lima Da Silva')
        print(62 * '*')
        print(23 * '_' + 'MENU PRINCIPAL' + 25 * '_')
        print('\nEscolha alguma opção:')
        print('1-Cadastrar Funcionário')
        print('2-Consultar Funcionário(s)')
        print('3-Remover funcionário')
        print('4-Sair')
        a = int(input('=> '))
        print(62 * '-')

        if a == 1:
            print('Bem-vindo ao cadastrar funcionários:'.upper())
            id = input('\nDigite o ID do funcionário novo: ')
            cadastrar_funcionario(id)
        elif a == 2:
            consultar_funcionarios()
        elif a == 3:
            remover_funcionario()
        elif a == 4:
            print('Finalizando o programa...')
            break
        else:
            print('Digite apenas os números apresentados!')
            break
    except ValueError:
        print('Pare de inserir um valor não inteiro!')
        continue 