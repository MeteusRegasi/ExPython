n=str(input('Digite seu nome completo: '))
nome=n.split()
n1=len(nome)
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[n1-1]))