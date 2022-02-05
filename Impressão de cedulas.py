while True:
    print('Caixa eletronico')
    print('1 - conta corrente')
    print('2 - poupança')
    op = int(input('Qual tipo de saque:'))
    if op == 1 or op == 2:
        s1 = int(input('Digite o valor do saque R$100 R$50 R$20 R$10:'))
        if s1 >=100:
            cedul100 = s1 // 100
            s1 -= cedul100 * 100
            print(' Cedulas de 100 = {}'.format(cedul100))
            if not s1: # CASO SEJA VERDADEIRO ELE PARA O LAÇO, SENÃO TESTA AS OUTRAS LINHAS DEBAIXO
                break
        if s1 >=50:
            cedul50 = s1 // 50
            s1 -= cedul50 * 50
            print(' Cedulas de 50 = {}'.format(cedul50))
            if not s1:
                break
        if s1 >=20:
            cedul20 = s1 // 20
            s1 -= cedul20 * 20
            print(' Cedulas de 20 = {}'.format(cedul20))
            if not s1:
                break
        if s1 >=10:
            cedul10 = s1 // 10
            s1 -= cedul10 * 10
            print(' Cedulas de 10 = {}'.format(cedul10))
            break



    print('Seu dinheiro esta saindo aguarde.....')
    print('Obrigado por usar o caixa eletronico')







