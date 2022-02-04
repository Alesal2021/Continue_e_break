while True:
    print('Calculadora')
    print('1 - adição')
    print('2 - multiplicação')
    print('3 - divisão')
    print('4 - subtração')
    print('5 - sair ')
    op = input('escolha uma opção: ')
    if op == '1' or op == '2' or op == '3' or op == '4':
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o primeiro valor: '))

    if (op == '1'):
        res = x + y
        print('O resultado {} + {} = {}'.format(x, y, res))
        continue
    if (op == '2'):
        res = x * y
        print('O resultado {} * {} = {}'.format(x, y, res))
        continue
    if (op == '3'):
        res = x / y
        print('O resultado {} / {} = {}'.format(x, y, res))
        continue
    if (op == '4'):
        res = x - y
        print('O resultado {} - {} = {}'.format(x, y, res))
        continue
    if (op == '5'):
        break
    else:
        print('Opção invalida')




print('Programa encerrado')