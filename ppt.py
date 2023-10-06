jokenpo = ('Pedra', 'Papel', 'Tesoura')
loop = 's'
while loop.lower() == 's':
    print('jokenpô \n [0] Pedra \n [1] Papel \n [2] Tesoura')
    nome1 = input('1 - Jogador, informe seu nome: ')
    nome2 = input('2 - Jogador, informe seu nome: ')
    jogador1 = int(input(f'{nome1}, faça sua jogada: '))
    jogador2 = int(input(f'{nome2}, faça sua jogada: '))


    if jogador1 == 0:
        if jogador2 == 0:
            print('Opa, temos um empate!')
        elif jogador2 == 1:
            print(f'{nome2} Venceu!')
        elif jogador2 == 2:
            print(f'{nome1} Venceu!')
        else:
            print('Valor inválido!')

    if jogador1 == 1:
        if jogador2 == 1:
            print('Opa, temos um empate!')
        elif jogador2 == 0:
            print(f'{nome1} Venceu!')
        elif jogador2 == 2:
            print(f'{nome2} Venceu!')
        else:
            print('Valor inválido!')

    if jogador1 == 2:
        if jogador2 == 2:
            print('Opa, temos empate!')
        elif jogador2 == 0:
            print(f'{nome2} Venceu!')
        elif jogador2 == 1:
            print(f'{nome1} Venceu!')
    loop = input('Deseja realizar uma nova partida? (S/N): ')
print('Jogo finalizado, obrigado por jogar!')
