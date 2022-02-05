
while True:
    print('Terminal de pagamento')
    print('1 - 0 - 3 anos')
    print('2 - 4 a 12 anos  ')
    print('3 - acima de 12 anos')
    print('4 - sair')
    op = int(input('Escolha sua opção 1 2 3 4:'))
    if op == 1 or op == 2 or op == 3 or op == 4:
        if op == 4:
            print('Bom filme')
            break
        s1 = int(input('Digite sua idade:'))
        s2 = int(input('quantos ingressos:'))
        if s1 <= 3:
            pessoas = s2
            print('Sua idade e {} Ingresso gratuito total de pessoas {} '.format(s1,s2))
            continue
        elif s1 <= 12:
            pessoas = s2
            ingresso = s2 * 15
            print('Sua idade e {} anos Valor do ingresso R${} total de pessooas e {}'.format(s1,ingresso,pessoas))
            continue
        elif s1 >= 13:
            valor = 30
            ingresso = s2 * valor
            print('Sua idade e {} anos Valor do ingresso {}'.format(s1,ingresso))
            continue
        else:
            print('opção invalida')
            break





