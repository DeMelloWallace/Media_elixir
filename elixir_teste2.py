def nome_principal_programa():
    linha_subtitulos('Média de elixir para acesso 😄') #Nome do programa

def exibir_menu():   #aqui foi criada a função de escolha de opções do restaurante
    print('Opção 1 - Cadastrar nova carta (nome e qtd de elixir): ')
    print('Opção 2 - Sair.\n')

def finalizar_programa(): #criação da opç]ao finalizar o programa
    linha_subtitulos('Obrigado por utilizar programa. 👍')
    voltar_ao_menu_principal()

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal - \n ')
    main()

def linha_subtitulos(texto):
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def media_elixir_nome_carta():
    cartas = {}

    for calculo in range(8):
        nome = input('Digite o nome da carta: ')
        try:
<<<<<<< HEAD
        quantidade_elixir = int(input(f'Digite o valor para {nome}: '))
        cartas[nome] = quantidade_elixir
        except ValueError:
            print('Valor inválido. Use apenas números.')
            return voltar_ao_menu_principal()
    
=======
            quantidade_elixir = int(input(f'Digite o valor para {nome}: '))
            cartas[nome] = quantidade_elixir
        except ValueError:
            print('Valor inválido. Use apenas números.')
            return voltar_ao_menu_principal()

>>>>>>> fefcc16 (Teste unitario(escolher opcoes))
    media = sum(cartas.values()) / len(cartas)

    print('_____Lista de cartas registradas_____')
    for nome , quantidade_elixir in cartas.items():
        print(f'{nome} : {quantidade_elixir}')

    print(f'\nA média final do seu deck é de: {media}\n')

    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolha = int(input('Escolha uma opção: '))

        if opcao_escolha == 1:
            media_elixir_nome_carta()
        elif opcao_escolha == 2:
            finalizar_programa()
        else:
            opcao_invalida()
<<<<<<< HEAD
    except valueError:
=======
    except ValueError:
>>>>>>> fefcc16 (Teste unitario(escolher opcoes))
            opcao_invalida()


def main():
    nome_principal_programa()
<<<<<<< HEAD
    exibir_menu()
=======
    escolha_opcoes()
>>>>>>> fefcc16 (Teste unitario(escolher opcoes))
    escolher_opcoes() # fluxo de decisão acontece aqui
    

if __name__ == '__main__':
    main()
