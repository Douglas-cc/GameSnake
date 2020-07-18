secreto = 'carneira'
digitados = []
chances = 5

while True:
    letra = input('Digite uma letra: ')

    if chances == 0:
        print('GAME OVER')
        break

    if letra not in secreto:
        chances -= 1
    print(f'Você tem {chances} chances')
    print()

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra')
        continue

    digitados.append(letra)

    if letra in secreto:
        print(f'Aaaah letra existe na palavra secreta {letra}')
    else:
        print(f'Infelizmente a letra {letra} não esta na palavra secreta')
        digitados.pop

    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '#'
    
    if secreto_temporario == secreto:
        print(f'Você venceu >>> {secreto_temporario}')
        break    
    else:        
        print(f'-> {secreto_temporario}')
    
    
