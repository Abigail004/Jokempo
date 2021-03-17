from random import choice
from time import sleep
comp1 = ['pedra', 'papel', 'tesoura']
sn = 's'
em = per = gan = 0


print('~~~~~~~~~~\033[32;1mJOKEMPÔ\033[m~~~~~~~~~~')
print('Seja bem vindo')
sleep(1)
print('REGRAS:')
sleep(1)
print('Você digitará PEDRA PAPEL ou TESOURA')
sleep(2)
print('E eu seu adversário também irei escolher PEDRA PAPEL ou TESOURA ')
sleep(2)
print('Acho que você ja jogou antes certo?')
sleep(2)
print('vamos começar??')
print('')
sleep(2)
while sn != 'n':

    if sn not in 'Ss':
        print('\033[31;1mDigite um valor válido\033[m (S :para sim e N:para não)')
        sn = input('Deseja continuar [S/N]: ')
        print()
    
    print()
    print(20*'~~')

    if sn in 'Ss':

        eu = input('Digite pedra papel ou tesoura para começar o jogo: ').lower()
        comp = choice(comp1)
        print('')
        print(20*'~~')

        while eu not in comp1:
            print('\033[31;1mDigite um valor valido\033[m')
            eu = str(input('Digite pedra papel ou tesoura: ').lower())
            print(' ')
            print(20*'~~')

        if eu == 'pedra' or 'papel' or 'tesoura':
            print('JO', end='')
            sleep(1)
            print('KEM', end='')
            sleep(1)
            print('PÔ')
            sleep(1)
            print(20*'~~')
            print(f'Você escolheu \033[32m{eu.upper()}\033[m e eu escolhi \033[31m{comp.upper()}\033[m')
            if eu == 'papel':
                if comp == 'pedra':
                    print(f' {eu} X {comp} = \033[32mVocê ganhou\033[m' )
                    gan += 1
                if comp == 'papel':
                    print(f' {eu}  X {comp}  = \033[34mEmpate\033[m')
                    em += 1
                if comp == 'tesoura':
                    print(f' {eu}  X {comp} :v: = \033[31mVocê perdeu\033[m')
                    per += 1
            if eu == 'pedra':
                if comp == 'pedra':
                    print(f' {eu} X {comp} : = \033[34mEmpate\033[m')
                    em += 1
                if comp == 'papel':
                    print(f' {eu} X {comp} = \033[31mVocê perdeu\033[m')
                    per += 1
                if comp == 'tesoura':
                    print(f' {eu} X {comp} = \033[32mVocê ganhou\033[m')
                    gan += 1

            if eu == 'tesoura':
                if comp == 'pedra':
                    print(f' {eu} X {comp} = \033[31mVoce perdeu\033[m')
                    per += 1
                if comp == 'papel':
                    print(f' {eu} X {comp} = \033[32mVocê ganhou\033[m',  )
                    gan += 1
                if comp == 'tesoura':
                    print(f' {eu} X  {comp} = \033[34mEmpate\033[m')
                    em += 1
            print('')
            print(20*'~~')
            sn = input('Deseja continuar [S/N]: ')

print(20*'~~')
print(f'Voce \033[31mperdeu {per} vezes\033[m, \033[32mGanhou {gan} vezes\033[m, e \033[34mEmpatou {em} vezes\033[m')
print('Obrigado por jogar !!!')
print(20*'~~')
