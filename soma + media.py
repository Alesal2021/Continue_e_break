soma = 0
cont = 1
while cont <= 5:
  s1 = int(input('Digite um valor {}ª numero '.format(cont)))
  soma = soma + s1
  cont = cont + 1
media = soma / 5
print('O somatorio = {} e a media = {}'.format(soma,media))