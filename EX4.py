def cadastrar_funcionario(ide):
    print('Cadastrar funcionários:')
    print('O ID do funcionário cadastrado:> {}'.format(ide))
    nome = input('Digite o nome do funcionário: ')
    setor = input('Digite o setor: ')
    salario = input('Informe o salário: ')
    dicionarioFuncionario = {'ide': ide,
                             'nome': nome,
                             'setor': setor,
                             'salario':salario}
    lista.append(dicionarioFuncionario.copy())

def consultar_funcionarios():
    while True:
        try:    
            print('Consultar funcionários:')
            consulta = int(input('Entre com a opção desejada:\n'
                                 '1 - Consultar todos os funcionários\n'
                                 '2 - Consultar Funcionário po id\n'
                                 '3 - Consultar Funcionários(s) por setor\n'
                                 '4 - Retornar\n'
                                 '=>' ))
            if consulta == 1:
                print('Bem-vindo consultar todos!')
                for funcionario in cadastrar_funcionario:
                    for key, value in funcionario.items():
                        print(' {} : {} '.format(key,value))

            elif consulta == 2:
                print('Bem-vindo a consultar o id!')
                entra = int(input('Digite o id de funcionário:> '))
                for funcionario in cadastrar_funcionario:
                    if funcionario['id'] == entra:
                        for key, value in funcionario.items():
                            print(' {} : {} '.format(key,value))

            elif consulta == 3:
                print('Bem-vindo aconsultar funcionário(s) por setor!')
                entra = input('Digite o setor do funcionário:> ')
                for funcionario in cadastrar_funcionario:
                    if funcionario['setor'] == entra:
                        for key, value in funcionario.items():
                            print(' {} : {} '.format(key,value))
            elif consulta == 4:
                return
            else:
                print('Digite apenas os números apresentados!')
                continue
        except ValueError:
            print('Pare de inserir um valor não inteiro!')


def remover_funcionario():
    print('Bem-vindo a remover funcionário(s)!')
    entra = input('Digite o id do funcionário:> ')
    for funcionario in cadastrar_funcionario:
        if funcionario['id'] == entra:
            funcionario.remove(funcionario)


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

lista = []
id = 0

while True:
    try:
        if a == 1:
            k = int(input('Digite o id do funcionário>: '))
            id = id + k
            cadastrar_funcionario(id)
        elif a == 2:
            consultar_funcionarios()
        elif a == 3:
            remover_funcionario()
        elif a == 4:
            print('Finalizando o programa...')
        else:
            print('Digite apenas os números apresentados!')
            break
    except ValueError:
        print('Pare de inserir um valor não inteiro!')
        continue  